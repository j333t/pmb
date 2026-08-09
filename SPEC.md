# PlusMinusBang Specification

**Version:** 1.2  
**Last Updated:** 2026-08-09

> **Changed in 1.2:** Repeating a symbol (`!!`, `!!!`) means "more so", capped
> at three. Weights (`+0.8`) are promoted from Future Features to the spec.
> Reasoning: [DECISIONS.md](DECISIONS.md) D2 and D4.
>
> **Changed in 1.1:** `*` is now *hard conditions* — rules, laws, contract terms,
> anything that cannot give way. `!` is now *attention* — things worth keeping in
> view that could still move. Previously `*` meant insight and `!` claimed the
> non-negotiables, which made the two overlap. Reasoning: [DECISIONS.md](DECISIONS.md) D1.

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
Attention. Things to keep in view — warnings, risks, must-hold assumptions.  
**Use for:** What you'd regret overlooking. Deadlines, exposure, fragile assumptions, anything that deserves a second look.

**Examples:**
```
! Must launch before Q4 or we miss the market window
! Critical assumption: AWS pricing stays flat (high risk)
! Only two people know how this deploys
```

`!` is for things that matter but could still move — a deadline you might renegotiate, a budget you might stretch, a risk you might mitigate. For things that cannot move at all, see [`*` Hard conditions](#-hard-conditions).

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

#### `*` Hard conditions
Things that cannot give way, whatever anyone decides.  
**Use for:** Rules, laws, regulations, contract terms, licences, physical limits — the fine print.

**Examples:**
```
* Section 4.2 of the ToS prohibits commercial redistribution
* API rate limit is 1000 req/min per account, not per endpoint
* GDPR requires explicit consent; a cookie banner isn't sufficient
* Lease runs three years with no exit clause
```

**Rationale:** Everyone already reads `*` as "terms and conditions apply". Borrowing that reflex costs nothing to teach, and hard conditions are exactly what fine print is.

**`!` or `*`?** Ask whether arguing could change it.

| | Can it give way? | |
|---|---|---|
| `!` | Yes — with negotiation, budget, or effort | `! Client wants it by Friday` |
| `*` | No — not by any decision of yours | `* Contract says 30 days' notice` |

If you're unsure, use `!`. Reserving `*` for the genuinely immovable is what makes it worth scanning for.

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

## Intensity and Weight

Both optional. Both express how much a line counts. Use one or the other, not both.

### Repeating a symbol

Repeat a symbol to mean "more so", up to three:

```
! Worth watching
!! Worth watching closely
!!! Drop everything
```

Three is the maximum. A fourth repeat simply reads as three. `*` does not repeat — a hard condition either holds or it doesn't.

You don't need a rule to stop you overdoing this. Ten exclamation marks is obviously unreadable, and you'll see that yourself. The cap exists so that machines writing PMB don't escalate indefinitely, and so parsers behave the same way everywhere.

### Weights

A number from 0 to 1 immediately after the symbol, before the space, is that line's weight — how much it should count. 0 is negligible, 1 is decisive.

```
+0.8 Cuts delivery time in half
-0.3 Marginally more expensive to run
!0.9 Contract renews automatically unless we act by the 30th
?0.7 We still don't know the renewal terms
```

For `+` and `-` the symbol supplies the sign, so the whole token reads as a signed weight between -1 and 1. For `!` `?` `~` the number is magnitude only. `*` takes no weight.

**Weights are mostly for machines.** Most people will never write one, and shouldn't feel they ought to. Their value is that a model reading PMB currently knows the *direction* of every claim but nothing about *magnitude* — it has to infer importance from wording, which is exactly the inference PMB exists to remove.

**An unweighted line is unweighted. It does not mean 0.5.** Absent is absent, not middling.

### How this affects the space rule

A symbol must be followed by a space. Intensity and weight sit inside the symbol token, so the space comes after them:

| Written | Reads as |
|---|---|
| `- 5% is acceptable` | Con, no weight |
| `-5%` | Text — no space after the symbol |
| `-0.5 Leaves no buffer` | Con, weight -0.5 |
| `-0.5% drop in margin` | Text — no space after the number |
| `!! Worth watching closely` | Attention, intensity 2 |
| `!!foo` | Text |

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
Learned: always ask for written policies, not verbal promises

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
  Pattern: I'm swayed by confidence over competence
```

---

## Best Practices

### Writing Guidelines

- **Keep the most important considerations at the top** - Your hard conditions, deal-breakers, or final conclusions should be immediately visible
- **Be specific** - "Reduces costs by 30%" beats "Saves money"
- **One point per line** - If you're writing paragraphs, break them into atomic claims
- **Nest counterarguments** - Don't just list pros and cons–show how they interact

### Symbol Usage

- **Start with `+` `-` `!`** - These cover 90% of use cases
- **Add `?` when you have genuine unknowns** - Don't use it as a softer way to state opinions
- **Reserve `*` for the genuinely immovable** - Rules, laws, contract terms. If arguing could change it, it's `!`
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
  ? Could we do a PWA instead–no store cut, faster iteration

2024-06-15
Talked to 20 users–they don't actually want an app
  They want mobile web to not suck
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
? Wrong question–ask "for whom, under what conditions?"
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
    ? Wait–what if we hire manager first using current profits?
      + Proven location could fund new manager salary
      ~ Not sure if that's the right sequence

[2024-08-15]
? Talked to 3 other business owners who expanded
  All said biggest mistake was expanding before systems were solid
  ! We don't even have training documentation yet
    - New location would be "winging it" like we did
      [EXP: Remember 2022 chaos with first location]
Decision: Pause expansion. Spend 6 months documenting + systemizing current location first.
```

---

## Future Features

The following features are under consideration for future versions:

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
