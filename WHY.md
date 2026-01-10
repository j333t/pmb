# Why PlusMinusBang?

Understanding why PMB exists and what problems it solves.

---

## The Problem

### Reasoning Happens in Your Head

Every day you make decisions – some small, some life-changing. You weigh options, consider tradeoffs, and arrive at conclusions. But most of this reasoning stays in your head.

When you write things down, you lose:
- **The full context** of why you thought something
- **How your thinking evolved** over time
- **What information changed your mind**
- **The tradeoffs you considered**

Weeks or months later, you remember your conclusion but **make up the reasoning** that led there.

### Writing Is Too Slow

The natural alternative is complete, long-form prose. But good writing is tedious. It takes time to craft sentences, structure paragraphs, and maintain flow.

So you don't do it. Or you write brief notes that are cryptic six months later.

### Traditional Pros/Cons Lists Fall Short

You might make a simple pros/cons list:

**Pros:**
- Benefit 1
- Benefit 2

**Cons:**
- Risk 1
- Risk 2

But this is too flat. Real reasoning has nuance:
- Every pro has limitations
- Every con has mitigations
- Some things are critically important
- Some things are open questions

Traditional lists can't capture this complexity without becoming unwieldy.

---

## The PlusMinusBang Solution

### Simple Symbols, Deep Structure

PMB uses single characters at the start of lines:
- `+` for points that support
- `-` for points that oppose
- `!` for critical information
- `?` for open questions
- And a few more for specific needs

This is **fast to write** (just one character) but **rich in meaning**.

### Nesting Captures Complexity

Every point can have counterpoints nested underneath:

```
- High upfront cost
  + But amortizes over 5 years
    ! Only if usage stays above 60%
      ? What's our historical usage trend?
```

This creates **argument trees** that preserve nuance without becoming essays.

### Time Shows Evolution

By dating your updates and never deleting old thoughts, you create a **reasoning history**:

```
Should I expand the business? 2024-08-01
+ Strong demand signal
- Requires $300k investment

2024-08-15
* Talked to others who expanded–they all said "systemize first"
! We don't even have training docs yet
Decision: Pause. Spend 6 months documenting systems first.
```

Your future self can see exactly how and why you changed your mind.

---

## What PMB Gives You

### 1. Reasoning Archaeology

You can reconstruct past thinking accurately. When someone asks "why did we decide X?", you have receipts–not invented memories.

**Example:** Six months after declining a partnership, you remember exactly why:
```
2024-06-15 - Partnership with Company X
+ Could expand market reach
- Required exclusivity clause
! Discovered they had pending lawsuit (unreported)
Decision: Hard pass
```

Without PMB, you'd vaguely remember "something felt off."

### 2. Transparent Thinking

Make your reasoning visible to:
- **Your future self** - remind yourself why you decided
- **Your team** - show your thought process
- **Stakeholders** - demonstrate due diligence
- **Your successor** - transfer institutional knowledge

PMB turns invisible thought into visible structure.

### 3. Pattern Recognition

When you mark recurring mistakes with `[EXP]`, you can search for patterns:

```
[EXP: Third time I've hired based on charisma over competence]
```

This transforms experience into **learnable lessons** instead of vague intuition.

### 4. Faster Evolution

Learn from your reasoning patterns:
- Which assumptions repeatedly fail?
- Where are you systematically overconfident?
- What kinds of information actually change your mind?

You get better at thinking by seeing how you think.

### 5. Better Execution

Make decisions based on complete context, not vague recollection. When you revisit a decision, you know:
- What you knew then
- What you didn't know then
- What assumptions you made
- What you'd do differently

This prevents repeated mistakes and wasted time re-arguing settled questions.

### 6. Portability

PMB works everywhere:
- Paper notebooks
- Plain text files
- Any outliner (Workflowy, Roam, Logseq, Obsidian)
- WhatsApp messages to yourself
- Code comments
- Meeting notes
- Email

No special software required. Just symbols and indentation.

### 7. Convert Intuition to Reason

When you have a "gut feeling," PMB forces you to articulate it:

**Vague:** "This partnership feels wrong"

