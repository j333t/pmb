---
title: "PlusMinusBang: A Plain-Text Notation for Structured Reasoning"
abbrev: "PlusMinusBang (PMB)"
docname: draft-shah-plusminusbang-00
category: info
submissionType: independent
ipr: trust200902
area: "Applications and Real-Time"
lang: en
kw:
 - plain text
 - notation
 - reasoning
 - argumentation
 - markdown
author:
 -
    ins: J. Shah
    name: Jeet Shah
    email: connect@j33t.pro
    uri: https://plusminusbang.com

normative:
  RFC2119:
  RFC8174:
  RFC5234:
  RFC3629:

informative:
  RFC6838:
  RFC7763:
  RFC7764:
  PMB:
    title: "PlusMinusBang (PMB) v1.2"
    target: https://plusminusbang.com/pmb.md
    author:
      - name: Jeet Shah
    date: 2026-08
  PMB-DECISIONS:
    title: "PMB Design Decisions"
    target: https://plusminusbang.com/DECISIONS.md
    author:
      - name: Jeet Shah
    date: 2026-08
  UNICODE:
    title: "The Unicode Standard"
    target: https://www.unicode.org/versions/latest/
    author:
      - org: The Unicode Consortium
  ISO8601:
    title: "Date and time -- Representations for information interchange"
    target: https://www.iso.org/standard/70907.html
    author:
      - org: International Organization for Standardization
    seriesinfo:
      ISO: 8601-1:2019

--- abstract

PlusMinusBang (PMB) is a plain-text notation for structuring reasoning. A
symbol at the start of a line marks the semantic role of that line -- support,
opposition, attention, hard condition, open question, or unresolved
uncertainty -- and indentation marks which line it responds to. The notation
carries no header, no terminator, and no escape mechanism, so it can be written
in any text editor, embedded in source-code comments, and read without tooling.

This document specifies the syntax of PMB, a normative grammar in ABNF, a
deterministic parsing algorithm, and the interpretation rules a consumer must
follow. It is intended for implementers of parsers, editors, and
language-model tooling that need to exchange structured reasoning as plain
text.

--- middle

# Introduction

Plain text has no way to mark what a line is *doing*. A reader -- human or
machine -- must infer from wording whether a sentence argues for something,
argues against it, records a fixed external constraint, or admits an unknown.
That inference is unreliable, and it is discarded every time the text is read
again.

PlusMinusBang (PMB) makes the role explicit with a single leading character:

~~~
Open the second location?
+ Current place runs at 95% capacity
- Needs 30 lakh upfront
  + We have 45 lakh saved
  ! Want to keep six months of runway
    ? Can we phase the payments
* Lease is three years, no exit clause
~~~

The notation has two mechanisms and no others: a line-initial symbol marks the
kind of thought, and indentation marks what the thought responds to. Everything
else in this document is a consequence of making those two mechanisms
unambiguous.

PMB is deliberately small and is not extensible. The symbol set was frozen at
six symbols plus the unmarked line on 2026-08-09; the reasoning for each symbol,
and for the alternatives rejected, is recorded in {{PMB-DECISIONS}}.

## Design Goals

The following goals are informative, but they explain why several rules in this
document are stricter than a reader might expect.

Learnable without documentation:
: Every symbol has a reading that is already common across languages and
  formats. A specification is needed to write a parser, not to write PMB.

Capture without interruption:
: The notation is written while thinking. Any rule that forces the author to
  stop and deliberate at the moment of writing is a cost the notation cannot
  afford, which is why each symbol marks a *kind* of thought rather than a
  *degree*, and why the one graded mechanism ({{intensity}}) is optional.

Degrade safely:
: A reader, parser, or renderer that does not understand part of the notation
  must still recover the text. Nothing in PMB may be silently dropped.

Faithful to the author:
: A parser reports what was written and nothing more. It does not infer weight
  that was not stated, convert between the two graded mechanisms, or reduce a
  document to a verdict. See {{interpretation}}.

## Applicability to Language Models and Other Automated Consumers {#ai}

A substantial share of PMB's use is expected to be text written for, or
written by, language models. Three properties of the notation follow from that
case rather than from the human one. This subsection is informative; the
normative consequences are in {{interpretation}} and {{generating}}.

Structure is stated rather than inferred:
: In prose, the role a sentence plays -- whether it argues for a position,
  qualifies an earlier claim, or records a constraint that settles the
  question -- is carried by wording, and a consumer must infer it. That
  inference is unreliable, it is repeated on every reading, and it is
  invisible when it is wrong. PMB moves the role into a single leading
  character, where it is read rather than derived. This is also why a
  consumer that supplies a weight the author did not write has defeated the
  purpose of the notation: it has reintroduced the inference the notation
  exists to remove.

