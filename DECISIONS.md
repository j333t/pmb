# PMB Design Decisions

Settled questions about the notation, reasoned in the notation.

**As of 2026-08-09 the symbol set is closed.** D3 was the last open question
about membership. Grammar, tags and tooling can still move; the six symbols
and the neutral line cannot.

The goal is a core symbol set where no further improvement is possible — a set
understood everywhere, by default, without explanation. Once it reaches that
point it should never change again. This file is how we get there and how we
prove, later, why each symbol is what it is.

Nothing here is deleted. Losing arguments stay on the page.

For the case for each symbol individually, argued in the notation, see
[AUTOLOGY.md](AUTOLOGY.md).

---

## D1 — What does ` * ` mean?

**CLOSED 2026-08-09 · ` * ` is a hard condition**

### Decision

```pmb
`*` — hard conditions. Rules, laws, regulations, contractual terms.
      Things that cannot give way.
`!` — attention. Note this, keep it in view. Not immovable.

The test between them: can it give way?
  No  -> `*`
  Yes -> `!`
```

### Why

```pmb
! The criterion is universality: a symbol must be understood everywhere,
  by default, with no explanation. Nothing else outranks this.
+ "*terms and conditions apply" is read correctly by everyone, everywhere
  + Arguably a stronger prior than +/- for pro and con
  + A symbol that borrows an existing reflex costs nothing to teach,
    which is the highest-value property a symbol can have
+ Re-scoping `!` to attention removes the overlap that blocked this
  Before: `!` claimed "deal-breakers, constraints, non-negotiables" —
  the same sentence as the new `*`. That language now belongs to `*` alone.
  + So CONTRIBUTING.md's rule against overlapping symbols is satisfied
+ The split is a kind, not a degree, which is how every other symbol works
  + And it has a real test — negotiable or not — so there's no hesitation
    at the moment of writing
```

### What this cost

Kept on the record, because it was the strongest argument on the other side.

```pmb
- `*` previously meant Insight: a reframe, an "I'm asking the wrong
  question" moment
  - That has no other home in the notation
    + `+` and `-` take a side. `?` and `~` mark gaps. `!` flags attention.
      A reframe dissolves the line above it rather than answering it.
  - It carried the "clarify while writing" property, which is the value
    that pays off on day one, before any archive exists
- The recommendation going in was to keep Insight and give hard conditions
  to `!` plus a [legal] tag
  - Overruled, correctly: a tag is slower to write than a symbol, and
    SOPs need this often enough that the speed matters
  ~ Whether reframes needed their own symbol at all is now D3
! Watch for: reasoning notes that feel flatter than before.
  If reframes stop getting written down because they have nowhere to go,
  that's the cost showing up, and it's worth reopening.
```

### The argument that was rejected

```pmb
~ Earlier framing: `*` is "a stronger !"
- Every other symbol marks a kind, not a degree
  - A severity ladder for exactly one symbol is a pattern PMB doesn't have
  - "Critical" vs "more critical" has no test, so it costs hesitation
    at write time, and hesitation is what PMB cannot afford
+ Resolved by reframing it as a kind — negotiable vs not — rather than
  a degree. The decision above stands on that, not on strength.
If degree is ever wanted, it belongs to every symbol at once. See D2.
```

---

## D2 — Should repeated symbols mean intensity?

**CLOSED 2026-08-09 · yes, up to three**

### Decision

```pmb
`!` `!!` `!!!` — repeat a symbol to mean "more so". Same for + - ? ~
Three is the maximum. A fourth repeat is not an error; it just reads
as three.

* `*` does not repeat. A hard condition either holds or it doesn't.
```

### Why

```pmb
+ Already how people write emphasis, in every language and format
  + So it passes the universality test on its own
+ Gives a degree axis to every symbol for one line of grammar,
  instead of spending a whole symbol on "stronger !"
+ Degrades safely — a parser that ignores it reads `!!` as `!` plus text
+ Costs nothing to learn. Nobody needs to be told what `!!` means.
- Adds a judgment call at write time
  + But an optional one. Nobody has to reach for it.

? Why cap it, when people self-limit anyway
  + Humans do self-limit. Ten exclamation marks is obviously unreadable
    and nobody needs a rule to avoid it.
  ! Machines do not self-limit. Without a cap, a model asked to signal
    urgency will escalate, and nothing stops it.
  + Three maps cleanly onto low / medium / high, which is as much
    resolution as an ordinal scale can carry honestly
  + And a fixed ceiling makes parsers deterministic
```

### Grammar note

```pmb
! This amends the rule that a symbol must be followed by a space.
  The repeated run is one token: symbol, repeats, then the space.
  `!! foo` is now legal. `!!foo` is still text.
```

---

## D3 — Does a reframe need its own symbol?

**CLOSED 2026-08-09 · no. The slot stays empty.**

### Decision

```pmb
There is no symbol for a reframe. The set is six symbols and an absence.

A reframe is written as a neutral line —
  "The competition isn't Company X, it's the status quo"
or as `?` when it is really a better question —
  "? Are we solving the wrong problem"
```

### Why

