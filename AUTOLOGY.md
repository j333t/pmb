# Autology

*Autological* — a word that describes itself. "Short" is short. "Polysyllabic"
is polysyllabic.

This is PMB on PMB: every symbol in the set, examined in the notation it belongs
to, using the symbols it is arguing about.

Partly a test. If a notation can't hold an argument about itself, it can't hold
much. Partly a record — the case for each symbol, kept where anyone can check it.

Decisions and open questions live in [DECISIONS.md](DECISIONS.md).
Syntax lives in [pmb.md](pmb.md).

---

## `+` — supports

```pmb
+ Arithmetic. Everyone alive reads + as "more", "add", "good".
  + Nothing to teach. Nothing to translate. No cultural exception known.
+ Half of the name. PlusMinusBang doesn't survive losing it.
+ One keystroke
  - Shifted on most layouts, where `=` sits unshifted right beside it
    ~ Considered and dropped. Recognition beats keystroke economy,
      every time.
- Collides with Markdown's bullet marker
  + Fenced ```pmb blocks resolve it
? Does `+` invite scorekeeping — tallying pluses against minuses
  ! It does. That is the single most common misuse of PMB.
    + The spec says so directly: symbols are semantic, not evaluative,
      and a single `*` can end a decision that ten `+` could not win
    - Saying so doesn't stop people doing it
      ~ Possibly unfixable. The instinct to count is older than the notation.
```

---

## `-` — opposes

```pmb
+ Arithmetic again, and the natural pair to `+`
* Load-bearing for the identity, not just the grammar. The notation is
  named PlusMinusBang. `-` cannot be swapped for something cleaner.
- The most collision-prone character in the whole set
  ! Markdown bullet, hyphen, minus sign, en-dash, YAML list item,
    CLI flag, and the start of any negative number
  ! The space is doing enormous work: `-5%` is text, `- 5%` is a con
    ? Is a rule that hinges on one space too fragile
      - On paper nobody writes `-5%` at the start of a reasoning line,
        so in practice the ambiguity almost never arises
      + And for parsers the rule is explicit and testable
        * Verified against fifteen edge cases before it shipped
      ~ Still the rule most likely to trip someone. Worth watching.
```

---

## `!` — attention

```pmb
+ Universal. Warning signs, alerts, and "bang" in half the programming
  languages ever written.
+ A third of the name, and the symbol that makes PMB more than a
  pros-and-cons list
  Plus and minus alone is a list. `!` is what makes it reasoning.
- Was overloaded until 2026-08-09
  ! It used to claim "deal-breakers, constraints, non-negotiable
    requirements" — which is now `*`
  + Narrowing it to attention made both symbols sharper
    * Recorded as D1
? Is "attention" too vague to be a kind rather than a degree
  ~ Probably the least crisply defined symbol in the set
  + But it's the one people reach for most often, and vagueness in the
    common case costs less than hesitation would
  + It also has a clean test against its neighbour: if arguing could
    change it, it's `!`; if not, it's `*`
```

---

## `*` — cannot give way

```pmb
+ "*terms and conditions apply" is possibly the strongest symbol-meaning
  association in all of written culture
  + Stronger, arguably, than + and - for pro and con
  + Borrowing an existing reflex costs nothing to teach, which is the
    highest-value property a symbol can have
* Binary by definition. Takes no weight and no repetition — a condition
  either holds or it does not.
  + Which is a useful check that D1 drew the line in the right place.
    A symbol that resists intensity is a symbol carrying a real kind.
- The newest meaning in the set, settled 2026-08-09
  ! So it has the least real usage behind it of any symbol here
- Cost: `*` used to mean insight. Reframes now have no symbol at all.
  ? Open as D3, and leaning towards leaving the slot empty
- Worst Markdown collision of the three
  ! Not only a bullet marker but also the emphasis character, so a bare
    `* foo` line can mangle in ways `+` and `-` do not
    + Fenced blocks resolve it
```

---

## `?` — a genuine unknown

```pmb
+ Universal, and the only symbol whose meaning nobody has ever queried
* Not a Markdown character. Survives rendering intact.
  + One of only two that do. `?` and `!` are the notation's safe pair.
+ Arguably does the most work per use of anything in the set
  It is the symbol that turns a conclusion back into an inquiry
- The most misused, by a distance
  ! Used as a soft way to state an opinion — "? Isn't this obvious"
  ! Used for things you could resolve by thinking for one more minute
    + The spec calls out both, explicitly
? Should a `?` that gets answered be rewritten or removed
  - No. Append the answer and leave the question standing.
    * Nothing in PMB is deleted. The question having been open is
      itself part of the record.
```

---

## `~` — unvalidated

```pmb
+ Reads as "approximately" in maths and in ordinary writing
+ The rarest symbol, and quite possibly the most valuable
  It is the only way to write "I don't know why I feel this" without
  the thought collapsing into prose and disappearing
  + And it's the symbol that catches confabulation at the moment
    of writing, rather than in review when it's too late
- Hardest to reach on a keyboard — shift plus backtick
  ~ Which may be exactly why it stays underused
? Is `~` really distinguishable from `?` in practice
  + The distinction is sharp on paper: `?` seeks information you don't
    have, `~` sits in uncertainty you cannot resolve even with it
  - People conflate them constantly anyway
    ! Most frequently asked question about the notation
    ~ Unclear whether that's a documentation failure or a real
      overlap. Worth watching before the set is frozen.
* Not a Markdown character at line start, so it survives rendering
```

---

## `(no symbol)` — neutral

```pmb
The absence of a symbol is a symbol.
+ The most important design choice in PMB, and the easiest to miss
  Not everything is an argument. A notation that demanded a symbol on
  every line would be abandoned inside a day.
+ Costs nothing. It is the absence of a decision, not a decision.
+ Makes every other symbol mean something, by contrast
  ! If every line were marked, no line would stand out —
    which is the same reason `*` has to stay rare
- Ambiguous against continuation lines
  ! Same indent with no symbol is a neutral node.
    Deeper indent with no symbol continues the line above.
  ~ Correct and unambiguous once stated, but it's the rule readers
    get wrong most often on first encounter
```

---

## The set as a whole

```pmb
Six symbols and an absence.
* The governing criterion: every symbol must be understood everywhere,
  by default, with no explanation. Nothing outranks this.
+ All six now pass it
  + and - arithmetic · ! warning · * fine print · ? question ·
  ~ approximately
  * Insight never passed, which is why it always felt arbitrary
    and why the slot is likely to stay empty
+ Three cover about 90% of real use, so the cost of the other three
  is close to zero for anyone who never reaches for them
- Three of the six collide with Markdown bullets
  ! Which plausibly explains why nothing like this caught on in twenty
    years — the symbols vanish exactly where writing happens
  + Fenced ```pmb blocks resolve it, and that was the first decision made
? Is the set finished
  ~ Close. D3 is the last open question about membership, and it is
    leaning towards "no new symbol".
  ! Once it closes, the set should stop changing permanently.
    A notation that keeps moving cannot be built on.
    * That is the whole point of writing these arguments down: so the
      set can be frozen with the reasons attached, and anyone who wants
      to reopen it has to answer what is already here.
```