The same content costs fewer tokens:
: Prose signals structure with connective language -- "however", "a drawback
  of this is", "it is worth noting that". PMB signals the same relationships
  with one character and the line's indentation. Measured across three
  documents rewritten in three formats with their claim sets held constant,
  and tokenised with byte-pair encodings of the kind current models use, PMB
  used roughly 44% fewer tokens than flowing prose and roughly 16% fewer than
  a conventional bullet list. The reduction was largest in deliberative
  material and smallest in a plain status report, which is what the
  scaffolding argument predicts: what is removed is the connective tissue, not
  the claims. Most of that reduction comes from writing atomic claims rather
  than from the notation itself; against a bullet list of identical wording,
  PMB costs about 4% less, because a marked line costs what a bullet costs and
  a neutral line costs nothing. The supportable claim is therefore not that
  PMB compresses text, but that it records the role of every line at no token
  cost over a bullet list that records none. The corpus is three documents by
  one author, so these figures are indicative rather than a benchmark; the
  measurement is published with the notation so that it can be repeated.

Conformance can be checked:
: The symbol set is closed, each line is recognisable in isolation, and the
  tree the lines produce is deterministic ({{parsing}}). A consumer can
  therefore verify mechanically that generated text conforms, and reject or
  repair what does not. Prose admits no equivalent check.

PMB structures reasoning; it does not validate it. A well-formed document can
be entirely wrong, and a symbol asserts only what its author claims. Documents
from untrusted sources carry further risks, which are described in
{{security}}.

## Relationship to Other PMB Documents

{{PMB}} is the canonical one-file description of the notation, written for
humans and for language models, and is the source of the semantics in
{{symbols}}. This document is authoritative for syntax, parsing, and
interoperability. Where the two disagree on a matter of parsing, this document
governs; the specific disagreements identified while writing it are listed in
{{settled}}.

The notation itself is dedicated to the public domain under CC0. The IETF Trust
boilerplate applies to this document as a document, not to the notation it
describes.

# Conventions and Definitions

{::boilerplate bcp14-tagged}

The following terms are used throughout:

Document:
: A sequence of lines, as defined in {{encoding}}.

Line:
: A sequence of characters terminated by an end-of-line sequence or by the end
  of the document.

Indent:
: The exact sequence of space (U+0020) and horizontal tab (U+0009) characters
  at the start of a line, up to but not including the first character that is
  neither. A line whose first character is neither has an empty indent.

Symbol:
: One of the six characters PLUS SIGN (U+002B), HYPHEN-MINUS (U+002D),
  EXCLAMATION MARK (U+0021), ASTERISK (U+002A), QUESTION MARK (U+003F), and
  TILDE (U+007E), when it appears as the first character after the indent and
  is followed by a valid symbol token terminator.

Symbol token:
: A symbol together with its optional modifier -- either a run of repeats or a
  weight. Defined in {{tokens}}.

Marked line:
: A line consisting of an indent, a symbol token, at least one space or tab,
  and text.

Unmarked line:
: A non-blank line that is not a marked line.

Blank line:
: A line containing nothing but its indent.

Node:
: An element of the parsed tree, produced by a marked line or by an unmarked
  line that is not a continuation.

Continuation:
: An unmarked line whose text belongs to the node above it rather than forming
  a node of its own. Defined in {{unmarked}}.

# Symbols {#symbols}

A symbol marks the semantic role of the line it begins. The six symbols and the
unmarked line are the complete set; implementations MUST NOT define additional
symbols and MUST NOT redefine these.

| Symbol | Name | Role |
|---|---|---|
| `+` | Pro | Supports. Benefit, advantage, evidence for. |
| `-` | Con | Opposes. Drawback, risk, evidence against. |
| `!` | Attention | Worth keeping in view. Can still give way. |
| `*` | Hard | Cannot give way. Rules, laws, contract terms, physical limits. |
| `?` | Question | A genuine unknown that needs resolving. |
| `~` | Flux | Unvalidated. Uncertainty not yet resolvable into `+`, `-`, or `!`. |
| (none) | Neutral | Fact, context, observation. No valence. |

The distinction between `!` and `*` is whether the thing can give way. A
deadline that could be renegotiated, a budget that could be stretched, or a risk
that could be mitigated is `!`. A regulation, a signed clause, or a physical
limit is `*`. The test is whether arguing could change it.

`*` differs from the other symbols in two syntactic respects: it does not
repeat and it takes no weight ({{tokens}}). A hard condition either holds or it
does not.

The unmarked line is a full member of the set, not an absence of markup. It
carries facts, context, and questions that reframe the discussion rather than
answer it.

# Syntax

## Encoding and Line Structure {#encoding}

A PMB document is a sequence of Unicode characters {{UNICODE}} encoded in UTF-8
{{RFC3629}}.

Lines are terminated by LF (U+000A) or by CRLF (U+000D U+000A). A parser MUST
accept both, MAY accept a lone CR (U+000D) as a terminator, and MUST treat the
final line of a document as terminated whether or not a terminator is present.

If a document begins with U+FEFF (BYTE ORDER MARK), a parser SHOULD remove it
before parsing. A parser that does not remove it MUST treat it as part of the
first line's text, which prevents the first line from being recognised as a
marked line.