```pmb
* D1's criterion decides it: a symbol must be understood everywhere,
  by default, with no explanation.
  - No glyph is universally read as "realisation" or "aha". None exists.
    + Every surviving symbol has such a reading — + and - arithmetic,
      ! warning, * fine print, ? question, ~ approximately.
      Insight never had one. That is why it always felt arbitrary.
  So the slot stays empty — not because reframes don't matter, but
  because nothing qualifies to hold them.
+ Reframes already have a home, and it is structural, not a symbol
  ! A reframe does not respond to the line above it. It replaces the
    question at the top.
    + So it belongs at root, as the next dated question — not as a
      marked node underneath the reasoning it just dissolved
    + Which is what people already do on paper when the frame breaks
  + Read that way, this is the notation working, not a gap in it
+ Six symbols that are all universal beats seven where one needs
  explaining. That is the convergence D1's criterion aims at.
```

### What this cost

```pmb
- The reframe stops being visually findable
  ! Often the highest-value line in a document, now unmarked
    ~ Acceptable. Rare things can be read for, and a reframe that opens
      a new dated block is findable by position instead.
? A `[insight]` or `[aha]` meta tag was the alternative
  + Uses machinery that already exists
  - Slower to write than a symbol — the objection that beat tags in D1
  ~ Not forbidden. Anyone can write it. It just isn't the notation.
! Watch for: reasoning notes that feel flatter than before.
  If reframes stop being written down because they have nowhere to go,
  that is the cost showing up. D1 already flagged the same signal.
```

### What closing this settles

```pmb
* Membership is now decided. D3 was the last open question about which
  symbols are in the set, so the set is frozen: + - ! * ? ~ and neutral.
  ! Grammar, tags and tooling can still move. The symbols cannot.
  + Frozen with the arguments attached, so anyone reopening a symbol has
    to answer what is already on this page.
```

---

## D4 — Weights

**CLOSED 2026-08-09 · promoted from "Future Features" in SPEC.md**

### Decision

```pmb
A number immediately after the symbol, before the space, is that line's
weight — how much it should count, from 0 (negligible) to 1 (decisive).

+0.8 Cuts delivery time by half
-0.3 Slightly more expensive to run
!0.9 Contract renews automatically unless we act

For + and -, the symbol carries the sign, so the whole token reads as a
signed weight between -1 and 1. For ! ? ~ the number is magnitude only.

* `*` takes no weight. A hard condition is binary by definition —
  which is a useful check that D1 drew the line in the right place.
```

### Why

```pmb
+ Mostly for machines, and that is fine
  ! A model reading PMB currently knows the direction of every claim
    but nothing about magnitude. It has to infer importance from
    wording, which is exactly the inference PMB exists to remove.
  + Ranking, thresholds and aggregation all become possible without
    the model guessing
- Humans will rarely write these, and shouldn't be pushed to
  + Which is fine. Unweighted stays the default and means nothing
    is claimed about weight.
! Do not treat an unweighted line as 0.5. Absent is absent, not middling.
  A parser that invents a default silently fabricates a judgment
  the author declined to make.
```

### The collision this creates, and how it is resolved

```pmb
! Weights conflict with the rule that a symbol must be followed by a space.
  "- 5%" is a con. "-5%" is text. But a weight needs "-0.5 text".
+ Resolved by making the weight part of the symbol token, and requiring
  the space after the number instead
  "-0.5 Leaves no buffer"  -> con, weight -0.5
  "-0.5% drop in margin"   -> text. No space after the number.
  "-5%"                    -> text. 5 is outside the 0..1 range.
  "- 5% is acceptable"     -> con, no weight
  + Fully deterministic. No case reads two ways.
```

### Two mechanisms for one axis

```pmb
~ Repetition (D2) and weights (D4) both express intensity.
  Two mechanisms for one concept is normally a smell.
+ Defensible here because they sit at different resolutions and serve
  different readers
  + Repetition is ordinal, instant to write, and for people
  + Weights are continuous, precise, and for machines
! Do not define a conversion between them.
  `!!` is not 0.66. Any mapping would be invented, and a parser that
  reports a made-up number is worse than one that reports none.
  + Expose whichever the author actually wrote, and nothing else
- They can be combined — `!!0.9` — but shouldn't be
  ~ Not forbidden. Just pick one.
```

### Scope — added 2026-08-09

What a weight is measured against was never stated. Now it is.

```pmb
A weight applies to its own line, measured against the line it responds to.
At root, that is the question the document is about.

- A stated weight is immutable. Nothing computed later may overwrite it.
- Siblings are not normalised. They need not sum to 1, or to anything.
- Not comparable across documents or authors.

+ Same scoping the symbols already have — nesting means "this is about that",
  and a weight just says how much
  + So there is nothing new to learn
? Whether the lines beneath a node roll up into it — see D6
```

### Amendment 2026-08-09 — combining is forbidden, not discouraged

