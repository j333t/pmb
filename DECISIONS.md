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

---

## Closed

- **D1** — `*` is a hard condition; `!` is attention · 2026-08-09
- **D2** — repeated symbols mean intensity, capped at three · 2026-08-09
- **D3** — reframes get no symbol; the slot stays empty · 2026-08-09
- **D4** — weights: a number after the symbol, 0 to 1 · 2026-08-09
