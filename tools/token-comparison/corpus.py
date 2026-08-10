"""Three documents, each written three ways, with the claim set held constant.

Format 2 (plain bullets) is the honest competitor. It already strips the
connective language, so comparing PMB against flowing prose alone overstates
the case. Document C is a control: a status report is nearly all fact and
almost no scaffolding, so PMB should gain little on it. If PMB wins big
everywhere including C, the corpus is rigged.
"""

A_PROSE = """We are considering opening a second location, and on balance the case for
waiting looks stronger than the case for moving now.

There are real reasons to expand. The current location runs at about 95%
capacity, and we turn away roughly forty people from the waitlist every week.
That is demand we are visibly failing to serve.

The main obstacle is capital. The build-out needs 30 lakh upfront. We do have
45 lakh in savings, so the money exists, but I want to preserve six months of
runway, which is about 11 lakh at our current burn. I had hoped we could phase
the payments to protect that buffer, but the landlord has confirmed he will not
phase anything.

The lease terms are a hard constraint rather than a negotiating position: it
runs three years with no exit clause. Separately, the FSSAI licence must be
issued before we can trade for a single day, so there is no way to open
provisionally and regularise later.

Finally there is my own bandwidth. A second site would split my attention, and
I am already working seventy-hour weeks.

Given all of this, my inclination is to hold for three months and look for a
smaller unit on the same street."""

A_BULLETS = """Should we open a second location?

- Current location runs at about 95% capacity
- We turn away roughly forty people from the waitlist every week
- Build-out needs 30 lakh upfront
  - We have 45 lakh in savings
  - But I want to keep six months of runway, about 11 lakh at current burn
    - Hoped to phase the payments; the landlord has confirmed he will not
- The lease runs three years with no exit clause, and cannot be negotiated
- The FSSAI licence must be issued before we can trade for a single day
- A second site would split my attention
  - I am already working seventy-hour weeks

Decision: hold three months and look for a smaller unit on the same street."""

A_PMB = """Open the second location?
+ Runs at 95% capacity
+ 40-odd people on the waitlist every week
- Needs 30 lakh upfront
  + We have 45 lakh saved
  ! Want six months of runway, about 11 lakh at current burn
    ? Can we phase the payments
      ! Landlord won't phase anything
* Lease is three years, no exit clause
* FSSAI licence must be issued before we trade a single day
- Splits my attention
  ! Already at 70-hour weeks
Decision: hold three months, look for something smaller on the same street."""

A_CLAIMS = 11

B_PROSE = """The evidence on intermittent fasting for longevity is mixed and mostly
indirect.

On the supportive side, a 2023 meta-analysis reports improved metabolic
markers, and animal studies have shown lifespan extension in the range of
20 to 30 percent. That second result needs care, though, because mice are not
humans and rodent lifespan findings have often failed to transfer.

Against that, the human randomised controlled trials we have are all
short-term, none running longer than about two years, and I have not been able
to find any study following participants for ten years or more.

My own experience is that I feel better when fasting, but I cannot rule out
placebo.

Reading all of this back, I think the question is wrongly framed. The useful
question is not whether it works, but for whom, and under what conditions."""

B_BULLETS = """Does intermittent fasting work for longevity?

- A 2023 meta-analysis reports improved metabolic markers
- Animal studies show 20-30% lifespan extension
  - But mice are not humans, and rodent findings often fail to transfer
- Human RCTs are all short-term, none longer than about two years
  - I could not find any study following participants for ten years or more
- Personally I feel better when fasting, but this could be placebo

The question may be wrongly framed: not whether it works, but for whom and
under what conditions."""

B_PMB = """Does intermittent fasting work for longevity?
+ Meta-analysis shows improved metabolic markers [2023]
+ Animal studies show 20-30% lifespan extension
  ! Mice aren't humans; rodent findings often fail to transfer
- Human RCTs are all short-term, none beyond two years
  ? Any study following participants ten years or more
~ I feel better fasting, but that could be placebo
Not whether it works, but for whom and under what conditions."""

B_CLAIMS = 7

C_PROSE = """Sprint 14 closed on Friday with 23 of the 26 tickets completed. The
authentication rewrite was merged and is currently sitting behind a feature
flag. Search indexing did not make it and has moved to the next sprint.

Two engineers are out next week. The staging deploy is scheduled for Tuesday,
Postgres on staging has been upgraded to version 16, and the load test is set
for Thursday."""

C_BULLETS = """Sprint 14 status

- Closed Friday, 23 of 26 tickets completed
- Authentication rewrite merged, behind a feature flag
- Search indexing moved to the next sprint
- Two engineers out next week
- Staging deploy scheduled for Tuesday
- Postgres on staging upgraded to version 16
- Load test set for Thursday"""

C_PMB = """Sprint 14 status
Closed Friday, 23 of 26 tickets completed
Authentication rewrite merged, behind a feature flag
Search indexing moved to the next sprint
Two engineers out next week
Staging deploy scheduled for Tuesday
Postgres on staging upgraded to version 16
Load test set for Thursday"""

C_CLAIMS = 8

DOCS = [
    ("A. Deliberation (second location)",   A_CLAIMS, A_PROSE, A_BULLETS, A_PMB),
    ("B. Evidence notes (fasting)",         B_CLAIMS, B_PROSE, B_BULLETS, B_PMB),
    ("C. Status report (sprint) [control]", C_CLAIMS, C_PROSE, C_BULLETS, C_PMB),
]
