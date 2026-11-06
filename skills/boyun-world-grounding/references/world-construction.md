# Research-to-game handoff

| Element | Why it exists | Failure without it |
|---|---|---|
| Players, roles, private types | Different resources and incentives | Everyone behaves as the same omniscient actor |
| Capital, inventory and constraints | Make actions feasible and outcomes conserved | Spending or influence appears for free |
| Information sets and disclosure timing | Separate known facts from private plans | Retail acts on a board's future campaign |
| Goals, payoff and horizon | Explain tradeoffs and when cash can be realized | Price rises become fictitious founder profit |
| Action menu and transition rules | Make model outputs executable | Narrative decisions cannot update the world |
| Beliefs and dependencies | Represent uncertainty without false independence | Correlated shocks get counted independently |
| Evidence and assumptions | Explain parameter origin | Model-generated numbers look empirical |
| Counterfactual and sensitivity | Reveal what changes a ranking | One favorable story appears inevitable |

A persona specification records role, owned resources, private information, public
observations, goal, horizon, payoff terms, action permissions, behavioral alternatives
and parameter provenance. Reputation is a modeled incentive only if its consequence
exists in the payoff or future process. Narrative risk aversion is not implemented
risk aversion without a supported utility or decision mechanism.

Jev request planning:
1. Assemble only the actor's permitted observation and own resources.
2. Provide a finite feasible menu with stable IDs, action meaning and consequences
   the actor could know. State the actor's goal, costs and relevant constraints.
3. Request a typed choice using the current official TypeSafe API contract. No prose
   reasoning or unsupported schema may be assumed. Do arithmetic and admissibility
   before the request, not in the question.
4. Validate the answer; use the probability distribution under an explicit sampling
   or threshold policy. Keep that policy fixed across compared arms unless it is
   the experimental variable. Record prompt/request hashes, model/version and costs.
5. Settle with numerical rules, reveal only authorized messages and continue.

The distribution is a conditional model judgment about an action, not an observed
frequency of a real-world event or a measured willingness to invest. Calibrate using
separate held-out observations when available. Do not invent a chain of thought.

Boyun has multiple modules; inspect the current checkout. Verify actor/round/report
limits, turn ordering, message delay, cash vs utility settlement and event support.
Do not treat a finite-game Nash diagnostic as a large-population equilibrium solver,
a generic AMM as a launchpad, or a strategic point score as a dollar return.
Research templates require an explicit translation and validation into the selected
module's accepted input. Unsupported mechanics remain blockers, not silent substitutes.
