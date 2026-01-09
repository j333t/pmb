# pmb
PlusMinusBang - a simple syntax for human reasoning

## Why this is needed
Important decisions and complex reasoning happen largely in our heads. Even when we write things down, we lose:
- The full context of why we thought something
- How our thinking evolved over time
- What information changed our minds
- The tradeoffs we considered

When we look back weeks or months later, we remember our conclusion, but rarely all the reasoning that led there.  
See more reasons and benefits [here](WHY.md). 


## How this works
The fundamental units of reasoning are just points that are for or against a topic. They could have critical information or even open questions. But it all lives in your head. The only option while writing it all down is complete, long-form prose. However good writing is, it gets a bit tedious, so we don't end up doing that. A natural alternative is simply to mark points as good or bad, for or against. 
This can be easily done by adding a single symbol at the begining of any point. Plus for points that support. Minus for points that are against. Exclamation marks or bangs for critical information. The pattern of symbols tells the story. 


## How this helps you
Here are the key benefits: 
- Transparent thinking: Make your reasoning visible to your future self and others
- Reasoning history: See how past-you thought, what you got wrong, what information changed the game
- Version history for thoughts: Track how your understanding evolved over time
- Faster evolution: Learn from your reasoning patterns
- Better execution: Make decisions based on complete context
- Portability: You can do this anywhere you can write, even on paper
- Convert intuition to reason: Force yourself to articulate why you believe something
- Avoid confabulation: Stop inventing reasons for conclusions you've already reached


## How to get started quickly
1. Start a new line with a `+` `-` or `!` and make your point
2. Start a new new line for another point

You can use this anywhere you can write – even on paper!  
See the full [Syntax](SPEC.md) and [Usage Guidelines](GUIDE.md) for more details

**Remember:** The goal isn't perfect notation — it's better thinking. If a symbol doesn't help, don't use it. If you need to break the rules, break them. 

<details>
<summary> Quick Example </summary>

**Before PMB:**  
"I'm thinking about switching jobs. The new one pays more but the commute is rough. They said it's remote-first but I'm not sure. Need to decide by Friday."


**With PMB:**
```
Should I take the new job? [2024-12-10]
+ 40% salary increase
+ Better title and growth opportunity
- 90-minute commute each way
  ! They claim "remote-first" but no written policy
  ? Can I negotiate 4 days remote?
- Leaving great team and projects
  + But learning has plateaued here
! Must decide by Friday or lose offer

2024-12-12 UPDATE
! Asked for written remote policy - they want 4 days in office
Decision: Declining. Commute + false remote promise = deal breaker
```

**Three months later, you remember exactly why you said no.**
</details>


## Core Syntax
### Essential Symbols  
`+` Pro  
Points that support something. Arguments in favor.
Use for: Benefits, advantages, reasons to proceed, evidence supporting a hypothesis.
```
+ Reduces costs by 30%
+ Team has experience with this tech
+ Customer feedback is overwhelmingly positive
```
`-` Con  
Points against something. Arguments opposing.
Use for: Drawbacks, risks, reasons to avoid, evidence contradicting a hypothesis.
```
- Implementation would take 6 months
- Requires hiring 3 new engineers
- Competitor already dominates this space
```
`!` Bang  
Critical information. Usually caveats, warnings, or must-hold assumptions.
Use for: Deal-breakers, constraints, non-negotiable requirements, critical dependencies.
```
! Must launch before Q4 or we miss the market window
! Assumes AWS pricing stays flat (high risk)
! Regulatory approval required in EU
```
See [SPEC.md](SPEC.md) for complete syntax, guidelines, and examples.

## Who is this for?
### Primary Users
- Decision makers: Founders, executives, product managers evaluating complex tradeoffs everyday
- Organisations: Collect and collate knowledge across teams and departments, while reducing dependence on individuals
- Knowledge workers: Anyone whose job is "thinking for a living". Convert information to intelligence
- Researchers & analysts: Tracking evidence for/against hypotheses
- Consultants: Build expertise that you can package easily
- Therapists & coaches: Helping clients examine thoughts from multiple angles
- Students: Learning to think critically and structure arguments

### Use Cases
- Reasoning AI models: Claude, GPT, and future LLMs benefit from structured reasoning traces
- Team collaboration: Making implicit debates explicit in shared documents
- Teaching: Showing students how experts actually think through problems
- Journalism: Tracking claims and counterclaims during investigation

See more advantages and use cases [here](WHY.md). 


---


## Version
Current: v1.0

## License
Released under [CC0](LICENSE) - public domain. Use freely.

## Community
**Share your usage**: [Join the discussion](https://github.com/j333t/pmb/discussions) to see how others are using PMB and share your own examples.
**Questions or suggestions?** [Open an issue](https://github.com/j333t/pmb/issues/new)
   
## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) to propose changes.





🔥
