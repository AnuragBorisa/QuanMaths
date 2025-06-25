Use R_X when you want a mixer that only converts the previously tagged cost-phase γ into measurement bias. That is exactly the QAOA requirement: no phase imprint ⇒ no bias.

Use R_Y when you want a simple population-shifter that may also introduce its own bias (but not tied to any prior phase).


𝑅_X acts like a “phase‐aware stir”: it takes whatever relative phases you’ve already imprinted (your cost‐tags) and uses them to drive constructive or destructive interference in the measurement. In other words, the interference pattern depends on the pre‐existing phase 𝛾


R_Y is a “blind stir”: it rotates amplitudes but doesn’t respect the earlier phase‐tags. Instead it injects its own shift so the final interference is a mix of your mixer’s choice and whatever phase was there, making it impossible to cleanly amplify only the cost‐desired states.

