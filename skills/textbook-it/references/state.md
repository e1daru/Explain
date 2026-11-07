# Show changing state

Use for execution order, recursion, pointers, closures, iteration, or any
question where the reader loses track of what persists.

Choose a small input. Give stable names to the objects or calls that matter.
Track only the fields needed to explain the result. Each row is an event;
its columns show the relevant state after that event. Distinguish a reference
to an object from the object itself. For recursion, include the returning
values, not only the calls going downward.

Example request: "Why does changing b also change a?"

    const a = { score: 0 };
    const b = a;
    b.score = 1;

| After | a points to | b points to | Object P |
|---|---|---|---|
| Create a | P | Not assigned | score: 0 |
| Assign b = a | P | P | score: 0 |
| Set b.score = 1 | P | P | score: 1 |

Both names reach the same object. Assignment copied the reference, so the
last statement changes the object reached through either name.

The useful information is shared identity, not a description of every symbol.
For this example, drawing two independent objects would teach the wrong model.
Avoid long traces that hide the one transition causing confusion.
