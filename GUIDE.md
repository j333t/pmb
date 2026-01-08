# PlusMinusBang User Guide

A practical guide to using PMB effectively for better thinking and decision-making.  
These are small things that take it to the next level. 

---

## Getting Started

### Your First PMB Document

Start simple. Pick a decision you're facing right now and write it down:

```
Should I [your decision]?
+ [One reason for]
+ [Another reason for]
- [One reason against]
- [Another reason against]
! [What's critical to know]
```

That's it. You're using PMB.  
Use it whenever and wherever you need to remember your reasons for later or for others. 

### Start With Three Symbols

Don't try to learn all seven symbols at once. Start with:
- `+` for things that support your decision
- `-` for things that oppose it
- `!` for critical information

Add the others (`? * ~`) only when you actually need them.

---

## Writing Effective PMB

### Be Specific

**Vague:** `+ Saves money`  
**Better:** `+ Reduces costs by 30% ($45k annually)`

**Vague:** `- Risky`  
**Better:** `- 40% chance of technical failure based on similar projects`

Specific points are easier to evaluate and harder to misunderstand.

### One Idea Per Line

If you're writing paragraphs, you're doing it wrong.

**Instead of:**
```
+ This would be good because it saves money and also the team has experience with it and customers have been asking for it
```

**Break it down:**
```
+ Saves money (30% cost reduction)
+ Team has prior experience
+ Customer demand is proven (40+ requests this quarter)
```

### Nest Your Thinking

When you write a point and immediately think "but..." or "however..." or "only if...", indent underneath it:

```
- Implementation takes 6 months
  + But we can ship an MVP in 2 months
    ! Only if we cut features X and Y
      ? Are those features actually needed?
```

This shows how your thoughts connect, not just what they are.

### Put Important Things First

Your future self (and others) will scan from the top. Put your deal-breakers and key insights first:

```
Should we acquire Company X? [2024-12-10]
! Must close by Q1 or we lose market opportunity
! Requires board approval (unlikely given last acquisition failure)
+ Adds $2M ARR
+ Strong technical team
- $15M acquisition cost
  + But 12-month payback period
```

The critical constraints are immediately visible. You can still keep scrolling further down for history.  
This also helps you rank which of your reasons carry more weight. 

---

## Using Extended Symbols

### When to Use `?` (Question)

Use `?` for genuine unknowns that need research:

```
- Integration might be complex
  ? How many API endpoints need updating?
  ? What's the current system architecture?
```

**Don't use `?` for:**
- Rhetorical questions ("? Isn't this obvious?")
- Soft opinions ("? I think this might work?")
- Things you could figure out by thinking harder

### When to Use `*` (Insight)

Use `*` for breakthroughs or reframes:

```
* Wait — we're optimizing for speed when users actually want simplicity
* The real competitor isn't Company X, it's the status quo
* This entire debate assumes we have 6 months, but the market window is 3
```

**Don't use `*` for:**
- Regular thoughts that happen to be yours (everything is your thought!)
- Mild observations
- Things you already knew

Reserve `*` for genuine "aha" moments that change the game.

### When to Use `~` (Flux)

Use `~` for unvalidated uncertainty:

```
~ Not sure if the team is fully on board with this direction
~ This partnership feels off somehow, can't articulate why
~ Moral dilemma: technically legal but feels ethically questionable
```

**Don't use `~` for:**
- Things you could easily verify (use `?` instead)
- Decisions you're procrastinating on
- Every single thought (that defeats the purpose)

When your `~` gets validated, upgrade it to `+` `-` or `!`.

---

## Time Management

### Dating Your Reasoning

Date major decision points:

```
Should we pivot the product? [2024-08-15]
+ Market feedback suggests new direction
- Would delay current roadmap by 4 months
! Runway: 8 months left

2024-09-01
* Talked to 10 more customers—they don't want the pivot
Decision: Staying course, improving core product instead
```

