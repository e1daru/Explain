# Make a distinction visible

Use for similar concepts, a misconception, or the question "what would change
if...?" Keep one situation fixed and vary the condition that matters. A small
table helps when corresponding properties need to be compared; a pair of
sentences is better for a simple distinction.

Example request: "How are authentication and authorization different?"

Use one attempt to open a private document:

| Check | Question it answers | Example outcome |
|---|---|---|
| Authentication | Which user is making the request? | Recognized as Sam |
| Authorization | May that user open this document? | Sam has no access |

A successful identity check can therefore be followed by a denied document
request. The second check depends on the permissions for that document.

Compare cases along the same dimensions. Explain why the changed condition
changes the outcome. Do not produce a broad pros-and-cons list when one
distinction answers the question.

An analogy is another possible bridge, not a required opening. Map the
relevant parts explicitly and mention a limit only when it prevents a wrong
inference. If understanding the analogy requires more work than understanding
the actual mechanism, use the actual mechanism.
