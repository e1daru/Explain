# Try explain-it

`explain-it` clarifies the learner's target, then uses short text explanations,
examples, and practice in one conversation. It chooses what helps at the
current step; there are no modes to select or learning files to create.

Use a separate chat for each topic and invoke `explain-it`. When comparing runs,
keep the model and reasoning setting the same where those controls are available;
medium effort matches the project's earlier comparison setup. Test Claude and
Codex separately and record the model used. These files do not select a model
or set its effort.

Learning a topic in one trial makes later trials easier. Treat your ratings
as personal feedback, not a controlled measurement of learning effectiveness.

## Common prompts

Prefix a prompt with `/explain-it` in Claude Code or `$explain-it` in Codex.
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

### Broad topic: clarify first

```text
Teach me about databases. I'm not sure where to start.
```

The first reply should use the host's question tool to help you choose a useful
direction and wait for your answer. If no suitable tool is available or permitted,
it should ask in plain chat. Once the target and enough background are known,
teaching should begin without a long questionnaire. Contrast this with the
specific code prompt above, which already supplies a target and background.

### Physics: shadows

```text
Help me understand why the same upright pole has a longer shadow when the Sun
is lower. Assume level ground. I do not know trigonometry. Use text only, keep
it concise, and use questions to work out what I am missing.
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

- A broad request gets a useful scope question; a sufficiently clear request
  starts the explanation without repeating known information.
- The tutor waits for your actual reply and uses it in its next turn.
- Clarifying questions use the question tool when available and permitted, one
  question per call, without repeating the question in chat. An asynchronous
  prompt stays pending until you answer; a preselected choice is not your reply.
- It teaches when you are stuck instead of repeatedly demanding an answer.
- The example is easy to follow in text, with no generated visuals or documents.
- Goals, definitions, and progress stay in the same chat; no learning directories
  or resource files appear.
- A correct guess is not treated as proof that you understand the reason.
- “Just explain” produces a direct explanation; “stop” ends the questioning.
- Once you can use the idea, it finishes without expanding into a course.

These are behaviors to observe, not a claim that every run already passes.
No new learner trial or end-to-end Claude/Codex teaching evaluation has been
run for this text-only revision. File-format validation and archive checks do
not establish teaching quality.

## Feedback sheet

Use 1–5, with 5 best, or leave a cell blank if you could not judge it. For
“low burden,” 5 means little unnecessary effort or reading. Include one
specific exchange that helped or got in the way.

| Model / topic | Useful questions | Explanation clarity | Example usefulness | Low burden | Overall experience |
|---|---|---|---|---|---|
| … / shared objects | | | | | |
| … / shadows | | | | | |
| … / flagged group | | | | | |

Separately record whether you solved the changed case unaided, with a hint,
after seeing the answer, or did not attempt it. Your preference is the primary
design signal; the changed case provides a small additional check of whether
the explanation helped. Keep these separate rather than inventing one
"success rate" from them.

## Source and adaptation

Reviewed on 2026-11-07 at upstream revision
`4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`:

- [Matt Pocock's Teach](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/teach/SKILL.md) grounds lessons in the learner's purpose, chooses a manageable challenge, and combines explanation with practice and feedback. It also distinguishes immediate performance from long-term retention.
- That skill uses a persistent workspace with HTML lessons, references, resources,
  learning records, and reusable assets. This adaptation keeps teaching in text
  within one chat and does not create that workspace.

`explain-it` contains original teaching instructions. It borrows the
goal-led teaching and feedback principles above, while choosing each next step
from the learner's reply. Clarifying questions establish the target; short
explanations and changed examples help the learner apply it. Any brief recall
happens within the chat, with no revision schedule or claim of lasting mastery.
It does not require Matt's skills, a glossary, or a learning workspace.
Clarification uses the host's question tool, with a plain-chat fallback only
when no suitable tool is available or permitted. These adaptations are design
choices for user testing, not findings established by the upstream repository.

The shared `name` / `description` frontmatter and Markdown body follow the
[Agent Skills format](https://agentskills.io/specification). Installation and
invocation guidance is based on [Claude Code's skills documentation](https://code.claude.com/docs/en/skills)
and [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills).
