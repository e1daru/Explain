---
name: textbook-it
description: Explain unfamiliar concepts, code, and processes with goal-first worked examples and useful visuals. Use when the user asks to understand how or why something works, or invokes textbook-it; not for unrelated implementation or editing requests.
---

# Textbook it

Make the missing relationship understandable with the least unnecessary
reading. Keep the goal-first walkthrough the user prefers, and choose a
representation for the particular obstacle.

## Frame the question

Start with the exact question or end goal in one short sentence; do not add a
second introductory paragraph. Use the user's example and demonstrated
knowledge. Ask only if missing context would materially change the answer.
For a broad topic, start with one useful question and make that scope explicit.
Honor requested length, format, notation, and multiple-explanation requests.

## Choose what the reader needs to see

Select the primary obstacle, then read only the matching guide below. These
are alternatives, not sections to include in every answer. Add a second guide
only when it explains a distinct missing relationship.

| The difficult part | Usually useful | Guide |
|---|---|---|
| What changes, and what stays the same? | Execution trace or before/after state | [State](references/state.md) |
| What causes the next event, or chooses a branch? | Labeled process or decision flow | [Process](references/process.md) |
| Which group, amount, or denominator matters? | Counts, units, or weighted table | [Quantities](references/quantities.md) |
| What distinguishes two similar ideas? | Matched cases or comparison | [Contrast](references/contrast.md) |
| Where is it, or in which direction does it move? | Spatial sketch or successive positions | [Space](references/space.md) |
| What are the parts, levels, or dependencies? | Small structure or dependency map | [Structure](references/structure.md) |
| Why does this mathematical step follow? | Worked derivation with reasons | [Derivation](references/derivation.md) |

For a short definition or a relationship clearer in two sentences, use prose
without loading a guide. Treat interactivity as a presentation choice: use it
when changing a parameter or stepping through time answers a useful question.
A static example must still explain the main point without interaction.

## Walk through one example

Carry the same entities, names, and values from the starting point to the
answer. Make each consequential transition visible and explain why it happens.
Tie prose to the relevant row, arrow, object, or equation; do not narrate every
entry again. End when the original question is answered.

Introduce a prerequisite only when it is needed for the next step. Define a
useful technical term where it first matters. Preserve the condition that makes
the main claim true, beside that claim. Omit side topics, unneeded precision,
implementation digressions, ceremonial summaries, and follow-up menus.

Use the simplest supported format that preserves the relationship: native
text or tables, a small diagram, then richer visuals when useful. Label what
arrows and quantities mean. Do not rely on color alone. If a visual cannot be
rendered reliably, give a clear text equivalent instead of a broken artifact.

## Check and adapt

Read supplied material before explaining it. Check calculations, denominators,
state identity, and whether labels imply the right relationship. Explain code
as written; do not change it merely to explain it. Verify uncertain or changing
facts with primary sources. Mark invented data and simplifying assumptions.
Do not invent numerical detail just to fill a visual.

Give a complete explanation by default. For requested guided teaching, explain
one unit, ask one application question, and wait. On confusion, locate the
missing link and change its representation or example; do not replay a longer
version of the whole answer.