A PMB document has no header, no version marker, no terminator, and no escape
mechanism. There is no way to escape a symbol; a line whose text must begin
with a symbol character is written as an unmarked line only by placing another
character first, which is a deliberate limitation ({{no-escape}}).

## Grammar {#grammar}

The following ABNF {{RFC5234}} defines the lexical form of a line. The
assignment of lines to nodes in a tree is defined in {{parsing}}, not by this
grammar.

~~~ abnf
pmb-document   = *( line eol ) [ line ]

line           = marked-line / unmarked-line / blank-line

marked-line    = indent symbol-token 1*wsp *text-char
unmarked-line  = indent 1*text-char
blank-line     = indent

indent         = *wsp
wsp            = SP / HTAB

symbol-token   = pro-token / con-token / attn-token
                 / query-token / flux-token / hard-token

pro-token      = 1*"+" / ( "+" weight )
con-token      = 1*"-" / ( "-" weight )
attn-token     = 1*"!" / ( "!" weight )
query-token    = 1*"?" / ( "?" weight )
flux-token     = 1*"~" / ( "~" weight )
hard-token     = "*"

weight         = zero-weight / one-weight
zero-weight    = "0" [ "." 1*DIGIT ]
one-weight     = "1" [ "." 1*"0" ]

text-char      = HTAB / %x20-10FFFF   ; any character except CR and LF

eol            = CRLF / LF
~~~

A line MUST be matched against `marked-line` first. A line that does not match
`marked-line` and is not a `blank-line` is an `unmarked-line`, whatever its
content. Every line matches exactly one production under this rule, so parsing
never fails at the lexical level.

The grammar admits a marked line with empty text (`- ` followed by nothing).
Such a line is a node with empty text. Generators SHOULD NOT emit one.

## Symbol Tokens {#tokens}

A symbol token is a symbol, optionally followed by a modifier, and MUST be
followed by at least one space or tab. The modifier is either a run of repeats
of the same symbol or a weight. It MUST NOT be both.

The symbol MUST be the first character of the line after the indent. A symbol
character elsewhere in a line is text: `2 + 2 = 4` is an unmarked line, and
`+ - possibly` is a pro whose text is `- possibly`.

The following are consequences of the grammar, stated explicitly because each
one is a case implementations have been observed to disagree on:

- A run MUST consist of repeats of the same symbol. `+- foo` is an unmarked
  line.
- `*` MUST NOT be repeated and MUST NOT take a weight. `** foo` and `*0.5 foo`
  are unmarked lines. This also avoids a collision with the Markdown emphasis
  delimiter `**`.
- A symbol token followed immediately by any character other than a space or
  tab does not form a symbol token, and the line is unmarked. `-5%` and
  `!!foo` are unmarked lines.
- A weight and a repeat run MUST NOT be combined. `!!0.9 foo` is an unmarked
  line.

### Intensity {#intensity}

A run of two or more repeats of the same symbol means "more so". A run of
length 1 carries no intensity; a run of length 2 is intensity 2; a run of
length 3 is intensity 3.

~~~
!  Worth watching
!! Worth watching closely
!!! Drop everything
~~~

Three is the maximum. A run of four or more repeats MUST be reported as
intensity 3. It is not an error and MUST NOT cause the line to be treated as
unmarked. Generators MUST NOT emit runs longer than three.

The cap exists because machine generators, unlike people, do not self-limit
when asked to signal urgency; a fixed ceiling also makes parsers deterministic.

### Weight {#weight}

A weight is a number in the closed interval \[0, 1\] written immediately after
the symbol, with no intervening space, and followed by at least one space or
tab. 0 means negligible; 1 means decisive.

~~~
+0.8 Cuts delivery time in half
-0.3 Marginally more expensive to run
!0.9 Contract renews automatically unless we act by the 30th
~~~

For `+` and `-` the symbol supplies the sign, so the token as a whole reads as
a signed weight in \[-1, 1\]. For `!`, `?`, and `~` the number is a magnitude
only. `*` takes no weight.

The grammar admits `0`, `1`, `0.` followed by one or more digits, and `1.`
followed by one or more zeros. It does not admit a leading decimal point, a
sign, or any value outside the interval. `+.5 foo`, `+1.5 foo`, and `-5%` are
therefore unmarked lines. Trailing zeros are permitted and are not significant:
`+1.00` and `+1` are the same weight.

An unweighted line is unweighted. A parser MUST NOT report a default weight for
it, and in particular MUST NOT report 0.5. See {{interpretation}}.

### Scope of a Weight {#weight-scope}

A weight applies to the line that carries it and to nothing else. It states how
much that line counts against the line it responds to -- its parent -- and, for
a line at the root, against the question the document is about. This is the
scoping the symbols already have: nesting means "this is about that", and a
weight is a statement about that relationship, not about the document as a
whole.

