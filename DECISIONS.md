# PMB Design Decisions

Open and settled questions about the notation, reasoned in the notation.

The goal is a core symbol set where no further improvement is possible — a set
understood everywhere, by default, without explanation. Once it reaches that
point it should never change again. This file is how we get there and how we
prove, later, why each symbol is what it is.

Nothing here is deleted. Losing arguments stay on the page.

---

## D1 — What does `*` mean?

**CLOSED 2026-08-09 · `*` is a hard condition**

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

**Status:** open · raised 2026-08-09 · not blocking

```pmb
? Should `!!` `++` `--` be legal, meaning "more so"
+ Already how people write emphasis, in every language and format
  + So it passes the universality test on its own
+ Gives a degree axis to all seven symbols for one line of grammar
+ Degrades safely — a parser that ignores it reads `!!` as `!` plus text
- Adds a judgment call at write time
  + But an optional one. Nobody has to reach for it.
- Risks an arms race: `!!!`, `!!!!`
  ~ Cap at two, or leave it and trust people
! Currently ungrammatical. `!! foo` fails the "symbol, then one space" rule.
  So this needs an explicit decision either way — silence lets parsers
  disagree, which is what the grammar exists to prevent.
```

---

## D3 — Does a reframe need its own symbol?

**Status:** open · raised 2026-08-09 · consequence of D1

```pmb
D1 gave `*` to hard conditions, so reframes now have no symbol.
? Do they need one, or was that a symbol PMB didn't owe them

- No universal glyph exists for "realisation" or "aha"
  By the D1 criterion that settles it: if nothing is understood
  everywhere by default, nothing qualifies, and the slot stays empty
  + Every surviving symbol has a universal reading —
    + and - arithmetic, ! attention, ? question, * fine print,
    ~ approximately. Insight never had one. That's why it kept
    feeling arbitrary.
+ Reframes can be written as neutral lines. They're usually statements.
  "The real competition isn't Company X, it's the status quo"
  + Reads fine unmarked
+ Or as `?` when the reframe is really a better question
  "? Are we solving the wrong problem"
- Cost: the reframe stops being visually findable
  ! The single highest-value line in a document no longer stands out
    ~ Which may be acceptable. Rare things can be read for.
? Alternative: a [insight] or [aha] meta tag
  + Uses machinery that already exists
  - Slower to write than a symbol, same objection that lost D1 for tags
~ Leaning: leave the slot empty. Six symbols that are all universal beats
  seven where one needs explaining.
  That is exactly the convergence D1's criterion is aiming at.
```

---

## Closed

- **D1** — `*` is a hard condition; `!` is attention · 2026-08-09
