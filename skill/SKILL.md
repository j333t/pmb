---
name: pmb
description: Structure reasoning in PlusMinusBang notation — line-initial symbols (+ pro, - con, ! attention, * hard condition, ? unknown, ~ uncertain) with indentation for reply structure. Use when the user says "pmb this", mentions PlusMinusBang, asks for pros and cons or a tradeoff analysis, asks you to show or structure your reasoning, wants a decision written down or a decision log kept or appended to, or hands you a messy dump of thinking to organise. Also use when reading or editing files that already contain PMB.
---

# PlusMinusBang

A notation for structuring reasoning in plain text. A symbol at the start of a
line marks what kind of thought it is. Indentation marks what it responds to.

## Symbols

| Sym | Name | Means |
|-----|------|-------|
| `+` | Pro | Supports. Benefit, advantage, evidence for. |
| `-` | Con | Opposes. Drawback, risk, evidence against. |
| `!` | Attention | Note this. Worth keeping in view — but it can give way. |
| `*` | Hard | Cannot give way. Rules, laws, regulations, contract terms, physical limits. |
| `?` | Question | Genuine unknown. Needs research — not a soft opinion. |
| `~` | Flux | Unvalidated. Uncertainty not yet resolvable into `+ - !`. |
| none | Neutral | Fact, context, observation. No valence. |

`+ - !` cover about 90% of use.

**Choosing between `!` and `*`:** ask whether arguing could change it. A
deadline that could be renegotiated, a budget that could stretch, a risk worth
holding in mind — `!`. A regulation, a signed clause, a licence, a physical
limit — `*`. Never use `*` for something merely important; that is what `!` is
for.

## Grammar

- One thought per line: symbol, space, text.
- The symbol counts only as the **first non-whitespace character** of a line,
  and only when followed by **at least one space**. `-5%` is text; `- 5%` is a
  con. `2 + 2` is neutral text.
- Indent to respond to the line above. Any symbol may nest under any other.
  A con under a pro is a limitation; a pro under a con is a mitigation; a `?`
  under a `*` questions whether that condition is really fixed.
- Deeper indent with no symbol continues the line above. Same indent with no
  symbol is a neutral node.
- Depth is relative. Two spaces is the convention; any consistent unit works.
- `[TAG]` or `tag:` annotates out of band: `[OBSOLETE]`, `[EXP]` (a recurring
  pattern or hard-won lesson), `[UPDATE]`, `[RESOLVED]`, `[..]` (placeholder).
- Dates in ISO 8601 (`YYYY-MM-DD`). Case-insensitive.
- Symbols are semantic, not evaluative. Never tally `+` against `-` to reach a
  verdict. A single `*` can end a decision on its own.

**Always emit PMB inside a fenced block tagged `pmb`.** Markdown treats `+`, `-`
and `*` as bullet markers and will erase the distinction on render. Bare PMB is
correct only in plain text files, code comments, and on paper.

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

`!` marks what deserves attention and could still move. `*` marks what will not
move no matter what anyone decides.

---

## Three modes

### Read

When the user's files or messages contain PMB, parse it as reasoning structure.
Preserve it exactly in edits — never flatten it into prose or plain bullets, and
never re-order it to look tidier. Indentation and symbol choice are content.

### Write

When asked for a decision, a tradeoff, or your own reasoning, emit a ```pmb
block.

- Deal-breakers first. Readers scan down and stop.
- One thought per line. Be specific: "cuts cost 30% ($45k/yr)", not "saves money".
- Use only the symbols you need. Most reasoning needs only `+ - !`.
- Reserve `*` for the genuinely immovable. When unsure, use `!`.
- Mark genuine unknowns `?` or `~` rather than inventing support for them.
- Do not balance the document. If the evidence is one-sided, let it be.
- Finish with a one-line recommendation, separated from the reasoning.

### Convert

When handed a dump of prose:

- Preserve every claim. Do not summarise, drop, or merge.
- Do not add reasons the user did not give.
- Split compound sentences into one claim per line.
- Nest only where the user signalled the relation ("but", "however", "only if",
  "although", "unless").
- Where they hedged, use `~`. Do not sharpen it into a `+` or `-` for them.
- Where a load-bearing claim went unsupported, add a `?` naming what would have
  to be true, and mark it clearly as your addition.
- Keep their wording. Compress phrasing, never meaning.

---

## Appending to a decision log

Never edit an existing dated block. Add a new block at the top with today's
date. When something written earlier turned out wrong, say so in the new block
and **leave the wrong version standing** — the history is the whole value. If
the same lesson has appeared before, tag it `[EXP]` so it can be found again.

---

Full spec: https://plusminusbang.com/pmb.md — public domain (CC0).