A stated weight is immutable. The weight a parser reports for a node MUST be
the one its author wrote, or absent. A consumer MUST NOT overwrite, adjust, or
supply it on the basis of that node's children, parent, or siblings.

Weights are not normalised: the weights of a set of siblings need not sum to 1,
need not sum to anything, and are not evidence about one another. Nor are
weights comparable across documents or across authors, and they are only
loosely comparable across branches of one document. A weight records one
author's judgment at one position in one tree.

The same scoping applies to intensity ({{intensity}}): a `!!` line beneath a
`!!!` line is a statement about itself, not a fraction of the line above.

### Aggregation over a Subtree {#aggregation}

The lines beneath a node bear on it. That is what nesting expresses, and a
consumer MAY therefore compute quantities over a subtree. Two constraints
apply.

First, any such quantity is derived. It MUST be labelled as derived, MUST NOT
be recorded as the weight of any node, and MUST NOT be presented as something
the document states.

Second, magnitudes may be combined and signs MUST NOT. The sign of a weight is
relative to the line it responds to, not to the question the document asks. In

~~~
- Needs 30 lakh upfront
  + We have 45 lakh saved
~~~

the `+` line is favourable with respect to the document's question, but it is
written as a rebuttal to a con and its sign is relative to that con. The
referent inverts at each level of nesting, so a consumer that sums signed
weights over a subtree computes a quantity whose terms do not share a referent.

Correcting for this would require the sign to alternate with depth, which
assumes every nesting relation is oppositional. PMB makes no such assumption:
any symbol may nest under any other ({{indentation}}), and four of the six
symbols -- `!`, `*`, `?`, and `~` -- carry no sign at all, as does the neutral
line. A `+0.8` with a `?0.9` beneath it is heavily contested, and the `?`
contributes nothing to a signed total.

A signed sum over a subtree is therefore undefined rather than merely
disfavoured. Magnitude aggregates are well defined -- how much weight of any
kind hangs beneath a node, how much of it is `?` or `~`, whether the subtree
contains a `*` -- and this specification permits them without naming any. A
consumer computing one should note that a single `*` in a subtree may settle
the question regardless of any total, per {{interpretation}}.

## Indentation and Depth {#indentation}

Depth is relative. A parser MUST determine depth by comparing indent strings
against an indent stack ({{parsing}}), and MUST NOT compute depth by dividing
an indent's length by a fixed unit.

Two indents are compared by removing their longest common prefix and comparing
the lengths of what remains:

- Indent B is *deeper* than indent A if, after removing the longest common
  prefix of A and B, what remains of B is longer than what remains of A.
- B is *shallower* than A if what remains of B is shorter.
- Otherwise A and B are at the *same depth*, which includes the case where
  they are identical.

Every character in an indent counts as one, and a horizontal tab counts the
same as a space. This specification defines no tab width. Tab width is a
property of how text is displayed rather than of the document, so any value
chosen here would cause two conforming parsers, configured differently, to
build different trees from identical bytes.

In a document that indents consistently -- any number of spaces per level, or
tabs throughout, so long as one unit is used -- the longest common prefix of a
line's indent and its parent's is the parent's indent itself, and the rule
reduces to "longer is deeper". Two spaces per level is the convention.

In a document that mixes units the rule still yields exactly one answer, but
that answer may not match what the author's editor displayed. A line indented
with one tab, following a line indented with two spaces, shares no common
prefix with it; one character remains against two, so the tab-indented line is
treated as shallower, though most editors draw it further right. The
comparison remains local: a mixed indent is placed relative to its neighbours
and never collapses the tree to the root. A parser SHOULD warn when a
document's indents use both tabs and spaces. Generators MUST NOT mix them.

Nesting means "this is about that". Any symbol MAY nest under any other. A con
under a pro is a limitation; a pro under a con is a mitigation; a `?` under a
`*` questions whether that condition is really fixed. A parser MUST NOT reject
or reorder any combination.

## Unmarked Lines: Continuations and Neutral Nodes {#unmarked}

An unmarked line is either a continuation of the node above it or a neutral
node of its own, decided by its indent alone:

- Deeper than the enclosing node: a continuation of that node.
- Equal to the enclosing node: a neutral node, sibling to it.
- Neither: unwound per {{parsing}}, then resolved by the same two rules.

~~~
+ Cuts delivery time in half
  measured over the last two quarters      <- continuation
+ Team has shipped this stack before
  - Only two of them are still here        <- child node
  Hiring is under way                      <- neutral sibling node
~~~

A node's text is the text of its own line followed by the text of each of its
continuations, in order, joined with a single space (U+0020). Leading indent is
removed from each continuation before joining; trailing whitespace SHOULD be
removed.

An implementation that needs to reproduce the original document MUST retain the
constituent lines separately as well; the joined form is lossy with respect to
the author's line breaks. This is a deliberate trade: continuations exist to
wrap a single thought that does not fit on one line, and joining with a space
is the form a consumer needs.

## Blank Lines