```pmb
`!!0.9 x` is text. A weighted line carries exactly one symbol.
- Reverses the last line above, which left combining legal
+ Writing the Internet-Draft made it unavoidable: a grammar cannot
  say "legal but don't"
  ! Left as advice, two conforming parsers disagree on identical bytes.
    That is the one thing a grammar exists to stop.
  ! And pmb.md already said "not both" in the same week this said
    "not forbidden". One of them had to go.
+ Nothing is lost. Each mechanism covers its whole range alone.
```

---

## D5 — How are two indents compared?

**CLOSED 2026-08-09 · drop the longest common prefix, compare what remains**

### Decision

```pmb
To compare indent A with indent B: remove the longest prefix they share,
then compare the lengths of what is left.
  Longer  -> deeper
  Shorter -> shallower
  Equal   -> same depth

Every character counts as one. A tab counts the same as a space.
No tab width is defined.
```

### Why

```pmb
? Depth is relative — but relative to what, when one line is indented
  with two spaces and the next with a tab
  ! No PMB document had ever said. Every parser was guessing.
- The obvious rule — expand tabs to N columns, then count — needs an N
  * There is no correct N. Tab width is a display setting, not a
    property of the document.
    ! So two parsers configured differently would build different trees
      from identical bytes. That is precisely what a grammar exists
      to prevent.
+ Dropping the shared prefix needs no constant at all
  + For any consistently indented document it reduces to
    "longer is deeper" — what everyone already assumes
  + And it states in one sentence, which matters for a spec that most
    people will read exactly once
- A mixed document can nest against what the editor draws
  A tab following two spaces reads as shallower, though it looks deeper
  + The misplacement stays local — one level off, still beside its
    neighbours. The tree does not collapse.
    ~ An earlier draft of the RFC unwound mixed indents all the way to
      the root. Equally deterministic, far worse failure. Dropped.
  + Parsers should warn on mixed indents, which turns a silent misparse
    into a visible one
  + "Don't mix tabs and spaces" is advice every text format already gives
```

---

## D6 — Do the weights beneath a node compose into it?

**CLOSED 2026-08-09 · magnitude composes, sign does not. Permitted, not defined.**

### Decision

```pmb
The lines beneath a node bear on it. That is what nesting is for, so
aggregating over a subtree is allowed.

- A stated weight is immutable. Anything computed is labelled derived and
  never written back into a weight the author wrote.
* Magnitudes may be combined. Signs may not.
- PMB does not name which aggregates a tool should compute.
```

### Why sign does not compose

```pmb
! A child's sign is relative to its parent, not to the question at root
  "+ We have 45 lakh saved" sits under "- Needs 30 lakh upfront"
  Relative to the decision, savings are favourable
  Relative to its parent, it is a rebuttal of a con
  ! So the referent inverts at every level down
    * A signed sum is then adding terms that don't share a referent
- Fixing it needs the sign to alternate with depth, minimax style
  ! Which assumes every nesting is oppositional
    * PMB denies that outright — any symbol may nest under any other
- And four of the six symbols carry no sign at all
  `! * ? ~` and the neutral line have nothing to give a signed total
  ! A `+0.8` with a `?0.9` under it is heavily contested, and the `?`
    contributes zero to any sum
* So a signed sum is undefined, not merely distasteful.
  That distinction is the whole finding.
```

### What does compose

```pmb
+ Magnitude, sign ignored — how much weight of any kind hangs beneath a node
  + Well defined for all six symbols and the neutral line
  + Answers the question that actually matters: how contested is this line
    A bare `+0.8` and a `+0.8` carrying three heavy children are not
    the same state, and nothing in the notation said so before
+ Unresolved weight — how much `?` and `~` sits in the subtree
+ Hardness — does the subtree contain a `*`
  * Binary, and it outranks any total
```

### Why permit rather than define

```pmb
? Should the spec name contested / unresolved / hard as standard quantities
- No. No tool has asked for them yet.
  ! Naming them is spec growth ahead of demand — the exact failure mode
    CONTRIBUTING.md exists to prevent
  + Permitting costs one rule — label what you derived — and leaves tools free
  ~ If two tools ship and disagree on the same document, that is the signal
    to come back and name them. Not before.
* The rule that holds either way: a derived number never overwrites a
  stated one.
```

### What this corrects

```pmb
[UPDATE 2026-08-09] An earlier ruling the same day said weights do not
compose at all, and banned aggregation outright.
- Over-reached. It banned two different things as if they were one.
  + Derivation — recomputing a parent's weight from its children —
    stays banned, and that part was right
  - Bearing — the children telling you how the parent is holding up —
    is what nesting is for. Banning it made nesting decorative.
! Kept on the record because the corrected rule is narrower than the
  first one, and anyone reopening this should see both.
```

---

## Closed

- **D1** — ` * ` is a hard condition; ` ! ` is attention · 2026-08-09
- **D2** — repeated symbols mean intensity, capped at three · 2026-08-09
- **D3** — reframes get no symbol; the slot stays empty · 2026-08-09
- **D4** — weights: a number after the symbol, 0 to 1 · 2026-08-09
  - amended 2026-08-09: `!!0.9` is text; weights take one symbol
- **D5** — indents compare by longest common prefix · 2026-08-09
- **D6** — subtrees aggregate by magnitude, never by sign · 2026-08-09
