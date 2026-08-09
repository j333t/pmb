# PMB agent skill

A drop-in skill that teaches an AI agent to read, write, and convert
PlusMinusBang. Public domain — copy it anywhere.

## Claude Code

Install for every project:

```sh
mkdir -p ~/.claude/skills/pmb
curl -o ~/.claude/skills/pmb/SKILL.md https://plusminusbang.com/skill/SKILL.md
```

Or for one project only, commit it to the repo:

```sh
mkdir -p .claude/skills/pmb
curl -o .claude/skills/pmb/SKILL.md https://plusminusbang.com/skill/SKILL.md
```

Then say "pmb this", or just ask for a decision — the skill triggers on its own.

## Claude.ai

Settings → Capabilities → Skills → upload `SKILL.md`.

## Anything else

`SKILL.md` is plain markdown with YAML frontmatter. The body works as-is in:

- A **project instruction** or **custom GPT** — paste the body.
- An **`AGENTS.md`** or **`CLAUDE.md`** — paste the body, or just link it:
  `Reasoning notation: https://plusminusbang.com/pmb.md`
- A **system prompt** — use the smaller single-purpose prompts instead:
  [reader](../prompts/reader.txt), [writer](../prompts/writer.txt),
  [converter](../prompts/converter.txt).

## What it does

**Read** — parses PMB it encounters, and preserves it through edits instead of
flattening it to prose.

**Write** — emits reasoning as a fenced ```pmb block, deal-breakers first,
marking genuine unknowns rather than inventing support for them.

**Convert** — restructures a prose dump without adding reasons you didn't give.
This is the one that removes the blank page.