A blank line MUST NOT affect the indent stack. Blank lines do not close nodes,
do not terminate a continuation, and carry no meaning. An implementation that
reproduces the original document SHOULD preserve them.

Authors commonly use a blank line to separate dated blocks. Because such blocks
begin at the root indent, no node is closed by the blank line itself; the
change of indent closes it.

## Tags and Dates

A tag is an annotation carried inside the text of a line, in either of two
forms: a bracketed form, `[EXP]`, and a prefix form, `ref:`. Common tags are
`[OBSOLETE]`, `[EXP]` (a recurring pattern or hard-won lesson), `[UPDATE]`,
`[RESOLVED]`, and `[..]` (a placeholder). Tags are case-insensitive. A tag may
carry additional text: `[OBSOLETE 2026-03: compliance rules changed]`.

Tags are part of the text. A parser MAY extract them into a separate field, but
MUST NOT remove them from the reported text, and MUST NOT reject a tag it does
not recognise. A line consisting only of a tag is an ordinary line and is
subject to the rules in {{unmarked}}.

Dates SHOULD be written in the extended calendar-date format of {{ISO8601}}
(`YYYY-MM-DD`). Dates carry no syntactic significance; a date line is an
ordinary unmarked line.

# Parsing {#parsing}

## Data Model

A parsed document is an ordered tree of nodes. Each node has:

`symbol`:
: One of `+`, `-`, `!`, `*`, `?`, `~`, or absent for a neutral node.

`intensity`:
: An integer in \[2, 3\], present only if the author wrote a run of repeats.
  Absent otherwise.

`weight`:
: A number in \[0, 1\], present only if the author wrote one. Absent otherwise.

`text`:
: The text of the line, joined with its continuations per {{unmarked}}.

`children`:
: An ordered list of nodes.

`intensity` and `weight` MUST NOT both be present, since the grammar does not
admit both. Implementations SHOULD also record source line numbers and the raw
lines, which are required for round-tripping and for diagnostics.

## Algorithm

A conforming parser maintains a stack of open nodes, each recorded with the
indent string of the line that produced it. The stack is initialised with a
root node whose indent is the empty string. For each line, in order:

1. If the line is blank, do nothing.

2. Otherwise compute its indent and its lexical form per {{grammar}}, and let
   the *innermost node* be the node at the top of the stack.

3. If the line is unmarked and its indent is deeper than the innermost node's
   indent, per {{indentation}}, the line is a continuation of that node. Append
   its text and process no further; the stack is unchanged.

4. Otherwise unwind: while the top of the stack is not the root and the
   current line's indent is not deeper than the top's indent, pop the stack.
   The root is never popped, so the loop always terminates.

5. The top of the stack is now the parent. Create a node -- a marked node or,
   for an unmarked line, a neutral node -- append it to the parent's children,
   and push it onto the stack with the current line's indent.

Step 3 is evaluated before step 4, and the order matters. An unmarked line at
the same depth as the innermost node must become a neutral sibling of it, not
a continuation of its parent; testing for a continuation only after unwinding
would produce the latter.

The algorithm is total: every document produces a tree, and no input causes it
to fail.

## Robustness

A parser MUST NOT drop a line. A line that is not a valid marked line is an
unmarked line and retains its full original text, including any leading
character that resembles a symbol. This is what allows an extension, a typo, or
a future version of the notation to degrade to readable text rather than to
silence.

A parser MUST NOT normalise a document as a side effect of parsing: it must not
rewrite indentation, reorder siblings, merge nodes, or convert between
intensity and weight.

Documents are untrusted input. See {{security}} for limits a parser is expected
to impose.

# Interpretation {#interpretation}

The rules in this section apply to consumers of a parsed document, including
language-model tooling, and are what distinguish PMB from a bullet list.

Report what was written:
: A consumer MUST NOT report a weight that the author did not write. An
  unweighted line makes no claim about weight; it does not mean 0.5. Inventing
  a default fabricates a judgment the author declined to make.

Do not convert between the graded mechanisms:
: Intensity and weight are separate. `!!` is not 0.66 and 0.66 is not `!!`. A
  consumer MUST report whichever the author wrote and MUST leave the other
  absent. Any mapping between them would be invented, and a consumer that
  reports an invented number is worse than one that reports none.

Symbols are semantic, not evaluative:
: A consumer MUST NOT reach a verdict by counting `+` lines against `-` lines.
  The symbols mark what kind of claim a line makes, not how a decision comes
  out. A single `*` can settle a question that a dozen `+` lines do not.

Aggregate magnitudes, never signs:
: The lines beneath a node bear on it, and a consumer MAY compute quantities
  over a subtree. It MUST label them derived, MUST NOT record them as the
  weight of any node, and MUST NOT sum signed weights, whose terms do not
  share a referent ({{aggregation}}). A document does not reduce to a score,
  and a single `*` can settle a question that no total would.

