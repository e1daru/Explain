# Textbook-it

Understand unfamiliar code, concepts, and processes through a concise question, one worked example, and a useful visual.

**Start with [textbook-it](skills/textbook-it/SKILL.md).** It builds on the B2 visual walkthrough and chooses among seven optional teaching guides. It can also give a short prose explanation when a visual would add work.

**[Download textbook-it](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it.zip)** · **[Download all versions](https://github.com/e1daru/textbook-it/releases/latest/download/all-skills.zip)** · **[Browse releases](https://github.com/e1daru/textbook-it/releases)**

## New: three question-led versions

These experimental skills adapt the questioning approach in [Matt Pocock's Grill Me / grilling](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grilling/SKILL.md) for learning. Each asks one focused question, waits for your answer, and uses it to decide what to explain next. Each is self-contained and works without installing the main skill.

| Version | How it finds the missing link | Download |
|---|---|---|
| [textbook-it-probe](skills/textbook-it-probe/SKILL.md) | Asks a diagnostic question, then explains the gap your answer reveals | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-probe.zip) |
| [textbook-it-predict](skills/textbook-it-predict/SKILL.md) | Shows a small example or visual and asks you to predict what changes | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-predict.zip) |
| [textbook-it-teachback](skills/textbook-it-teachback/SKILL.md) | Starts with your own explanation and repairs a missing or mistaken connection | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-teachback.zip) |

**[Download just these three](https://github.com/e1daru/textbook-it/releases/latest/download/question-led-skills.zip)** · **[Testing prompts and feedback sheet](docs/question-led-trials.md)**

Try **predict** first if you liked B2's visual walkthrough. This is a design recommendation; the new variants have not yet been tested with learners. Say “just explain” at any point to switch to a direct explanation.

For Claude Code, invoke `/textbook-it-probe`, `/textbook-it-predict`, or `/textbook-it-teachback`. For Codex, use the same name with `$` in place of `/`. Installation uses the same folders described below. From an updated clone, install all three with:

```bash
python3 scripts/install.py --host both --skill textbook-it-probe
python3 scripts/install.py --host both --skill textbook-it-predict
python3 scripts/install.py --host both --skill textbook-it-teachback
```

## Skill catalog

Every individual download contains a complete skill folder, including its supporting files. The three question-led versions above supplement these seven explanation versions.

| Skill | Approach | Status | Download |
|---|---|---|---|
| [textbook-it](skills/textbook-it/SKILL.md) | Goal-first explanation with seven optional strategy guides | Current main version | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it.zip) |
| [textbook-it-b2](skills/textbook-it-b2/SKILL.md) | A compact visual carries the walkthrough | Preferred baseline from user review | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-b2.zip) |
| [textbook-it-b1](skills/textbook-it-b1/SKILL.md) | Concise, sequential worked steps | Experimental alternative | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-b1.zip) |
| [textbook-it-b3](skills/textbook-it-b3/SKILL.md) | Worked example with a matched contrast | Experimental alternative | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-b3.zip) |
| [textbook-it-a](skills/textbook-it-a/SKILL.md) | Build intuition from a concrete situation | Early prototype | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-a.zip) |
| [textbook-it-b](skills/textbook-it-b/SKILL.md) | Explain a method through consequential steps | Early prototype | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-b.zip) |
| [textbook-it-c](skills/textbook-it-c/SKILL.md) | Explain the central mechanism concisely | Early prototype | [ZIP](https://github.com/e1daru/textbook-it/releases/latest/download/textbook-it-c.zip) |

Use the main version for a complete explanation in one response, or one of the question-led versions for interactive teaching. You do not need to install every alternative.

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

The question-led variants use original instructions inspired by Matt Pocock's concise, adaptive interview workflow. His current `grill-me` delegates to `grilling`, which asks rounds of design questions with recommended answers. Here, one learning question comes at a time, without revealing its answer, and the session ends at the learner's immediate goal. See the [source notes and trial protocol](docs/question-led-trials.md) for the differences and evaluation limits.

To rebuild the downloadable archives:

```bash
python3 scripts/package.py
```

The output includes one ZIP per skill, `question-led-skills.zip`, `all-skills.zip`, and `SHA256SUMS.txt` in `dist/`. Local evaluation logs and machine-specific files are excluded from the published repository and packages.
