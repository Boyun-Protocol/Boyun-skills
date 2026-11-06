# Lifecycle, shocks and response policies

## Discover; do not just ask users to enumerate

Start from the objective, mechanism, actors and existing answers. The agent builds
a proposed map of lifecycle states, value flows and dependencies; users correct
priorities, control rights and constraints. Propose material upside, downside,
transition, recovery, no-action and failed-response branches. Explain why each can
change the decision, then ask two or three unresolved material choices at a time.

| Layer | Agent prepares | User supplies or confirms |
|---|---|---|
| Objective/constraints | Outcome definition and conflicting goals | Acceptable loss, locked resources, horizon, priority |
| Lifecycle | States, real transition evidence and dependent mechanics | Intended venue/product design; special control rights |
| Stress coverage | Relevant shocks, combinations and missing observations | Priorities or omitted situations, not the entire catalogue |
| Trigger specification | Metric, reference, window, freshness and visibility | Threshold preferences if not measurable from evidence |
| Response policy | Feasible choices, cost, timing, failure and fallback | Compare policies, approve a proposed policy or retain human decision |
| Validation | Unsupported mechanics, test cases and remaining gaps | Material tradeoffs; never secrets in chat |

## General discovery dimensions

- Market/path: rapid price moves, gaps, spikes and reversals; upside targets too.
- Depth/concentration: LP withdrawal, inventory imbalance, large holders, routed flow.
- Treasury/cash flow: committed costs, runway, fees, funding/buyback exhaustion.
- Incentives: reward expiry, sponsor/partner exit, adverse selection, public-information changes.
- Operation/infrastructure: stale data, congestion, RPC/oracle failure, exploit suspicion.
- External events: catalyst resolution, decision postponement and competing attention.
- Recovery/termination: re-entry, restart, compensation obligations, residual positions.

Select only applicable dimensions and explain omissions. A DEX type, lending system
or launchpad determines mechanics; no checklist implies one generic engine supports all.
Life stages are observed protocol states, not merely marketing labels. A cap threshold
can be a user trigger but cannot replace confirmation of actual protocol migration.

## Trigger → observation → response

A trigger needs ID, applicable lifecycle, metric/unit/source, reference, comparator,
window, cadence, freshness/gap policy, detection delay, actor visibility and rearming.
A five-minute return compares the observed price at time t with an admissible price
at t−5minutes: r = P(t)/P(t−5m)−1. A peak drawdown uses a peak reference instead.
Specify price venue/side/numeraire and endpoint tolerance. A missing or stale reference
makes detection unknown; it is not evidence the event did not happen. Fifteen-minute
bars cannot establish the exact five-minute path. Do not interpolate evidence into existence.

A response defines actor/authority, feasible action, funding, latency, fees/impact,
partial fill/failure, cooldown and fallback. Trigger threshold is a decision boundary,
not a guaranteed execution price. A trigger can be observed after substantial overshoot.
Automatic simulation policy and actual transaction authorization are separate.

Resolve simultaneous triggers, lifecycle changes and pending decisions under an explicit
ordering. Choose priority or composability and reserve funds once; cancel stale actions
where necessary. Specify cooldown/rearm/recovery to prevent repeated spending on every
observation. Include unobserved and blocked paths in reporting. No unsupported expressions,
external instructions or arbitrary executable code belong in a condition.

## Check the user's choices

| Check | Example issue | Handling |
|---|---|---|
| Definition | 'down20%' with no price/window reference | Ask or propose an explicit definition |
| Authority | Change protocol fee without admin right | Mark unavailable; offer feasible alternatives |
| Budget | Same reserve promised to multiple simultaneous responses | Report conflict; prioritize or reallocate |
| Mechanism | Sell at stop price with absent bids/depth | Model gap, partial or no fill; do not guarantee exit |
| Goal conflict | Require cash exit yet prohibit sales in every exit branch | Explain contradiction and ask preference |
| Observation | Fifteen-minute bars used for five-minute trigger | Research finer data or label hypothetical stress path |
| Timing | Detect incident after response window has expired | Include delay/failure branch |
| Information | Retail reacts to unpublished board action | Restrict information and disclosure timing |
| Feedback | Buyback changes price and other holders then sell | Represent endogenous effects and cash cost |
| Recovery | Resume automatically while data is stale | Explicit recovery criteria or remain paused/unknown |

Preferences are not automatically invalid. Distinguish malformed definitions,
unsupported controls, infeasible resources, contradictory goals and merely untested
assumptions. Clarify material conflicts before execution, without promising safety.

## Branch odds and comparison

Occurrence likelihood, shock severity, observation probability, action judgment and
execution success are different quantities. Do not label all of them 'confidence'.
Rare scenarios with no trustworthy frequency remain named stress tests. Do not make
independent percentages for overlapping crashes and LP exits, or renormalize an
unobserved branch away. Conditional policy changes future outcomes and possibly
future event likelihoods; an exogenous shock replay must be labelled as such.

Compare policies under matched initial capital and declared shocks. Record state,
observations, decision/failed alternative, execution, funds and actor consequences.
Report per-scenario outcomes, downside, time underwater, recovery and terminal
inventory/locked capital. Aggregate only with justified weights; unweighted scenario
coverage is not a forecast. Model choice probabilities never establish crash odds.

## Existing product boundary

Author prompts can discover and clarify these requirements. A planning JSON does
not execute them. Inspect current module capabilities before translation: scheduled
metric events and declared choice scenes do not implement rolling-time detection,
real venue state transitions, action permissions or cash settlement. Missing mechanics
must block the corresponding claim, even if a simpler toy world can be generated.