Preserve superseded reasoning:
: PMB documents are written append-only: new dated blocks are added above old
  ones and the old ones are left intact, because the record of how the author
  actually reasoned is the point. A consumer that summarises a document SHOULD
  distinguish current reasoning from superseded reasoning by date rather than
  discarding the latter.

# Generating PMB {#generating}

Generators, and in particular language-model generators, are subject to
additional constraints:

- One thought per line. A generator SHOULD NOT emit a line that contains
  multiple independent claims.
- Emit `+`, `-`, and `!` by default. `*`, `?`, and `~` are for the cases the
  first three do not cover; marking every line is noise.
- Do not escalate. Intensity is capped at three ({{intensity}}), and a
  generator MUST NOT exceed it to signal urgency.
- Prefer a weight to a run of repeats when precision matters, and never emit
  both.
- Do not mix tabs and spaces ({{indentation}}).
- Reserve `*` for conditions that genuinely cannot give way. `*` is worth
  scanning for only if it is rare.

# Interoperability with Markdown and Other Carriers {#carriers}

Markdown {{RFC7763}} {{RFC7764}} treats `+`, `-`, and `*` at the start of a
line as interchangeable bullet markers and renders all three identically, which
destroys the distinction PMB depends on. `!` is significant in image syntax,
and `**` delimits emphasis.

Therefore, in any context where Markdown will be rendered, PMB MUST be placed
inside a fenced code block whose info string is `pmb`:

~~~~
```pmb
+ Renders as written
- Including this line
* And this one
```
~~~~

The info string `pmb` identifies the content as this notation. Consumers
SHOULD treat a fenced block tagged `pmb` as a PMB document and MAY treat one
tagged with a filename ending in `.pmb` the same way.

Bare PMB, with no fence, is correct in plain-text files, in source-code
comments, in commit messages, in terminal output, and on paper -- anywhere the
text will not be run through a Markdown renderer.

PMB inside another structured format inherits that format's escaping rules,
which PMB itself does not provide ({{no-escape}}). In YAML, a PMB document is a
literal block scalar; in JSON, a string with escaped line breaks; in HTML, the
content of a `pre` element with its characters escaped.

## The Absence of an Escape Mechanism {#no-escape}

PMB defines no escape character. A line of text that begins with `- ` cannot be
written as a neutral line; it is a con. This is a deliberate consequence of
the design goal that the notation be learnable without documentation: an escape
character is a rule that must be taught, and it would appear in documents far
more often than the case it exists to handle.

Applications that need to embed arbitrary text SHOULD do so at the carrier
level rather than proposing an escape mechanism.

# Security Considerations {#security}

## Resource Exhaustion

Parsing is linear in the size of the input, and the stack depth is bounded by
the nesting depth of the document. A hostile document can nonetheless present
very long lines, very deep nesting, or very long indents. A parser that
processes untrusted input SHOULD impose limits on input size, line length, and
nesting depth, and MUST fail predictably rather than exhausting memory when a
limit is reached.

## Symbol Spoofing

The six symbols are the ASCII code points listed in {{symbols}} and no others.
Unicode contains characters that render similarly or identically in common
fonts, including U+2212 MINUS SIGN, U+2010 HYPHEN, U+FF0B FULLWIDTH PLUS SIGN,
U+FF0A FULLWIDTH ASTERISK, U+2731 HEAVY ASTERISK, U+01C3 LATIN LETTER
RETROFLEX CLICK, and U+FF01 FULLWIDTH EXCLAMATION MARK.

A line beginning with such a character is an unmarked line under this
specification, but may appear to a human reader to be a marked one. The
converse risk also exists: a rendering that substitutes glyphs may make a
marked line appear unmarked.

This matters because the symbols carry authority. A line marked `*` asserts a
constraint that cannot be negotiated, and a reader -- especially an automated
one -- may treat it as settling a question. An attacker who can influence a
document can therefore attempt to forge a hard condition, or to disguise one so
that it is not counted.

Implementations that display PMB SHOULD make marked and unmarked lines
visually distinguishable by means other than the leading character itself, for
example by styling recognised symbol tokens. Implementations that parse
untrusted input SHOULD report the presence of confusable leading characters
rather than silently treating the line as text.

## Untrusted Documents as Input to Automated Consumers

PMB is a format whose purpose is to tell a reader how much weight to give a
claim. When a language model or other automated system consumes a PMB document
from an untrusted source, the symbols, intensities, and weights in that
document are assertions by its author, not facts, and they are attacker-
controlled if the author is an attacker. A `*` line in untrusted input MUST NOT
be treated as a constraint on the consuming system's own behaviour, and a
weight of 1 in untrusted input asserts only that the author wrote 1.

Consumers SHOULD keep the provenance of a document alongside its parsed
content, and SHOULD NOT merge trusted and untrusted PMB into a single tree
without recording which nodes came from where.

## Retention of Superseded Content

