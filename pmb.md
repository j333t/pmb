# PlusMinusBang (PMB) v1.0

A notation for structuring reasoning in plain text. A symbol at the start of a
line marks what kind of thought it is. Indentation marks what it responds to.

Public domain (CC0). Canonical: https://plusminusbang.com/pmb.md

## Symbols

| Sym | Name | Means |
|-----|------|-------|
| `+` | Pro | Supports. Benefit, advantage, evidence for. |
| `-` | Con | Opposes. Drawback, risk, evidence against. |
| `!` | Bang | Critical. Constraint, dealbreaker, assumption that must hold. |
| `?` | Question | Genuine unknown. Needs research — not a soft opinion. |
| `*` | Insight | Reframe. Changes the question rather than taking a side. |
| `~` | Flux | Unvalidated. Uncertainty you cannot yet resolve into `+ - !`. |
| none | Neutral | Fact, context, observation. No valence. |

`+ - !` cover about 90% of use. The rest are optional.

## Grammar

- One thought per line: symbol, space, text.
- The symbol must be the **first non-whitespace character** of the line and must
  be followed by **at least one space**. `-5%` is text; `- 5%` is a con.
  Symbols appearing mid-line are text: `2 + 2` parses as neutral.
- Indent to respond to the line above. Any symbol may nest under any other.
- Nesting means "this is about that". A con under a pro is a limitation. A pro
  under a con is a mitigation. A `?` under a `!` questions the assumption.
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
Hire Priya to run sales? [2026-03-04]
+ Closed $4M at her last company
  ? Was that her, or the brand behind her
- Wants 25% above band
  + Band is two years stale
! Nobody on the panel has ever run a sales team
  - So we are grading on charisma
    ~ She is the most impressive person we have met. That is the worry.
? What would make me say no

[2026-03-11]
! Reference check: her last two hires both quit inside six months
Decision: hire. Strong closer, we will coach the management side.

[2026-09-20]
- Team of six down to three. Same shape as her last job.
  * The reference call already told me this. I read it as a detail, not a signal.
  [EXP] Third time I have hired a closer and hoped management would follow
```

## For machines

- **Emit PMB inside a fenced block tagged `pmb`.** Markdown treats `+`, `-` and
  `*` as bullet markers and will erase the distinction on render. Bare PMB is
  correct in plain text files, code comments, on paper, and anywhere Markdown
  is not rendered.
- Parse: `^([ \t]*)([+\-!?*~])[ \t]+(.*)$` → indent, symbol, text. Build the
  tree from a relative-indent stack rather than dividing the indent by two.
  A line that does not match is neutral or a continuation, per the grammar.
- Preserve unrecognised leading symbols as text rather than dropping the line.
- Symbols are semantic, not evaluative. Do not count `+` against `-` to reach a
  verdict. One `!` can outweigh ten `+`.

## Rules of thumb

- Be specific. "Cuts cost 30% ($45k/yr)" beats "saves money".
- Deal-breakers at the top. Readers scan down and stop.
- Don't use every symbol every time. Over-symbolising is noise.
- Four levels of nesting usually means you are looping, not reasoning.
- Label what you don't know (`?` `~` `!`) instead of inventing a reason for it.

**The goal isn't perfect notation — it's better thinking. If a symbol doesn't
help, don't use it.**