**Clear:**
```
~ This partnership feels off
? What's causing this feeling?
- Their CEO dodged questions about funding
- Timeline seems artificially urgent
! They haven't shared customer references despite promises
* Pattern: High-pressure tactics usually mean something's wrong
```

Your intuition becomes actionable.

### 8. Avoid Making Up Reasons

Sometimes your mind fills gaps in reasoning with explanations that sound plausible but aren't grounded in evidence. This is called **confabulation**–your brain creating coherent stories even when the facts are missing.

PMB forces you to label uncertainty:
```
? I don't know this
~ I'm uncertain about this
! This is an assumption
```

Instead of inventing confident-sounding reasons, you mark what you actually don't know.

### 9. Scales With Complexity

Simple decisions need only `+ - !`:
```
Lunch options
+ Close by
- Expensive
```

Complex decisions can nest deeply:
```
Acquisition decision
+ Strategic fit
  - But culture clash risk
    ! Need to interview 10+ employees first
      ? Can we do this before deadline?
        - Deadline is in 2 weeks
          + But maybe we can negotiate extension
            ? Should we ask for 30 or 60 days?
```

The system grows with your needs without becoming unwieldy.

---

## Who Benefits Most?

### Decision Makers
Founders, executives, product managers evaluating high-stakes tradeoffs. PMB captures the reasoning that justifies major decisions.

### Teams & Organizations
Shared reasoning prevents:
- Re-arguing settled debates
- Knowledge loss when people leave
- Confusion about past decisions
- Misalignment on priorities
- Audit trails for heavily regulated industries

PMB creates institutional memory.

### Knowledge Workers
Anyone whose job is "thinking for a living". PMB turns thought into reusable knowledge.

### Students & Learners
Learning to structure arguments, evaluate evidence, and think critically. PMB makes the process explicit and teachable.

### Therapists & Coaches
Helping clients examine beliefs, challenge assumptions, and see patterns in their thinking.

### Researchers
Tracking evidence for/against hypotheses, noting confidence levels, identifying gaps in knowledge.

---

## Real-World Use Cases

### Strategic Decisions
```
Should we pivot our product strategy?
+ Market research shows demand
+ Competitors moving this direction
- Would delay roadmap 6 months
  ! We have 8 months runway left
    - That's cutting it close
      ? Can we raise bridge round?
! Key assumption: New direction has better unit economics
  ? Need to model this before deciding
```

### Hiring Decisions
```
Candidate: Alex - 2024-11-15
+ Strong technical skills
+ Culture fit in interviews
- Overqualified for role (might leave quickly)
  ? Can we offer equity to retain?
! No management experience but applying for lead role
  - Would need heavy mentoring
    + But Sarah could mentor
      ? Is Sarah willing to take this on?
```

### Investment Analysis
```
Stock: TechCo - 2024-12-10
+ Strong revenue growth (40% YoY)
+ Expanding margins
- High P/E ratio (85x)
  + But justified if growth continues
    ! Assumes no competition
      - Three well-funded competitors launched this year
        * Market might be more competitive than assumed
~ Gut feeling: Overvalued but momentum could continue
? Set price alert at $120 to reconsider?
```

### Daily Reflection
```
Week of 2024-12-09
+ Shipped feature X ahead of schedule
+ Good 1-on-1 with Sarah, alignment on Q1
- Spent too much time in meetings (22 hours)
  ! Need to block focus time
    * Try: No meetings Tues/Thurs mornings
? Why am I avoiding the Y project?
  ~ Feels overwhelming, not sure where to start
    * Maybe break it into smaller pieces first
```

---

## Why Not Just Use...?

### "Why not just use regular notes?"

Regular notes don't force structure. You write paragraphs that are hard to scan later. PMB makes patterns instantly visible.

### "Why not just use tags like #pro #con?"

Tags come after the text and require extra typing. PMB's start-of-line symbols are faster to write and easier to scan.

### "Why not just use a spreadsheet?"

Spreadsheets are good for tabular comparisons but terrible for nested reasoning. You can't show how thoughts relate to each other.

### "Why not just think really hard?"

Thinking hard is great! But without externalizing your reasoning:
- You forget why you decided things
- You can't share your thought process
- You can't learn from your patterns
- You invent reasons after the fact