PMB documents are append-only by convention: reasoning that turned out to be
wrong is retained rather than deleted, and this is a feature of the notation
rather than an oversight. Consequently a PMB document is likely to contain
statements the author no longer holds, along with dates that reveal when the
author held them. Applications that publish, share, or index PMB documents
SHOULD account for this, and SHOULD NOT assume that removing a claim from
current reasoning removes it from the document.

The notation offers no confidentiality, integrity, or authenticity mechanism.
Where any of these is required, it must be provided by the carrier or the
transport.

# IANA Considerations

This document has no IANA actions.

In particular, no media type is registered for PMB. A media type would be
warranted if PMB were transferred as a stand-alone entity over a protocol that
dispatches on media type. In current practice PMB is carried inside other
formats -- Markdown documents, source files, and message bodies -- where it is
identified by the fenced-block info string `pmb` described in {{carriers}}, and
a registration would add a dispatch mechanism that nothing dispatches on.

Should that change, the appropriate action is a registration of `text/pmb` in
the standards tree or vendor tree under the procedures of {{RFC6838}}, with
UTF-8 as the required charset, no other parameters, and `.pmb` as the file
extension.

--- back

# Complete Example

The following document exercises every construct in this specification: all six
symbols, a neutral line, nesting, a continuation, a blank line, dated blocks in
reverse-chronological order, and a tag.

~~~
Open the second location? [2026-03-04]
+ Current place runs at 95% capacity
+ 40-odd people on the waitlist every week
- Needs 30 lakh upfront
  + We have 45 lakh saved
  !! Want to keep six months of runway
     which at current burn is just under 11 lakh
    ? Can we phase the payments
* Lease is three years, no exit clause
* FSSAI licence must be issued before we can trade a single day
-0.4 Splits my attention
  ! Already at 70-hour weeks

[2026-03-18]
! Landlord won't phase anything
? Is there a smaller unit on the same street
  [EXP: same trap in 2022 -- committed before systems were ready]
Decision: hold three months, look for something smaller.
~~~

`!` marks what deserves attention and could still move: the runway, the hours,
the landlord. `*` marks what will not move whatever anyone decides. The line
beginning `which at current burn` is a continuation of the `!!` line above it
and does not create a node. The `[EXP: ...]` line is a neutral child of the `?`
line above it, and its tag is part of its text.

# Test Vectors

Each row is a single line presented to a parser at the root indent. "Unmarked"
means the line produces a neutral node or a continuation per {{unmarked}}, with
the text shown being the entire line.

| Input | Symbol | Intensity | Weight | Text |
|---|---|---|---|---|
| `+ Cuts cost 30%` | `+` | -- | -- | `Cuts cost 30%` |
| `- 5% is acceptable` | `-` | -- | -- | `5% is acceptable` |
| `-5%` | (unmarked) | -- | -- | `-5%` |
| `-0.5 Leaves no buffer` | `-` | -- | 0.5 | `Leaves no buffer` |
| `-0.5% drop in margin` | (unmarked) | -- | -- | `-0.5% drop in margin` |
| `+0 Negligible either way` | `+` | -- | 0 | `Negligible either way` |
| `+1 Decisive` | `+` | -- | 1 | `Decisive` |
| `+1.00 Decisive` | `+` | -- | 1 | `Decisive` |
| `+1.5 Out of range` | (unmarked) | -- | -- | `+1.5 Out of range` |
| `+.5 No leading zero` | (unmarked) | -- | -- | `+.5 No leading zero` |
| `!! Worth watching closely` | `!` | 2 | -- | `Worth watching closely` |
| `!!! Drop everything` | `!` | 3 | -- | `Drop everything` |
| `!!!! Still three` | `!` | 3 | -- | `Still three` |
| `!!foo` | (unmarked) | -- | -- | `!!foo` |
| `!!0.9 Both mechanisms` | (unmarked) | -- | -- | `!!0.9 Both mechanisms` |
| `!0.9 Contract renews` | `!` | -- | 0.9 | `Contract renews` |
| `* GDPR requires consent` | `*` | -- | -- | `GDPR requires consent` |
| `** Not emphasis` | (unmarked) | -- | -- | `** Not emphasis` |
| `*0.9 No weight on hard` | (unmarked) | -- | -- | `*0.9 No weight on hard` |
| `+- Mixed run` | (unmarked) | -- | -- | `+- Mixed run` |
| `+ - possibly` | `+` | -- | -- | `- possibly` |
| `2 + 2 = 4` | (unmarked) | -- | -- | `2 + 2 = 4` |
| `~ Might be wrong` | `~` | -- | -- | `Might be wrong` |
| `?? Really unclear` | `?` | 2 | -- | `Really unclear` |
| `- ` | `-` | -- | -- | (empty) |
| `-` | (unmarked) | -- | -- | `-` |
| `− Unicode minus` | (unmarked) | -- | -- | `− Unicode minus` |

Structural vectors, each given as a complete document. Within them, `<TAB>`
stands for a single horizontal tab and `·` for a single space; both are
written visibly because the distinction is the point.

~~~
+ a
  b
~~~

: One node, symbol `+`, text `a b`. `b` is a continuation.

