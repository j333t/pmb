# PlusMinusBang (PMB) v1.2

A notation for structuring reasoning in plain text. A symbol at the start of a
line marks what kind of thought it is. Indentation marks what it responds to.

Public domain (CC0). Canonical: https://plusminusbang.com/pmb.md

## Symbols

| Sym | Name | Means |
|-----|------|-------|
| `+` | Pro | Supports. Benefit, advantage, evidence for. |
| `-` | Con | Opposes. Drawback, risk, evidence against. |
| `!` | Attention | Note this. Worth keeping in view — but it can give way. |
| `*` | Hard | Cannot give way. Rules, laws, regulations, contract terms, physical limits. |
| `?` | Question | Genuine unknown. Needs research — not a soft opinion. |
| `~` | Flux | Unvalidated. Uncertainty you cannot yet resolve into `+ - !`. |
| none | Neutral | Fact, context, observation. No valence. |

`+ - !` cover about 90% of use. Start there.

**`!` or `*`?** Ask whether it can give way. A deadline you could negotiate, a
budget you could stretch, a worry you should hold in mind — `!`. A regulation, a
signed clause, a licence you cannot trade without — `*`. If arguing would change
it, it's `!`.

## Intensity and weight

Both are optional. Skip this section on first read — `+ - !` and indentation
are the whole notation.

**Repeat a symbol** to mean "more so", up to three:

```pmb
! Worth watching
!! Worth watching closely
!!! Drop everything
```

Three is the maximum. A fourth repeat just reads as three. `*` does not
repeat — a hard condition either holds or it doesn't.

**Or write a weight** — a number from 0 to 1 immediately after the symbol,
meaning how much this line should count:

```pmb
+0.8 Cuts delivery time in half
-0.3 Marginally more expensive to run
!0.9 Contract renews automatically unless we act by the 30th
```

For `+` and `-` the symbol supplies the sign, so the token reads as a signed
weight between −1 and 1. For `! ? ~` the number is magnitude only. `*` takes no
weight.

Weights exist mainly for machines. Most people will never write one, and an
unweighted line claims nothing about weight — **it does not mean 0.5.** Use one
mechanism or the other, not both.

## Grammar

- One thought per line: symbol, space, text.
- The symbol must be the **first non-whitespace character** of the line, and the
  symbol token must be followed by **at least one space**. The token is the
  symbol, plus up to two repeats, or a weight — not both.
  `-5%` is text; `- 5%` is a con; `-0.5 tight` is a con weighted −0.5;
  `-0.5% margin` is text, because no space follows the number.
  Symbols appearing mid-line are text: `2 + 2` parses as neutral.
- Indent to respond to the line above. Any symbol may nest under any other.
- Nesting means "this is about that". A con under a pro is a limitation. A pro
  under a con is a mitigation. A `?` under a `*` questions whether that
  condition really is fixed.
- Deeper indent with no symbol continues the line above. Same indent with no
  symbol is a neutral node.
- Depth is relative, not absolute. Two spaces is the convention; any consistent
  unit works, including tabs.
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

- **Emit PMB inside a fenced block tagged `pmb`.** Markdown treats `+`, `-` and
  `*` as bullet markers and will erase the distinction on render. Bare PMB is
  correct in plain text files, code comments, on paper, and anywhere Markdown
  is not rendered.
- Parse: `^([ \t]*)([+\-!?*~])(\2{0,2}|0(?:\.\d+)?|1(?:\.0+)?)?[ \t]+(.*)$`
  → indent, symbol, modifier, text. The modifier is either up to two repeats of
  the same symbol, or a weight in `[0,1]`. Build the tree from a relative-indent
  stack rather than dividing the indent by two. A line that does not match is
  neutral or a continuation, per the grammar.
- **Do not convert between intensity and weight.** `!!` is not `0.66`. Report
  whichever the author wrote — `intensity: 2` or `weight: 0.9` — and leave the
  other absent. An unweighted line is unweighted, **not `0.5`**; inventing a
  default fabricates a judgment the author declined to make.
- Preserve unrecognised leading symbols as text rather than dropping the line.
- Symbols are semantic, not evaluative. Do not count `+` against `-` to reach a
  verdict. A single `*` can end a decision on its own.
- When emitting: cap repeats at three, and prefer weights over repetition when
  precision matters. Never escalate past `!!!` to signal urgency.

## Rules of thumb

- Be specific. "Cuts cost 30% ($45k/yr)" beats "saves money".
- Deal-breakers at the top. Readers scan down and stop.
- Don't use every symbol every time. Over-symbolising is noise.
- Four levels of nesting usually means you are looping, not reasoning.
- Label what you don't know (`?` `~` `!`) instead of inventing a reason for it.

**The goal isn't perfect notation — it's better thinking. If a symbol doesn't
help, don't use it.**
