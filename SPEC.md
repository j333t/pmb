# PlusMinusBang Specification

**Version:** 1.0  
**Last Updated:** 2026-01-07

---

## Overview

PlusMinusBang (PMB) is a notation system for structuring reasoning in plain text. It uses symbols at the start of lines to mark semantic meaning, making thought patterns instantly scannable.

PMB is like HTML for thinking – it structures your reasoning so your future self (and others) can reconstruct your thought process accurately.




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
>[!Note]
>You will naturally feel like completing the sentence with one more `?`, but that is left upto you to use it. I prefer using it for grammar's sake. 

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
* We're solving the wrong problem – users don't want faster, they want simpler
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

**Rationale:** Questions (`?`) seek information. Flux captures the state of sitting in uncertainty even when you *have* information.  
When validated, the flux graduates to `+`, `-`, or `!`.

#### `[]` or `Meta` Tags
Two types:  
1. With the `[]` for highlighting a tag. Better visibility.  
2. With `:` after the meta tag. Faster to write  
Choose whichever one is faster to process  
**Use for:** Version markers, status tags, cross-references, etc. 

**Examples:**
```
[obsolete] 2024-12-15
- This concern no longer applies

[exp] Repeated pattern from 2021, 2023
! Don't make this mistake again

ref: link to another reason
```

**Common meta tags:**
- `[OBSOLETE]` - Information that's no longer valid
- `[EXP]` - Experience / timeless lesson or recurring pattern
- `[UPDATE]` - Marks a revision point
- `[RESOLVED]` - Question or issue closed
- `[..]` - Placeholders. You can even describe what should be there

Can add more info in the bracket for clarity.  
Use either lower or upper case everywhere for readibility. 

---

## General formating rule
**Case agnostic**  
Use as per your preference. Consistency recommended for easier reading. 

**Dates**  
ISO 8601 format recommended `YYYY-MM-DD`

**Markdown**  
Use as usual. Example: 
```
- + this is a point for
- - this is a point against
- ! this is a bang
```

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

Indent related points under their parent to create argument threads. 

**Use 2 spaces for each level of nesting.**

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

**Any symbol can be nested under any other symbol.** 

<details>
<summary><b>See common patterns</b></summary>

- `+` nested under `-` (mitigating factor for a risk)
- `-` nested under `+` (limitation of a benefit)
- `!` nested under anything (critical caveat)
- `?` nested under `!` (questioning an assumption)

This creates **argument trees** where every pro can have counter-cons, every con can have mitigating factors, and complexity is preserved. The nesting shows which thoughts are responses to which other thoughts.

**Example:**
```
- this looks complicated
  + but it captures every nuance
+ gives infinite detail
  - however may seem difficult for beginners
    ! but they understand as soon as they try it
! Must ensure not to over do this
  ? if they have to stop and think, how will it help them capture everything raw?
```
</details>

---

## Time and Evolution

### Versioning Reasoning

**Don't delete old thoughts.** They show your reasoning evolution – what you got wrong, what changed, how you learned.

**Guidelines:**

1. **Date major decision points** using ISO 8601 format `YYYY-MM-DD`
2. **Add new reasoning above old reasoning** (newest first)
3. **When reality contradicts your reasoning, document what you learned**

**Example:**
```
Should I take the job?
2024-01-20 Declining offer
? Asked for written remote policy
! They want 4 days in office - "remote-first" was misleading
* Learned: Always ask for written policies, not verbal promises

2024-01-15
+ 40% salary increase
+ Better title and growth opportunity
- 90-minute commute each way
! They claim "remote-first" but no written policy
```

### Marking Obsolete Information

Tag something `[OBSOLETE]` only if it's dangerous to act on and the temporal ordering isn't clear enough.

```
! Must use PostgreSQL for compliance
[OBSOLETE 2024-03: Compliance rules changed, MySQL now allowed]
```

In most cases, dating your updates makes obsolescence obvious without explicit tags.

### Experience Patterns

Mark recurring lessons or patterns with `[EXP]` (experience) so they are easier to spot & recollect.

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
- **Nest counterarguments** - Don't just list pros and cons–show how they interact

### Symbol Usage

- **Start with `+` `-` `!`** - These cover 90% of use cases
- **Add `?` when you have genuine unknowns** - Don't use it as a softer way to state opinions
- **Reserve `*` for true insights** - Not every thought is an epiphany
- **Use `~` sparingly** - For genuine uncertainty, not just "I haven't decided yet"

### Avoiding Common Pitfalls

**Don't go crazy with symbols.** PMB is a tool for clarity, not decoration. If you're using all 7 symbols in every note, you're probably over-engineering. 

---

## Examples

### Product Decision

```
Should we build a mobile app? 2024-06-01
+ 60% of traffic is mobile web
+ Competitors all have apps
- Would cost $200k and 6 months
  ? Can we ship MVP in 3 months instead?
- Team has no mobile experience
  + But Sarah used to work at Meta on mobile
! App stores take 30% cut
  * We could do PWA instead–no store cut, faster iteration

2024-06-15
* Talked to 20 users–they don't actually want an app
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
* "Does it work?" is wrong question–need "For whom? Under what conditions?"
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
    * Wait–what if we hire manager first using current profits?
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

#### Weights
Optional numeric indicators for confidence or importance levels.

#### Explicit Linking
Direct references between related reasoning across documents or time periods.

#### Dedicated Tools to solve for:   
- Weight visualization
- Cross-document linking
- Long-term storage and search
- Auto-complete for common patterns

---

## Contributing

PMB is an open notation system. Use it, adapt it, build tools for it.

To propose changes to this specification:
1. [Discuss](https://github.com/j333t/pmb/discussions) with the community
2. Open an [issue](https://github.com/j333t/pmb/issues)
3. Submit a pull request with your proposed changes

Share your examples, templates, and tool integrations. The more people use structured reasoning, the better we all think.

---

## License

This specification is released under CC0 1.0 Universal (Public Domain).

PMB notation is public domain. Use freely in personal, commercial, and academic contexts.

---

## Reminder

**The goal isn't perfect notation–it's better thinking.**

If a symbol doesn't help, don't use it. If you need to break the rules, break them. The map is not the territory, and the notation is not the thought.