~~~
+ a
  - b
  c
~~~

: `+ a` with two children: `- b`, and a neutral node `c`. `c` is not a
  continuation of `a`, because its indent equals that of `b`.

~~~
+ a

  b
~~~

: One node, symbol `+`, text `a b`. The blank line has no effect.

~~~
  + a
+ b
~~~

: Two root-level siblings. Depth is relative, so the first line's indent does
  not make it a child of anything.

~~~
+ a
<TAB>+ b
~~~

: `+ b` is a child of `+ a`. The common prefix is empty; nothing remains of
  `a`'s indent and one character remains of `b`'s, so `b` is deeper.

~~~
+ a
··+ b
<TAB>+ c
~~~

: `+ c` is a child of `+ a` and a sibling of `+ b`. The common prefix of `··`
  and `<TAB>` is empty, leaving two characters against one, so `+ c` is
  shallower than `+ b` and unwinds one level. This is the mixed-indent case:
  the result is deterministic and local, but it is not what an editor drawing
  a tab as four columns would suggest. Do not mix units.

# Reference Regular Expression

This appendix is informative. The following expression, in a dialect supporting
backreferences, recognises a marked line as defined in {{grammar}}:

~~~
^([ \t]*)(?:(\*)|([+\-!?~])(\3*|0(?:\.\d+)?|1(?:\.0+)?))[ \t]+(.*)$
~~~

Capture 1 is the indent; capture 2 is `*` if the line is a hard condition;
capture 3 is the symbol otherwise; capture 4 is the modifier -- an empty
string, a run of additional repeats, or a weight; capture 5 is the text.
Intensity is one plus the length of capture 4 when capture 4 is a run of
repeats, clamped to 3.

The expression is a recogniser only. Depth, continuations, and the tree must be
computed by the algorithm in {{parsing}}; in particular, an implementation MUST
NOT derive depth by dividing the length of capture 1 by two.

This expression corrects the one published in {{PMB}} v1.2 in three respects:
it excludes `*` from repeats and weights, it accepts runs of four or more
repeats so that they can be clamped to 3 rather than falling through to text,
and it excludes the combination of a run and a weight. {{PMB}} published a
regular expression of its own through v1.2; from v1.2.1 it carries none and
defers to this document.

# Points Settled by This Document {#settled}

This appendix is informative and is expected to be removed before publication.
It records the questions that {{PMB}} v1.2 and {{PMB-DECISIONS}} left open or
answered inconsistently, and the disposition taken here.

Items 1 through 6 change what a parser does with a document that exists today,
and are reflected in {{PMB}} v1.2.1, whose reasoning {{PMB-DECISIONS}} records
as an amendment to D4 and as D5 and D6. From v1.2.1 that document no longer
carries a regular expression or a parsing algorithm of its own; it states the
notation and defers here for the interchange format. Items 7 through 12 are
interchange-level detail that a one-file specification deliberately omits, and
are settled here only.

Contradictions resolved:

1. Runs of four or more repeats. The prose states that a fourth repeat "just
   reads as three"; the published regular expression does not match such a
   line at all, making it text. Settled in favour of the prose:
   intensity clamps to 3 ({{intensity}}).
2. A run combined with a weight. {{PMB}} states "not both"; {{PMB-DECISIONS}}
   D4 states that `!!0.9` is "not forbidden, just pick one". Settled as not
   admitted by the grammar; such a line is unmarked ({{tokens}}).
3. Repeats and weights on `*`. The prose forbids both; the published regular
   expression permits both. Settled in favour of the prose ({{tokens}}).

Questions the prose documents did not address:

4. Comparison of mixed tab and space indentation, which no prose document
   defines. Settled as comparison of what remains after removing the two
   indents' longest common prefix, so that no tab width is ever needed and a
   mixed indent is still placed relative to its neighbours ({{indentation}}).
5. Whether a blank line closes a node or terminates a continuation. Settled as
   structurally insignificant.
6. How a continuation joins its parent's text. Settled as a single space, with
   the raw lines retained for round-tripping ({{unmarked}}).
7. A symbol token followed by whitespace and nothing else. Settled as a legal
   node with empty text, so that trailing whitespace cannot change a line's
   type ({{grammar}}).
8. Character encoding, line terminators, and a leading byte order mark, none of
   which the prose documents mention ({{encoding}}).
9. Whether Unicode characters that resemble the symbols are symbols. Settled as
   no, with the consequences recorded in {{security}}.
10. The exact numeric forms a weight admits -- leading zero required, trailing
    zeros insignificant, no sign, no value outside \[0, 1\] ({{weight}}).
11. Whether a parser may extract tags from text. Settled as yes, provided the
    text is not modified.
12. That PMB has no escape mechanism, and that this is deliberate rather than
    an omission ({{no-escape}}).

# Acknowledgements
{:numbered="false"}

The design decisions this document formalises, including the arguments that
lost, are recorded in {{PMB-DECISIONS}}.
