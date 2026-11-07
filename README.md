# Textbook-it

Understand unfamiliar code, concepts, and processes through a concise question, one worked example, and a useful visual.

**Start with [textbook-it](skills/textbook-it/SKILL.md).** It builds on the B2 visual walkthrough and chooses among seven optional teaching guides. It can also give a short prose explanation when a visual would add work.

**[Download textbook-it](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it.zip)** · **[Download released versions](https://github.com/e1daru/textbook-it/releases/latest/download/all-skills.zip)** · **[Browse releases](https://github.com/e1daru/textbook-it/releases)**

## Explain it

**[Read the skill](skills/explain-it/SKILL.md)** · **[Testing prompts and feedback sheet](docs/explain-it-trials.md)**

`explain-it` teaches in one text-only chat session. It clarifies your goal and background, explains one idea through a small example, and adjusts to your replies. If your request is already clear, it starts immediately. Say “just explain” to skip practice questions.

Clarification uses the host's question tool, one question at a time, waiting for your answer. Plain chat is the fallback when no suitable tool is available or permitted. Practice questions can stay in chat.

Everything stays in the conversation: no learning directory, resource files, or generated visuals. The skill itself is one `SKILL.md` file.

Install the renamed skill from an updated clone:

```bash
python3 scripts/install.py --host both --skill explain-it
```

You can also copy `skills/explain-it/` into `~/.claude/skills/` or `~/.agents/skills/`. If you previously installed `teach-it`, remove that old skill folder after installing `explain-it` to avoid duplicate choices.

In Claude Code:

```text
/explain-it Help me understand why two Python variables can share one list.
```

In Codex, use `$explain-it` with the same request.

## Skill catalog

Every individual download contains a complete skill folder, including its supporting files.

| Skill | Approach | Status | Download |
|---|---|---|---|
| [explain-it](skills/explain-it/SKILL.md) | Clarifying questions, short text explanations, and practice in one chat | Single-session teaching skill | [Install from clone](#explain-it) |
| [textbook-it](skills/textbook-it/SKILL.md) | Goal-first explanation with seven optional strategy guides | Current main version | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it.zip) |
| [textbook-it-b2](skills/textbook-it-b2/SKILL.md) | A compact visual carries the walkthrough | Preferred baseline from user review | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-b2.zip) |
| [textbook-it-b1](skills/textbook-it-b1/SKILL.md) | Concise, sequential worked steps | Experimental alternative | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-b1.zip) |
| [textbook-it-b3](skills/textbook-it-b3/SKILL.md) | Worked example with a matched contrast | Experimental alternative | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-b3.zip) |
| [textbook-it-a](skills/textbook-it-a/SKILL.md) | Build intuition from a concrete situation | Early prototype | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-a.zip) |
| [textbook-it-b](skills/textbook-it-b/SKILL.md) | Explain a method through consequential steps | Early prototype | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-b.zip) |
| [textbook-it-c](skills/textbook-it-c/SKILL.md) | Explain the central mechanism concisely | Early prototype | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-c.zip) |

Use `textbook-it` for a complete explanation in one response, or `explain-it` for interactive teaching. You do not need to install every alternative.

## Install in Claude Code

Download and unzip `textbook-it.zip`, then put the complete `textbook-it` folder inside `~/.claude/skills/`:

```text
~/.claude/skills/textbook-it/
├── SKILL.md
└── references/
    ├── state.md
    ├── process.md
    ├── quantities.md
    ├── contrast.md
    ├── space.md
    ├── structure.md
    └── derivation.md
```

Then use it in Claude Code:

```text
/textbook-it Explain why two Python variables can refer to the same list.
```

Personal skills apply across local projects. For a project-only installation, use `.claude/skills/` inside that project. See [Claude Code's skill documentation](https://code.claude.com/docs/en/skills).

## Install in Codex

Place the same complete folder inside `~/.agents/skills/` for a personal installation, or `.agents/skills/` inside a project. Invoke it with:

```text
$textbook-it Explain why a low Sun makes a longer shadow.
```

If the skill does not appear, start a new Codex session. See [OpenAI's local skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Install from a clone

With Git and Python 3 installed:

```bash
git clone https://github.com/e1daru/textbook-it.git
cd textbook-it
python3 scripts/install.py --host both
```

Use `--host claude` or `--host codex` for one application. To install another version:

```bash
python3 scripts/install.py --host claude --skill textbook-it-b2
```

The installer copies the complete folder, uses no external Python packages, and refuses to overwrite a different existing installation. Identical installations are left as they are. To replace an older copy, first move that copy out of the host's skills directory, then run the installer again.

## How it chooses an explanation

| Reader's difficulty | Guide | Example |
|---|---|---|
| What changes or persists? | [State](skills/textbook-it/references/state.md) | Two names pointing to one object |
| What happens next, and why? | [Process](skills/textbook-it/references/process.md) | A thermostat decision loop |
| Which group or quantity matters? | [Quantities](skills/textbook-it/references/quantities.md) | The fragile share among marked packages |
| What distinguishes two ideas? | [Contrast](skills/textbook-it/references/contrast.md) | Identity versus permission |
| Where are things, or how do they move? | [Space](skills/textbook-it/references/space.md) | Motion and inward pull |
| How do the parts fit together? | [Structure](skills/textbook-it/references/structure.md) | Chapters, contents, and an index |
| Why does a mathematical step work? | [Derivation](skills/textbook-it/references/derivation.md) | Preserving an equation's equality |

These are optional strategies, not seven sections added to every answer. The main skill reads a guide when it helps with the question, follows one example, and stops when the question is answered.

You can add constraints to your request, such as “I know basic Python,” “use no formulas,” or “explain in two sentences.” For guided practice, explicitly ask it to teach one step at a time.

## Development and evidence

B2 was preferred in user review. The current modular version was compared with B2 on three matched questions using fresh medium-effort agents, plus a short-answer constraint check. The code and arithmetic were checked; this small evaluation does not establish a learning advantage or reliability across all topics. Claude Code installation compatibility is separate from testing teaching quality on Claude.

The design draws on [the Agent Skills format](https://agentskills.io/specification), [Anthropic's open-source skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), and [IES guidance on worked examples and visual explanations](https://ies.ed.gov/ncee/wwc/PracticeGuide/1). The seven-guide organization is a design choice to refine through use.

`explain-it` has file-format validation but still needs real learner trials. See the [source notes and trial protocol](docs/explain-it-trials.md) for its design background and evaluation limits.

To rebuild the downloadable archives:

```bash
python3 scripts/package.py
```

The output includes one ZIP per skill, `all-skills.zip`, and `SHA256SUMS.txt` in `dist/`. Local evaluation logs and machine-specific files are excluded from the published repository and packages.
