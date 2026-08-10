# PlusMinusBang (PMB) v1.2.1

A notation for structuring reasoning in plain text. A symbol at the start of a
line marks what kind of thought it is. Indentation marks what it responds to.

Public domain (CC0). Canonical: https://plusminusbang.com/pmb.md

## Symbols

| Sym | Name | Means |
|-----|------|-------|
| `+` | Pro | Benefit, advantage, evidence for. |
| `-` | Con | Drawback, risk, evidence against. |
| `!` | Attention | Worth keeping in view — but it can give way. |
| `*` | Hard | Cannot give way. Rules, laws, contract terms, physical limits. |
| `?` | Question | Genuine unknown. Needs research — not a soft opinion. |
| `~` | Flux | Unvalidated. Uncertainty you can't yet resolve into `+ - !`. |
| none | Neutral | Fact, context, observation. No valence. |

`+ - !` cover about 90% of use. Start there.

**`!` or `*`?** Can it give way? A deadline, a budget, a worry you should hold
in mind — `!`. A regulation, a signed clause, a licence you cannot trade
without — `*`. If arguing could change it, it's `!`.

## Intensity and weight

Both optional. Skip this on first read — `+ - !` and indentation are the whole
notation.

**Repeat a symbol** to mean "more so", up to three. A fourth just reads as three.

```pmb
! Worth watching
!! Worth watching closely
!!! Drop everything
```

**Or write a weight** — 0 to 1, straight after the symbol, for how much the
line counts.

```pmb
+0.8 Cuts delivery time in half
-0.3 Marginally more expensive to run
!0.9 Contract renews automatically unless we act by the 30th
```

`+` and `-` supply the sign, so the token reads as −1 to 1. For `! ? ~` it's
magnitude only. **`*` takes no weight and never repeats** — a hard condition
holds or it doesn't. Use one mechanism or the other, never both: `!0.9 x` is
weighted, `!!0.9 x` is text.

A weight is about its own line, measured against the line it responds to, and
nothing computed later overwrites it. Mainly for machines — most people never
write one, and an unweighted line claims nothing about weight. **It does not
mean 0.5.**

## Grammar

- One thought per line: symbol, space, text.
- The symbol must be the line's **first non-whitespace character**, and the
  token must be followed by **at least one space**.
  `-5%` is text; `- 5%` is a con; `-0.5 tight` is a con weighted −0.5;
  `-0.5% margin` is text, because no space follows the number.
  Mid-line symbols are text: `2 + 2` parses as neutral.
- Indent to respond to the line above. Any symbol may nest under any other.
- Nesting means "this is about that": a con under a pro is a limitation, a pro
  under a con a mitigation, a `?` under a `*` asks whether that condition really
  is fixed.
- Deeper indent with no symbol continues the line above, joining it with a
  single space. Same indent with no symbol is a neutral node. Blank lines carry
  no meaning and never close a node.
- Depth is relative. Two spaces is the convention; any consistent unit works,
  tabs included. Don't mix units — a mixed document still parses, but not always
  the way your editor draws it.
- `[TAG]` or `tag:` annotates out of band: `[OBSOLETE]`, `[EXP]` (a recurring
  pattern or hard-won lesson), `[UPDATE]`, `[RESOLVED]`, `[..]` (placeholder).
- Dates in ISO 8601 (`YYYY-MM-DD`). Case-insensitive. No header, no terminator.

## Time

Append, don't delete. Old reasoning is the record of how you actually thought.
Date decision points, add new dated blocks above old ones, leave the old intact.
Being visibly wrong on the record is the point, not a defect — it is the only
way to find out which of your reasoning patterns keep failing.

## Example

```pmb
Open the second location? [2026-03-04]
+ Current place runs at 95% capacity
+ 40-odd people on the waitlist every week
- Needs ₹30L upfront
  + We have ₹45L saved
  ! Want to keep six months of runway
    ? Can we phase the payments
* Lease is three years, no exit clause
* FSSAI licence must be issued before we can trade a single day
- Splits my attention
  ! Already at 70-hour weeks

[2026-03-18]
! Landlord won't phase anything
? Is there a smaller unit on the same street
Decision: hold three months, look for something smaller.
```

`!` marks what deserves attention and could still move — runway, hours, the
landlord. `*` marks what will not move no matter what anyone decides.

## For machines

- **Emit PMB inside a fenced block tagged `pmb`.** Markdown renders `+`, `-` and
  `*` as identical bullets, erasing the distinction. Bare PMB is correct
  anywhere Markdown isn't rendered — plain text, code comments, paper.
- **Report what was written.** `!!` is not `0.66`; give `intensity: 2` or
  `weight: 0.9` and leave the other absent. Unweighted is unweighted, not `0.5`.
  Never overwrite a stated weight from a node's children, parent or siblings,
  and never normalise siblings to sum to 1. Inventing any of it fabricates a
  judgment the author declined to make.
- **Aggregate magnitudes, never signs.** The lines under a node bear on it, so
  totalling the weight beneath one is fair — as a *derived* value that never
  replaces a stated one. But a child's sign is relative to its parent, not to
  the question: `+ We have 45 lakh saved` under `- Needs 30 lakh upfront` is
  favourable to the decision while rebutting the con. The referent inverts each
  level down, and `! * ? ~` carry no sign at all, so a signed sum is undefined.
- Preserve unrecognised leading symbols as text rather than dropping the line.
- Symbols are semantic, not evaluative. Don't count `+` against `-` to reach a
  verdict. A single `*` can end a decision on its own.
- When emitting, never escalate past `!!!`, and prefer a weight when precision
  matters.

Writing a parser? The ABNF grammar, the tree-building algorithm, indent
comparison, test vectors and a reference regular expression are in the
[Internet-Draft](RFC/draft-shah-plusminusbang-00.md). This file is the notation;
that one is the interchange format.

## Rules of thumb

- Be specific. "Cuts cost 30% ($45k/yr)" beats "saves money".
- Deal-breakers at the top. Readers scan down and stop.
- Don't use every symbol every time. Over-symbolising is noise.
- Four levels of nesting usually means you are looping, not reasoning.
- Label what you don't know (`?` `~` `!`) instead of inventing a reason for it.

**The goal isn't perfect notation — it's better thinking. If a symbol doesn't
help, don't use it.**
