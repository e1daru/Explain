# Show parts, levels, or dependencies

Use when the reader cannot place an unfamiliar part in a larger system.
Choose the relationship before drawing: "is part of," "is a kind of,"
"depends on," and "sends data to" mean different things.

A tree suits genuine nesting. A labeled graph suits dependencies that cross
branches. Keep one level of detail relevant to the question; do not draw an
entire architecture because one component is unfamiliar.

Example request: "Where does an index fit in a textbook?"

    Textbook
    ├── Chapters: explain subjects
    ├── Contents: lists chapters in reading order
    └── Index: maps terms to the pages that discuss them

The contents helps you choose a chapter. The index helps you find a particular
term wherever it appears. This is a part-of map, not a sequence in which the
book must be read.

For a layered technical system, show the role of each relevant layer and trace
one example across the boundaries. If the question instead asks what happens
next, use a process representation. Avoid unlabeled boxes whose arrangement
looks meaningful but does not tell the reader which relationship to infer.
