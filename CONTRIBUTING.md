# Contributing to PlusMinusBang

Thank you for your interest in improving PMB! This notation system is designed to be simple, stable, and useful. Your contributions help make it better for everyone.

---

## How to Contribute

### 1. Share Your Usage

The best contribution is **using PMB and sharing what you learn:**

- Post examples of how you use it
- Write blog posts or tutorials
- Share templates for specific use cases (hiring decisions, product evaluations, research notes)
- Build tools and integrations

No permission needed–PMB is public domain. Just use it and tell others!

### 2. Report Issues

Found something unclear or confusing in the spec? [Open an issue](https://github.com/j333t/pmb/issues/new).

**Good issues include:**
- What you were trying to do
- What was confusing or didn't work
- How you think it could be improved

### 3. Suggest Improvements

Have an idea for improving PMB? Great! Here's how to propose it:

**Before opening a PR:**
1. [Open an issue first](https://github.com/j333t/pmb/issues/new) describing your proposal
2. Explain the problem it solves
3. Show examples of how it would work
4. Discuss with the community

**After discussion:**
1. Fork the repository
2. Make your changes
3. Submit a pull request referencing the issue

---

## What We're Looking For

### ✅ Welcome Contributions

- **Clarifications**: Making the spec easier to understand
- **Examples**: Real-world usage showing PMB in action
- **Tools**: Plugins, scripts, integrations for different platforms
- **Translations**: PMB spec in other languages
- **Templates**: Starter documents for common use cases
- **Fixes**: Typos, broken links, formatting issues

### ⚠️ Needs Strong Justification

- **New symbols**: PMB is intentionally minimal. New symbols need to solve problems the existing ones can't.
- **Syntax changes**: Changes to core notation require broad consensus
- **Breaking changes**: We avoid these unless absolutely necessary

### ❌ Not Accepting

- Changes that significantly increase complexity without clear benefit
- Symbols that overlap with existing ones
- Features that make PMB platform-specific
- Prescriptive rules that reduce flexibility

---

## Design Principles

When proposing changes, consider these principles:

**Simplicity over completeness**  
PMB doesn't need to handle every edge case. It needs to be easy to learn and remember.

**Text-first**  
PMB works in any plain text editor. Don't add features that require special tools.

**Human-readable**  
The notation should be obvious even without syntax highlighting or special rendering.

**Flexible, not rigid**  
PMB is a tool for thinking. People should feel free to adapt it, not constrained by rules.

---

## Process for Major Changes

### 1. Proposal (Issue)

Open an issue with:
- **Problem statement**: What need are you addressing?
- **Proposed solution**: How would it work?
- **Examples**: Show it in action
- **Alternatives considered**: What else did you think about?

### 2. Discussion

The community discusses:
- Does this solve a real problem?
- Does it fit PMB's design principles?
- Are there simpler alternatives?
- What are the tradeoffs?

### 3. Decision

Final editorial control rests with the maintainer to keep the spec coherent and focused. Decisions consider:
- Community feedback
- Alignment with design principles
- Impact on existing users
- Long-term maintainability

### 4. Implementation (PR)

If approved:
- Update relevant documentation
- Add examples showing the change
- Update version number if needed
- Document in CHANGELOG.md

---

## Pull Request Guidelines

**Good PRs:**
- Reference an existing issue
- Make one logical change
- Include before/after examples
- Update all relevant documentation
- Follow existing formatting style

**PR checklist:**
- [ ] Referenced issue number in description
- [ ] Updated SPEC.md if syntax changed
- [ ] Added examples if introducing new features
- [ ] Updated CHANGELOG.md
- [ ] Spell-checked and proofread

---

## Documentation Style

When writing or updating docs:

- **Be concise**: One idea per sentence
- **Show, don't just tell**: Include examples
- **Write for humans**: Avoid jargon and unnecessary formality
- **Use active voice**: "Start each line with a symbol" not "Each line should be started with a symbol"
- **Format consistently**: Follow existing markdown style

---

## Tool Development

Building a PMB tool? Awesome! Here's what helps:

**Tell us about it:**
- Open an issue or PR to add your tool to the README
- Include a brief description and link

**Design guidelines:**
- Support the core syntax (`+ - ! ?`) at minimum
- Make extended syntax optional
- Don't lock users into your tool–export to plain text
- Follow the spec, but feel free to add tool-specific features

**Suggested integrations:**
- Workflowy, Roam, Logseq, Obsidian (outliners/PKM tools)
- VS Code, Sublime, Vim (code editors)
- Notion, Confluence (collaboration platforms)
- Mobile note apps

---

## Community Guidelines

**Be kind**  
We're all trying to think better. Assume good intentions and treat others with respect.

**Be constructive**  
If you disagree with something, explain why and suggest alternatives.

**Be patient**  
Not everyone has the same context or experience. Help people understand.

**Be open**  
Your way of using PMB might not be everyone's way. That's okay–flexibility is a feature.

---

## Questions?

- **General questions**: [Open a discussion](https://github.com/j333t/pmb/discussions)
- **Bug reports**: [Open an issue](https://github.com/j333t/pmb/issues/new)
- **Feature requests**: [Open an issue](https://github.com/j333t/pmb/issues/new) with your proposal

---

## License

By contributing to PMB, you agree that your contributions will be released under the same CC0 (public domain) license as the project.

---

**Thank you for helping make thinking better for everyone!** 🧠✨
