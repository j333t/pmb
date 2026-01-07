# PlusMinusBang Specification

**Version:** 1.0  
**Last Updated:** 2024-12-10

---

## Overview

PlusMinusBang (PMB) is a notation system for structuring reasoning in plain text and outlines. It uses symbols at the start of lines to mark semantic meaning, making thought patterns instantly scannable.

PMB is like HTML for thinking—it structures your reasoning so your future self (and others) can reconstruct your thought process accurately.

---

## Core Syntax

### Essential Symbols

#### `+` Pro
Points that support something. Arguments in favor.

**Use for:** Benefits, advantages, reasons to proceed, evidence supporting a hypothesis.

**Examples:**
```
+ Reduces costs by 30%
+ Team has experience with this technology
+ Customer feedback is overwhelmingly positive
```

#### `-` Con
Points against something. Arguments opposing.

**Use for:** Drawbacks, risks, reasons to avoid, evidence contradicting a hypothesis.

**Examples:**
```
- Implementation would take 6 months
- Requires hiring 3 new engineers
- Competitor already dominates this space
```

#### `!` Bang
Critical information. Usually caveats, warnings, or must-hold assumptions.

**Use for:** Deal-breakers, constraints, non-negotiable requirements, critical dependencies.

**Examples:**
```
! Must launch before Q4 or we miss the market window
! Critical assumption: AWS pricing stays flat (high risk)
! Regulatory approval required in EU
```

#### `?` Question
Open questions, gaps in knowledge, things to research.

**Use for:** Unknowns, uncertainties requiring investigation, hypotheses to test.

**Examples:**
```
? What's the actual market size?
? Can our infrastructure handle 10x traffic?
? Do we have the legal rights to this approach?
```

#### `(no symbol)` Neutral
Observations, facts, context, or general information.

**Use for:** Background, definitions, statements without clear valence.

**Examples:**
```
The meeting is scheduled for Tuesday
Current system uses PostgreSQL
Industry standard is 99.9% uptime
```

---

## Extended Syntax

These symbols are optional. Use only when the essential symbols don't capture your intent.

#### `*` Insight
Your own ideas, epiphanies, realizations.

**Use for:** Breakthroughs, reframes, "aha moments" that aren't clearly pro/con yet.

**Examples:**
```
* We're solving the wrong problem—users don't want faster, they want simpler
* The real competition isn't Company X, it's the status quo
* This entire debate assumes linear growth, but network effects change everything
```

**Rationale:** Insights often reframe the entire question rather than supporting one side. They're generative, not evaluative.

#### `~` Flux
Unvalidated ideas, uncertainty, ambivalence, drafts.

**Use for:** Pre-reasoning thoughts, moral dilemmas, probabilistic fog, brainstorming before you've decided if something is pro/con.

**Examples:**
```
~ Unsure if my co-founder is fully committed
~ This stock looks undervalued, but technicals are unclear
~ Feels ethically wrong, but can't articulate why yet
~ Moral dilemma
```

**Rationale:** Questions (`?`) seek information. Flux captures the state of sitting in uncertainty even when you *have* information. When validated, flux graduates to `+`, `-`, or `!`.

#### `[]` Meta Tags
Dates, status markers, and metadata.

**Use for:** Timestamps, version markers, status tags, cross-references.

**Examples:**
```
[2024-12-10]
+ Initial analysis completed

[OBSOLETE 2024-12-15]
- This concern no longer applies

[EVERGREEN: Repeated pattern from 2021, 2023]
! Don't make this mistake again
```

**Common meta tags:**
- `[YYYY-MM-DD]` - Dates (ISO 8601 format recommended)
- `[OBSOLETE]` - Information that's no longer valid
- `[EXP]` - Experience / timeless lesson or recurring pattern
- `[UPDATE]` - Marks a revision point
- `[RESOLVED]` - Question or issue closed

---

## Structure and Nesting

### Basic Structure

Start each point on a new line with a symbol followed by a space.

```
+ First benefit
+ Second benefit
- First risk
- Second risk
```

### Nesting

Indent related points under their parent to create argument threads. **Use 2 spaces for each level of nesting.**

Think of nesting as a conversation with yourself. When you write a point and immediately think "but..." or "however..." or "only if...", indent and write that counter-thought underneath.

```
- High upfront cost
  + But amortizes over 5 years
    ! Only if usage stays above 60%
      ? What's our historical usage trend?
```