### "Why not just use SWOT analysis / decision matrices / other frameworks?"

Those frameworks are great for specific use cases. PMB is more general-purpose and flexible. You can even use PMB *within* those frameworks.

---

## The Bigger Picture

### PMB Is Like HTML for Thinking

HTML structures content for computers to render. PMB structures reasoning for humans to understand.

Both are:
- Simple markup systems
- Human-readable in plain text
- Platform-agnostic
- Composable and nestable

### From Individual to Institutional

PMB starts as a personal thinking tool but scales to teams and organizations:

**Individual:** Decide better, learn faster, avoid repeated mistakes

**Team:** Share context, align on priorities, preserve knowledge

**Organization:** Institutional memory, decision auditing, knowledge management

**Society:** Transparent reasoning, better public discourse, accountable decisions

---

## The Bottom Line

**PMB solves the fundamental problem: reasoning is invisible.**

By making reasoning visible, you:
- Make better decisions
- Learn from experience
- Share knowledge effectively
- Avoid making up reasons
- Build on past thinking

All with just a few symbols and plain text.

**The goal isn't perfect notation–it's better thinking.**

---

## Possibilities It Opens Up

### For AI Systems

PMB is the perfect format for LLMs to record their reasoning:

**Current problem:** AI reasoning is opaque. You get an answer but can't see how it got there.

**With PMB:** AI can show its work:
```
Question: Should we prioritize feature A or B?

Analyzing feature A:
+ Addresses top user request (500+ votes)
+ Technical complexity: low
- Revenue impact: indirect
  ! Assumes users convert after getting this feature
  ? Conversion rate unknown - need data

Analyzing feature B:
+ Direct revenue driver ($200k ARR potential)
- Technical complexity: high (3-4 months)
  ? Do we have the right team expertise?
! Competitive pressure - 2 competitors launched similar features

* Insight: Feature B has higher stakes but higher uncertainty
Recommendation: Start with A, validate conversion hypothesis, then prioritize B
```

This makes AI:
- **More transparent** - you can see the reasoning, not just the answer
- **Easier to audit** - identify flawed assumptions or missing considerations
- **Better at collaborating** - humans can add their own reasoning to the thread
- **Able to improve** - learn from which reasoning patterns lead to good outcomes

### For Human-AI Collaboration

Humans and AI can reason together in the same format:

```
Human: Should we expand to Europe? 2024-12-10
+ Market size: 200M potential users
- Requires local compliance team
  ? What's the actual compliance cost?

AI: 2024-12-10 - Research on EU compliance
+ GDPR compliance: ~$50k setup + $30k/year
! Need data residency (server infrastructure in EU)
  - Additional $100k infrastructure cost
  ? Can we use existing AWS EU regions?
    + Yes - AWS Frankfurt available
      - But latency for some services
* Total cost estimate: $150k setup + $30k/year ongoing
```

The reasoning is interleaved and builds on itself. Each party can see and respond to the other's points.

### For Future Technologies & Applications

**Collective intelligence:** Teams using PMB create shared reasoning databases that new members can query and learn from–institutional memory that actually works.

**Decision audit trails:** For regulated industries, PMB provides compliance-ready documentation of reasoning processes–not just what was decided, but why.

**Knowledge graphs:** PMB documents can be automatically parsed into knowledge graphs showing how concepts, decisions, and reasoning connect across time.

**AI training data:** PMB-formatted reasoning traces are perfect training data for next-generation reasoning AI–structured examples of how humans actually think through problems.

**Mind reading devices:** When we have devices that can accurately capture thoughts directly, PMB could be the format thoughts are recorded in–already structured, already semantic.

---

## Get Started

Ready to try PMB? See:
- **[SPEC.md](SPEC.md)** - Complete syntax reference
- **[GUIDE.md](GUIDE.md)** - How to use PMB effectively
- **[TOOLS.md](TOOLS.md)** - Integrations and scripts
- **[Examples](examples/)** - Real-world usage

Or just start right now:
```
Your decision
+ One reason for
- One reason against
! What's critical
```

That's it. You're using PMB.
