# Examples

Real shapes of PMB across different situations. None of these are tidy — that's
the point. Notice how often the useful line is the one admitting something.

Watch the difference between `!` and `*`. `!` is worth your attention but could
still move. `*` will not move whatever anyone decides.

Syntax: [pmb.md](../pmb.md) · Guidance: [GUIDE.md](../GUIDE.md)

---

## The thing you keep putting off

```pmb
The shoulder [2026-01-12]
- Hurts every morning now, not just after the gym
  ~ Started in October? Can't actually remember.
+ It's manageable. I can still work.
! I have said "it's manageable" for three months straight
? What does it cost me to just get it scanned
  - A morning, and some money
    Which is nothing next to what I'm actually afraid of
~ I don't want to know

[2026-02-02]
Scanned. Small tear. Physio, eight weeks, no surgery.
The waiting was the expensive part. Not the scan.
[EXP] I delay medical things until they decide for me
```

---

## Should I quit

```pmb
Should I quit? [2026-04-01]
- No offer in hand
  ! Six months of savings. That's the whole runway.
+ I've stopped learning anything here
+ I dread Sunday evenings
  ~ Is that the job, or is that me
- New manager starts next month, might fix it
  ? How long do I give them
    Two months. Writing the date down now, while I'm honest.

[2026-06-01]
New manager is genuinely good. Sundays feel exactly the same.
So it was never the manager.
Decision: start looking. Quietly, savings intact.
```

---

## Money, and the reason under the reason

```pmb
Buy the used car or keep repairing? [2026-05-20]
+ This repair is only ₹8,000
  - Fourth one this year
    ! ₹35,000 in repairs on a car worth ₹90,000
+ I know this car's problems
- Replacement is ₹4.2L, needs a loan
  ? What's the EMI actually
    ₹9,400 a month for four years
      ! More per month than I have ever spent on repairs
  * Loan needs two years of ITRs. I have one.
    - So this isn't even available until next July
~ I want the new car for reasons I'm not putting on this list
  Name them or drop them.
    - I'm embarrassed picking up clients in this one
      + That's a real reason. It just needed saying out loud.
      ! It's also not worth ₹4.2L. Rent one for client days.
```

The `*` ends the argument on its own — everything above it was moot until the
paperwork exists. That's the difference between `*` and `!`.

---

## A team decision, and what it missed

```pmb
Ship the redesign now, or wait for Q3? [2026-02-10]
! Support is drowning — 40% of tickets are about the old nav
+ Design is done, tested with 12 users
- Engineering says 3 weeks, which historically means 5
  + Even 5 lands before Q3
? What breaks if we're wrong
  - Worst case we roll back. We've done it before.
    + So the downside is bounded and the upside isn't
Decision: ship. Rollback plan written before we start.

[2026-03-25]
Shipped in 4 weeks. Nav tickets down 60%.
- Signups dipped 8% for a fortnight
  Nobody predicted that. We measured the thing we changed.
  [EXP] We always test what we touched, never what sits next to it
```

---

## Weighing evidence

```pmb
Does a 4-day week actually work? [2026-03-01]
+ Iceland trial: no productivity drop, 2,500 workers
  ! Public sector only — different incentives entirely
+ UK pilot 2022: 92% of firms carried on afterwards
  ? Who self-selected into that pilot
    - Firms already inclined to make it work
      ! So the headline number may not transfer anywhere
- No long-run data past about two years, in any study
~ Every study measures output. None measure what quietly got dropped.
? Wrong question — not "does it work" but "for which kind of work"
? Which roles even have output measurable at a weekly grain
```

---

## Reasoning with an AI in the same document

PMB lets a person and a model add to one thread instead of trading paragraphs.
Each side can see, and argue with, the other's actual reasoning.

```pmb
Move off the managed database? [2026-06-02]
- Bill has tripled in 18 months
+ Zero ops time from us today
  ! Nobody on the team has run a database in production

AI [2026-06-02] — ran the cost comparison
+ Self-hosted equivalent: ~$400/mo infra against $2,100 today
- Add ~$1,500/mo of engineer time, at 20% of one person
  ! So the real saving is ~$200/mo, not $1,700
    - That's inside the noise of your current growth rate
* Your DPA commits you to EU data residency until March 2028
  - Self-hosting means owning that obligation yourself
? Is the pain the bill, or something else

[2026-06-03]
The bill was never the problem. The problem is that I can't
explain the bill to the board.
Decision: stay. Write the one-pager instead.
```

---

## An SOP, with the immovable parts marked

Not every use is a decision. In a procedure, `*` marks what is fixed by
contract, law or licence, and `!` marks what people get wrong. The reader's eye
lands on both before they start.

```pmb
SOP: onboarding a new client [2026-04-01]
1. Send the welcome pack within 24 hours
   * Contract must be signed before anything else goes out
2. Book the kickoff call
   * Never before the deposit clears — this is in the MSA, not our policy
   ? If they push for an earlier call, who can approve it
     Nobody. See above.
3. Set up the shared folder
   Use the template. Don't build one from scratch.
   * Client data stays in the India region. DPA clause 7.
4. Add them to the monthly report list
   ! Miss this and they get invoiced without a report. Happens.
   [EXP] Caused two of our last three billing disputes
```

Numbered steps carry the procedure. `*` carries what you are not allowed to
change. `!` carries what people keep getting wrong.

---

## A monthly review

The lightest possible use — two symbols, nothing else. Most people who write
PMB never need more than this.

```pmb
Anaya - March [2026-03-31]
+ Took over the Kohli account with no handover and kept it steady
+ Asks for help early now, which is new
- Two deadlines moved without telling anyone
  ! The client heard it from them, not from us
- Still waits to be assigned work
? What would it take to have her run a project end to end
```

---

## Add your own

PMB is public domain. Send an example that shows a shape these don't —
[open a PR](https://github.com/j333t/pmb/pulls) or
[start a discussion](https://github.com/j333t/pmb/discussions).