**Reading the nesting:**
- "It's expensive"
  - "Yes, but it pays for itself"
    - "Only under certain conditions"
      - "Do we meet those conditions?"

**Any symbol can be nested under any other symbol.** Common patterns:
- `+` nested under `-` (mitigating factor for a risk)
- `-` nested under `+` (limitation of a benefit)
- `!` nested under anything (critical caveat)
- `?` nested under `!` (questioning an assumption)

This creates **argument trees** where every pro can have counter-cons, every con can have mitigating factors, and complexity is preserved. The nesting shows which thoughts are responses to which other thoughts.

---

## Time and Evolution

### Versioning Reasoning

**Don't delete old thoughts.** They show your reasoning evolution—what you got wrong, what changed, how you learned.

**Guidelines:**

1. **Date major decision points** using ISO 8601 format (YYYY-MM-DD)
2. **Add new reasoning above old reasoning** (newest first)
3. **When reality contradicts your reasoning, document what you learned**

**Example:**
```
Should I take the job? [2024-01-15]
+ 40% salary increase
+ Better title and growth opportunity
- 90-minute commute each way
! They claim "remote-first" but no written policy

[2024-01-20]
? Asked for written remote policy
! They want 4 days in office - "remote-first" was misleading
* Learned: Always ask for written policies, not verbal promises
Decision: Declining offer
```

### Marking Obsolete Information

Tag something `[OBSOLETE]` only if it's dangerous to act on and the temporal ordering isn't clear enough.

```
! Must use PostgreSQL for compliance
[OBSOLETE 2024-03: Compliance rules changed, MySQL now allowed]
```

In most cases, dating your updates makes obsolescence obvious without explicit tags.

When you revisit a decision, don't rewrite history or pretend you had reasons you didn't actually have. Instead, add a dated update:

```
! UPDATE [2024-01-07]: My earlier assumption was wrong.
```

This prevents confabulated "retroactive logic."

### Experience Patterns

Mark recurring lessons or patterns with `[EXP]` (experience) so they surface when relevant.

**Use EXP for:**
- Repeated mistakes: "I keep doing X and it fails"
- Hard-won lessons: Insights that took years to learn
- Blind spots: Biases you've identified in yourself
- Life principles: Rules you've derived from experience

**Example:**
```
[2024-06-15]
- Hired based on charisma without technical validation
  ! Turned out they couldn't actually code
  [EXP: Same mistake in 2021 with Mark, 2023 with Sarah]
  * Pattern: I'm swayed by confidence over competence
```

---

## Best Practices

### Writing Guidelines

- **Keep the most important considerations at the top** - Your deal-breakers, critical insights, or final conclusions should be immediately visible
- **Be specific** - "Reduces costs by 30%" beats "Saves money"
- **One point per line** - If you're writing paragraphs, break them into atomic claims
- **Nest counterarguments** - Don't just list pros and cons—show how they interact

### Symbol Usage

- **Start with `+` `-` `!`** - These cover 90% of use cases
- **Add `?` when you have genuine unknowns** - Don't use it as a softer way to state opinions
- **Reserve `*` for true insights** - Not every thought is an epiphany
- **Use `~` sparingly** - For genuine uncertainty, not just "I haven't decided yet"

### Avoiding Common Pitfalls

**Don't go crazy with symbols.** PMB is a tool for clarity, not decoration. If you're using all 7 symbols in every note, you're probably over-engineering.

**The pattern tells the story.** The beauty of this system is it doesn't need a "conclusion" symbol—the reasoning tree *is* the conclusion. The pattern of `+` `-` `!` tells the story.

---

## Avoiding Confabulation

Confabulation happens when your mind fills in missing reasoning with something that sounds right, even though it isn't grounded in actual evidence. It's not lying—it's your brain trying to maintain a coherent story.

**Confabulation is that moment when you turn a vibe into a fake reason.**

### When Confabulation Happens

- You don't fully know something
- Your memory is incomplete
- Your reasoning has gaps
- You're unsure but feel pressure to produce an answer
- Inventing a reason because you feel you should have one
- Backfilling explanations after a decision
- Overconfidence when you actually don't know
- Mixing assumptions with facts

### How PMB Helps Prevent Confabulation

**The notation system forces you to label uncertainty instead of papering over it.**

