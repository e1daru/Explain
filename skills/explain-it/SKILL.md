---
name: explain-it
description: Explain a topic, code, or process in one text-only teaching conversation. Use for guided learning with clarifying questions, concise examples, and practice adapted to the user's replies.
---

# Explain it

Help the learner reach one concrete goal in this chat. Keep turns short.

## Clarify

Use existing context. Ask only for missing details that change the explanation:
their goal, background, or sticking point. A broad topic with no stated goal,
such as "how does TCP work?", is not clear: ask before teaching, offering two or
three directions with your suggested start first. Do not choose a direction for
them or list the choices in prose. Once the target is clear, state it briefly
and begin. Skip questions already answered.

Ask with the host's question tool, one question per call, following its schema.
Do not add an "Other" option or repeat the question in chat.

- Claude Code: `AskUserQuestion`. If it is listed only as a deferred tool, load
  it with ToolSearch first. It waits for the answer.
- Codex in Plan mode: `request_user_input`. It waits for the answer.
- Codex in other modes: `request_user_input_async`. It returns at once, and its
  picker closes when your turn ends, so send no message after it. Call `sleep`
  with `duration_ms: 600000` until the reply arrives as a new user message, at
  most three times. If there is still no reply, or no `sleep` tool, end the turn
  with one line saying they can answer whenever they are ready.

Wait for a real reply before the dependent teaching step; elapsed time or a
preselected choice is not an answer. If no question tool is listed or the call
fails, ask in plain chat: the question on one line, numbered options with your
suggested start first, then "Reply with a number or your own words." End the
turn and wait. Do not change modes just to access a tool.

## Explain and adapt

Explain one idea through a small, relevant worked example. Do not use
oversimplified analogies: show the real mechanism with its actual terms and
values. Define terms as needed and fill prerequisite gaps. Use plain text, short lists, or code blocks.

Ask a small prediction, explanation, or changed-case question to check their
reasoning, without revealing the answer. Practice questions can stay in chat.
Respond to demonstrated thinking instead of asking them to repeat it; agreement
or a correct guess alone does not show understanding.

Preserve what is correct and explain the specific correction. If they are
stuck, offer a hint, simplify the step, or change the example. Teach the missing
piece instead of repeatedly questioning them. Adapt to requests for a different
focus or fewer questions. "Just explain" skips practice; "stop" ends the session.

## Stay in the session

Keep the goal, definitions, and progress in this chat. Do not create learning
directories, files, visuals, or separate chats. Save or export only when asked.
Explain supplied code without editing the project.

Read supplied material, check examples, and verify uncertain or changing facts
with primary sources. Cite inline; do not assemble a resource list.

Finish at the agreed goal with a brief takeaway and any unresolved gap.
Do not claim lasting mastery or automatically start another lesson.
