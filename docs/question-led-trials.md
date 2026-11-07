# Try the three question-led skills

These are alternatives to compare, not three stages that must run in sequence.

| Skill | Starting point | Typical exchange |
|---|---|---|
| `textbook-it-probe` | A concrete diagnostic question | Your answer → identify the gap → explain it → try a changed case |
| `textbook-it-predict` | One example with an unknown result | Predict → reveal and explain → update the visual → predict a changed case |
| `textbook-it-teachback` | Your explanation of the idea | Explain → clarify or challenge one connection → repair → apply elsewhere |

Use a separate chat for each trial and explicitly invoke one skill. Keep the
model and reasoning setting the same where those controls are available;
medium effort matches the project's earlier comparison setup. Test Claude and
Codex separately and record the model used. These files do not select a model
or set its effort.

The same prompt helps compare style, but learning a topic in one trial makes
later trials easier. Rotate the order across topics and treat your ratings as
personal preferences, not a controlled measurement of learning effectiveness.

## Common prompts

Prefix a prompt with `/textbook-it-probe`, `/textbook-it-predict`, or
`/textbook-it-teachback` in Claude Code. Use `$` instead of `/` in Codex.
Answer naturally; "I don't know" is useful input. Do not read all the skill
instructions before a trial if you want to judge the experience itself.

### Code: shared objects

```text
Help me understand why changing b can affect a here. I know basic Python
assignment and lists, but I am unsure what is shared. Keep it concise and
use questions to work out what I am missing.

a = [1, 2]
b = a
b.append(3)
```

### Physics: shadows

```text
Help me understand why the same upright pole has a longer shadow when the Sun
is lower. Assume level ground. I can follow a simple sketch but do not know
trigonometry. Keep it concise and use questions to work out what I am missing.
```

### Quantities: a flagged group

```text
In an invented batch of 1,000 packages, 10 are damaged. An inspection flags
8 of the damaged packages and 90 of the undamaged packages. Help me understand
which numbers determine the damaged share among flagged packages. I know
fractions but get confused about which group goes on the bottom. Keep it
concise and use questions to work out what I am missing.
```

## What to watch during a trial

- The first question helps locate a specific missing relationship.
- The tutor waits for your actual reply and uses it in its next turn.
- It teaches when you are stuck instead of repeatedly demanding an answer.
- A visual, when used, makes the relationship easier to see.
- A correct guess is not treated as proof that you understand the reason.
- “Just explain” produces a direct explanation; “stop” ends the questioning.
- Once you can use the idea, it finishes without expanding into a course.

These are behaviors to observe, not a claim that every run already passes.
No new learner trial or end-to-end Claude/Codex teaching evaluation has been
run for these three variants. File-format validation and archive checks do
not establish teaching quality.

## Feedback sheet

Use 1–5, with 5 best, or leave a cell blank if you could not judge it. For
“low burden,” 5 means little unnecessary effort or reading. Include one
specific exchange that helped or got in the way.

| Skill / model / topic | Useful questions | Explanation clarity | Visual usefulness, if any | Low burden | Overall preference |
|---|---|---|---|---|---|
| probe / … / … | | | | | |
| predict / … / … | | | | | |
| teachback / … / … | | | | | |

Separately record whether you solved the changed case unaided, with a hint,
after seeing the answer, or did not attempt it. Your preference is the primary
design signal; the changed case provides a small additional check of whether
the explanation helped. Keep these separate rather than inventing one
"success rate" from them.

## Source and adaptation

Reviewed on 2026-11-07 at upstream revision
`4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`:

- [Matt Pocock's Grill Me](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grill-me/SKILL.md) is currently a small entry point to `grilling`.
- [Grilling](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grilling/SKILL.md) adapts rounds of questions as dependent decisions are resolved. It presents recommended answers and aims to resolve the design before action.
- [Teach](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/teach/SKILL.md) is a broader, persistent teaching workspace. Its lesson-file and learning-record workflow is outside these small conversational variants.
- [Wait What](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/wait-what/SKILL.md) asks for an explanation to be rephrased when it does not land.

The three new skills contain original teaching instructions. They borrow the
idea of choosing the next question from the previous answer and the direct
instruction style. For this purpose, they ask one question, avoid giving away
the answer, teach as soon as the gap is clear, and stop at the immediate goal.
They do not require Matt's skills, a glossary, a learning workspace, or a
particular question tool. These adaptations are design hypotheses for user
testing, not findings established by the upstream repository.

The shared `name` / `description` frontmatter and Markdown body follow the
[Agent Skills format](https://agentskills.io/specification). Installation and
invocation guidance is based on [Claude Code's skills documentation](https://code.claude.com/docs/en/skills)
and [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills).
