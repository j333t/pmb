# Changelog

Notable changes to the PlusMinusBang specification.

The notation is versioned; the tooling around it is not. **The symbol set has
been frozen since 1.1** — six symbols and the neutral line, closed when D3
settled the last question about membership. Grammar, tags and tooling can still
move. The symbols cannot.

Reasoning for every entry below is in [DECISIONS.md](DECISIONS.md), where
nothing is deleted, including the arguments that lost.

---

## [1.2.1] — 2026-08-10

Parsing precision only. No change to the symbols or to what they mean.

```pmb
Parsing precision only. Symbols and meanings unchanged.
+ Three contradictions between pmb.md's prose and its own regex, closed
+ Seven questions the prose never answered, answered
- Documents using `!!!!`, `**`, `*0.5` or `!!0.9` may parse differently
  ! But no two 1.2 parsers agreed on those anyway — that was the bug
* Every one of these was found by writing the Internet-Draft.
  That was the point of writing it.
```

### Fixed

- **` !!!! ` and longer runs read as intensity 3.** The prose said a fourth
  repeat "just reads as three"; the published regular expression matched no
  such line at all, making it plain text. (D2)
- **` ** ` and `*0.5` are text.** ` * ` takes no repeats and no weight. The prose
  said so; the regular expression permitted both.
- **`!!0.9` is text.** Combining intensity with a weight was "not both" in
  `pmb.md` and "not forbidden" in D4, written the same week. Now forbidden: a
  weighted line carries exactly one symbol. (D4, amended)

### Added

- **Indent comparison is defined.** Drop the longest common prefix of two
  indents and compare what remains; longer is deeper. No tab width is assumed
  anywhere, because tab width is a display setting rather than a property of
  the document. (D5)
- **What a weight is measured against**: its own line, against the line it
  responds to. A stated weight is immutable — nothing computed later
  overwrites it. (D4)
- **Subtree aggregation.** The lines beneath a node bear on it, so magnitudes
  may be totalled as a derived value. Signs may not: a child's sign is relative
  to its parent and inverts at every level down, and four of the six symbols
  carry no sign at all. A signed sum is undefined, not merely discouraged. (D6)
- Continuations join their parent with a single space. Blank lines carry no
  meaning and never close a node.
- [`tools/token-comparison/`](tools/token-comparison/) — the measurement behind
  the token-cost claims, so they can be repeated rather than taken on trust.

### Changed

- **`pmb.md` no longer carries the reference regular expression or the parsing
  algorithm.** Those moved to the Internet-Draft, which states them more
  precisely. `pmb.md` keeps every rule governing how a reader or writer should
  behave. The split is deliberate: one file is the notation, the other is the
  interchange format.

---

## [1.2] — 2026-08-09

### Added

- **Intensity by repetition.** Repeat a symbol to mean "more so", capped at
  three. Already how people write emphasis everywhere, so it costs nothing to
  teach, and it gives a degree axis to every symbol for one line of grammar
  instead of spending a whole symbol on "a stronger ` ! `". (D2)
- **Weights.** A number from 0 to 1 immediately after the symbol, for how much
  the line counts. Promoted from Future Features. Mostly for machines: a model
  reading PMB knew the direction of every claim but nothing about magnitude.
  (D4)

---

## [1.1] — 2026-08-09

### Changed

- **` * ` is now hard conditions** — rules, laws, regulations, contract terms,
  physical limits. Anything that cannot give way. Everyone already reads ` * ` as
  "terms and conditions apply", and a symbol that borrows an existing reflex
  costs nothing to teach. (D1)
- **` ! ` is now attention** — worth keeping in view, but able to give way.
  Previously ` ! ` claimed the non-negotiables, which was the same sentence as
  the new ` * `. Re-scoping it removed the overlap. (D1)

```pmb
The test between them: can it give way?  No -> `*`   Yes -> `!`
- Cost: `*` used to mean insight, and a reframe now has no symbol at all
  + It has a home anyway — a reframe opens the next dated block rather
    than answering the line above it
  ~ Watch for reasoning notes that feel flatter than before. If reframes
    stop being written down, that is the cost showing up.
```

### Removed

- **` * ` no longer means insight.** A reframe gets no symbol at all; the slot
  stays empty. No glyph is universally read as "realisation", and the
  criterion for membership is that a symbol be understood everywhere without
  explanation. A reframe is written as a neutral line, or as ` ? ` when it is
  really a better question. (D3)

This closed the last open question about membership, freezing the symbol set.

---

## [1.0] — 2026-01-07

### Added

- Initial specification: ` + ` ` - ` ` ! ` ` ? ` ` * ` ` ~ ` and the neutral line,
  indentation for nesting, `[TAG]` annotations, ISO 8601 dates, and append-only
  time — old reasoning is kept, because being visibly wrong on the record is
  how you find out which of your patterns keep failing.
