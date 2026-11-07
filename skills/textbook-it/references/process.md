# Show a process or decision

Use when the obstacle is causality, order, responsibility, a branch, or a loop.
Choose a labeled flow for causes and decisions, a timeline for elapsed order,
or a small sequence diagram when messages cross between participants.
These are different relationships; do not let an unlabeled arrow stand for all.

Begin at the input the user cares about and finish at their desired outcome.
Walk one concrete path before adding relevant branches. Put a branch condition
on the branch. Include a failure path only when the question depends on it.

Example request: "How does a thermostat decide when to stop heating?"

In a simplified controller with one target temperature:

    Measure room temperature
              |
              v
    Temperature below target?
          / yes        \ no
    Heater on         Heater off
          \              /
           Measure again

Below the target, the heater supplies heat. Once the measured temperature
reaches the target, the controller switches the heater off. Continuing to
measure lets it respond when the room cools again.

This answers the control question without describing wiring or software
architecture. The diagram models the controller's decision; it does not
promise instantaneous temperature changes or describe every real thermostat.
For causal explanations, explain the mechanism behind an arrow rather than
merely placing two event names next to it.