This creates a timeline of how your thinking evolved.  
Alternatively, you can also put newest reasons at the top, unless it breaks your flow of thought, or seems unnatural to read in reverse.    
If you are [ranking thoughts](#put-important-things-first), keep the most important ones at the top, then newest first under them. 

### Don't Delete, Append

When you were wrong, don't erase it. Add what you learned:

**Bad:**
```
+ This will definitely work
[removed embarrassing wrong prediction]
```

**Good:**
```
+ This will definitely work [2024-06-01]

[2024-08-01]
! That assumption was completely wrong
+ Learned: I underestimated integration complexity by 3x
```

Your mistakes are very valuable data.

### Using [EXP] Tags

When you notice a pattern repeating, mark it `[EXP]`:

```
[2024-10-15]
- Hired based on impressive interview performance
  ! They struggled with actual work—interview skills ≠ job skills
  [EXP: Third time this has happened—2021, 2023, now]
  * Pattern: I need to add work samples to hiring process
```

Search for `[EXP]` before making similar decisions in the future.

---

## Avoiding Confabulation

Confabulation is when your brain fills gaps in reasoning with real-sounding explanations that aren't fully true. 
It's not lying—it's your mind trying to maintain a coherent story.

**Confabulation is turning a vibe into a fake reason.**

### When Confabulation Happens

You're at risk when:
- You don't fully know something but feel pressure to explain
- Your memory is incomplete but you "remember" details
- You've already decided and are backfilling justification
- You're mixing assumptions with facts
- You're overconfident without solid evidence

### How PMB Prevents Confabulation

The notation forces you to label uncertainty instead of papering over it (like putting wallpaper over damp patches or cracks). 

**Confabulation sounds like:**
- "I guess the reason is..."
- "Probably because..."
- "It must be that..."

**PMB makes you write:**
```
? Why does this happen?
~ I have a hunch but not sure
! Assumption: X must be true (unverified)
```

### The Anti-Confabulation Checklist

**Before you write a "reason," ask:**

**Am I backfilling justification after deciding?**
```
Bad: I chose A, so let me list why A is good
Good: [2024-12-10] Listed reasons, chose A
      [2024-12-15] Chose A failed because X
      * Learn: My initial reasoning missed Y
```

**Did I separate assumptions from facts?**
```
Confabulation: + This will save money
Clear thinking: ! Assumption: Usage stays above 60%
                  + If assumption holds, saves 30%
                  ? Need to verify historical usage
```

**Am I mixing vibes with evidence?**
```
Confabulation: - This feels wrong, so here's why...
Honest: ~ This feels off, not sure why
        ? What's causing this feeling?
        ? What would I need to see to trust it?
```

**Did I check for missing information?**
```
Confabulation: + Obviously this will work
Clear: + Early signs are positive
       ? Need: market research, technical feasibility study
       ! Don't have enough data yet
```

**Am I overconfident?**
```
Ask yourself:
- What would change my mind?
- What evidence would contradict this?
- Which parts are assumptions vs facts?

Mark fragile assumptions with !
```

### When Revisiting Old Decisions

Don't rewrite history. Don't pretend you had reasons you didn't.

```
! UPDATE [2024-12-15]: My earlier assumption was wrong
* What I learned: [specific lesson]
* Pattern: [if this is recurring]
```

This prevents convincing yourself that you "knew all along."

---

## Common Patterns

### Decision Framework

```
Should we [decision]? [date]
! Critical constraints
! Must-have requirements
+ Key benefits
  - Limitations of those benefits
- Key risks
  + Mitigations for those risks
? Open questions
* Insights or reframes
Decision: [outcome and why]
```

### Research Notes

```
Topic: [question you're investigating]
+ Evidence supporting
  ! Confidence level / source quality
- Evidence contradicting
  ! Confidence level / source quality
? Gaps in knowledge
* Emerging patterns or insights
~ Tentative conclusions
```

### Retrospective / Post-Mortem

```
Project: [name] [date]
+ What worked
  * Why it worked (if we know)
- What didn't work
  * Why it failed (if we know)
  [EXP] if this is a recurring pattern
! Critical lessons
? Unanswered questions
* Changes for next time
```

### Weekly Reflection

```
Week of [date]
+ Wins
- Challenges
! What needs attention
? Open questions for next week
* Insights or patterns noticed
```

---

## Tips for Different Use Cases

### For Decisions

- Always date your decision points
- Include your actual choice and timeline
- Note what would change your mind
- Come back and add what you learned

### For Learning / Research

- Separate evidence (no markings) from interpretation (indent thoughts under evidence)
- Mark confidence levels on sources
- Use `?` for research directions
- Use `*` when you connect ideas

### For Team Collaboration

- Be specific so others can follow your reasoning
- Date all updates to show evolution
- Use `!` to highlight deal-breakers
- Link to relevant docs/data

### For Daily Notes

- Keep it simple—mostly just `+ - !`
- Don't overthink symbol choice
- Focus on capturing thoughts, not perfection
- Review weekly to spot patterns

---

## What to Avoid

### Don't Over-Symbolize

If you're using all 7 symbols in every note, you're over-engineering. Most notes need only `+ - !`.

### Don't Use PMB for Everything

Some things are better as:
- Plain prose (explanations, stories)
- Tables (comparisons with many dimensions)
- Diagrams (spatial relationships, flows)

PMB is for reasoning structure, not all writing.

### Don't Get Stuck in Analysis Paralysis

PMB helps you think clearly, but at some point you need to decide and act. If you're on your 4th level of nesting, you're probably overthinking.

```
- Risk of failure
  + But we can mitigate with X
    - But X costs money
      + But we'll save money on Y
        - But Y has other dependencies
          + But those are solvable
            ! You're in a loop. Time to decide.
```

### Don't Treat It Like a Grading System

PMB isn't about "winning" arguments by having more `+` than `-`. Sometimes one critical `!` outweighs ten pros.

The pattern tells the story, not the count.

---

## Advanced Techniques

### Separating Perspectives

When you need to see multiple viewpoints:

```
Acquisition decision [2024-12-10]

  From CEO perspective:
  + Strategic fit with vision
  - Distracts from core business
  
  From CFO perspective:
  + Accretive to revenue
  - High integration costs
    ! Cash flow implications
  
  From CTO perspective:
  - Technical debt in acquired codebase
  + Strong engineering team
    ! Culture fit is critical
```

### Tracking Confidence

Add confidence markers to assumptions:

```
! Assumption [HIGH CONFIDENCE]: Market grows 20% annually
! Assumption [MEDIUM CONFIDENCE]: Competitors won't react for 6 months
! Assumption [LOW CONFIDENCE]: Regulatory approval takes < 3 months
  ? This is pure guess, need expert opinion
```

### Linking Across Documents

Reference related reasoning:

```
! Capacity concerns here
  → See [2024-Q2-Infrastructure-Review] for details
  
- Team bandwidth issue
  ← Relates to [Hiring-Plan-2024]
```

(This will be easier when explicit linking syntax is formalized)

---

## Getting Help

- **Stuck on which symbol to use?** Start with `+ - !` and add others only when needed
- **Not sure if you're confabulating?** Ask: "Do I actually know this, or am I filling gaps?"
- **Analysis paralysis?** Set a timer. Decide after 15 minutes of PMB reasoning.
- **Want feedback?** Share your PMB notes in [GitHub Discussions](https://github.com/j333t/pmb/discussions)

---

## Remember

PMB is a tool for thinking, not a set of rules to follow perfectly.

- Use what helps
- Skip what doesn't
- Adapt to your needs
- Iterate as you learn

**The goal is better decisions, not perfect notation.**