Confabulation happens when you forget something was an assumption and start treating it as a fact. PMB's structure keeps assumptions visible so they don't silently harden into "truth."

### Recognizing Confabulation Triggers

If you feel tempted to "explain" something you're not sure about, that's the confabulation trigger.

**Confabulation often sounds like:**
- "I guess the reason is…"
- "Probably because…"
- "It must be that…"

**If you catch yourself doing this, replace it with:**
```
? Why does this happen?
~ I have a hunch but not sure
```

### Anti-Confabulation Checklist

**Am I backfilling a justification after the fact?**

Don't rewrite history. Add dated updates instead of pretending you always knew.

**Did I separate assumptions from facts?**

Confabulation thrives when assumptions silently become "truth." Use:
```
! Critical assumption: X must be true for this to work
```

If it later turns out false, you'll see exactly where your reasoning broke.

**Am I mixing vibes with evidence?**

A feeling is valid—but it's not a reason. Instead of inventing a reason to justify a vibe, write:
```
~ This feels off, not sure why
? What is causing this feeling?
```

This keeps intuition honest without forcing fake logic.

**Did I check for missing information?**

Confabulation fills gaps. The notation system exposes gaps. Use:
```
? Missing data: X
? Need to research: Y
```

If you don't know, say so explicitly.

**Am I overconfident?**

If you feel unusually certain, ask:
- What would change my mind?
- What evidence would contradict this?
- Which part of this is assumption vs fact?

Mark the fragile parts with `!`.

---

## Examples

### Product Decision

```
Should we build a mobile app? [2024-06-01]
+ 60% of traffic is mobile web
+ Competitors all have apps
- Would cost $200k and 6 months
  ? Can we ship MVP in 3 months instead?
- Team has no mobile experience
  + But Sarah used to work at Meta on mobile
! App stores take 30% cut
  * We could do PWA instead—no store cut, faster iteration

[2024-06-15]
* Talked to 20 users—they don't actually want an app
  * They want mobile web to not suck
Decision: Fix mobile web, table native app for now
```

### Research Notes

```
Does intermittent fasting work for longevity?
+ Meta-analysis shows improved metabolic markers [Study 2023]
+ Animal studies show 20-30% lifespan extension
  ! But mice ≠ humans
- Human RCTs are short-term (≤2 years)
  ? Are there any 10+ year studies?
~ Personal experience: Feel better when fasting, but is that placebo?
* "Does it work?" is wrong question—need "For whom? Under what conditions?"
```

### Business Decision

```
Should we open a second location? [2024-08-01]
+ Current location at 95% capacity
+ 40+ customers on waitlist weekly
+ Strong brand recognition in city
- Requires $300k upfront investment
  + But we have $450k in savings
  ! Need to keep 6 months runway ($180k)
    ? Can we negotiate landlord to phase payments?
- Would split management attention
  ! I'm already working 70-hour weeks
  - Can't hire manager until location is profitable
    * Wait—what if we hire manager first using current profits?
      + Proven location could fund new manager salary
      ~ Not sure if that's the right sequence

[2024-08-15]
? Talked to 3 other business owners who expanded
  * All said biggest mistake was expanding before systems were solid
  ! We don't even have training documentation yet
    - New location would be "winging it" like we did
      [EXP: Remember 2022 chaos with first location]
Decision: Pause expansion. Spend 6 months documenting + systemizing current location first.
```

---

## Future Features

The following features are under consideration for future versions:

### Weights
Optional numeric indicators for confidence or importance levels.

### Explicit Linking
Direct references between related reasoning across documents or time periods.

### Dedicated Tools
- Long-term storage and search
- Auto-complete for common patterns
- Cross-document linking
- Weight visualization

---

## Contributing

PMB is an open notation system. Use it, adapt it, build tools for it.

To propose changes to this specification:
1. Open an issue at [github.com/j333t/pmb/issues](https://github.com/j333t/pmb/issues)
2. Discuss with the community
3. Submit a pull request with your proposed changes

Share your examples, templates, and tool integrations. The more people use structured reasoning, the better we all think.

---

## License

This specification is released under CC0 1.0 Universal (Public Domain).

PMB notation is public domain. Use freely in personal, commercial, and academic contexts.

---

## Reminder

**The goal isn't perfect notation—it's better thinking.**

If a symbol doesn't help, don't use it. If you need to break the rules, break them. The map is not the territory, and the notation is not the thought.
