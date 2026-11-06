---
name: boyun-world-grounding
description: Build Boyun financial and economic simulation research briefs from user conversations and evidence. Map claims into actor incentives, unequal information, finite actions, rules and validation gates without confusing model judgments with calibrated event odds.
---
# Boyun evidence-to-world grounding

Use [assets/world-grounding.json](assets/world-grounding.json) for the research
handoff. It is a planning contract, not an executable world schema. Read
[references/world-construction.md](references/world-construction.md) when defining
actors, typed Jev questions or engine handoff.

## Start with the user's decision
Inherit known answers from the conversation/research brief. Identify the compared
choices, success measure, horizon and source access. Ask only two or three missing
choices that change evidence collection or mechanics; explain why they matter.
For example: Which actor perspectives need detail? Which privately held plans may
partners see? Which missing rates should be researched versus tested as assumptions?
Keep accepted decisions separate from proposed defaults. Never ask users to provide
API secrets in chat. No new paid pilot is implied by world construction alone.

## Research what can change the world
For each parameter trace: user decision → research question → evidence → usable
feature → actor/rule → output affected. If evidence cannot support a parameter,
retain it as unknown or an explicit proposed assumption. Record cutoff and freshness.
Market volume cannot establish retail wallets' cash, and a token chart cannot reveal
KOL incentives. Gather transactions/positions, contracts, audience evidence and event
sources separately when those mechanisms matter. Preserve provider disagreements.

## Construct the game before personas
Define players and bounded resources, private types, information available at each
decision, feasible actions, timing, state transitions and payoff accounting. A shared
profit motive does not mean shared wealth, information, beliefs or time preference.
Include an abstain/wait action where feasible and give every cost a payer.

Build reviewed role templates, then scenario-specific variants grounded in evidence
or labelled hypotheses. Let the user emphasize roles and behavioral variants.
More variants improve detail by default; they must not increase total wealth,
population share or influence. Distinguish cohort weights from independently funded
market agents; one weighted trader is not many interacting traders.

## Bind information and decisions
Separate world truth, actor observations and actor beliefs. Restrict private fields
before model requests; review public descriptions, action labels and messages too.
Model outputs can reveal only what their actor is authorized to know. Belief updates
need supplied likelihoods/mechanics; they do not happen because a prompt says Bayesian.

Use direct official TypeSafe Jev for bounded typed action judgments where configured,
or local Laya when the user wants free private inference. Before a behavioral
claim, run the same world on the other model: in the 2026-11-05 lending case the two
reversed every behavioral result.
A separate author constructs the world and action menu; Jev does not write prose,
construct rules or supply a reasoning trace. Validate returned option IDs, finite
probabilities and totals, record model/version, observation and usage. Arithmetic,
capital feasibility, fees, dates and settlement belong in code. No hidden fallback.

## Review before execution
Locate the actual engine schema and limits; do not reuse remembered limits as current
facts. Give every proposed mechanism an executable target or mark it unsupported.
Test information isolation, resource conservation, valid actions, reproducibility and
sensitivity before a small authorized live pilot. Schema validity is not calibration.

Report readiness separately for evidence review, world construction and execution.
Keep event odds, Jev action judgments and repeated-run frequencies distinct. Frozen
policies mean the compared runs use the same declared decision mechanism, not that
actors ignore new observations. If policies are prepared ahead, specify their covered
states and stop on uncovered states. No terminal outcome may leak into decisions.

## Discover contingent choices proactively
For financial decisions, read [references/stress-policies.md](references/stress-policies.md)
and use [assets/stress-policy-plan.json](assets/stress-policy-plan.json). The agent
proposes lifecycle states, extreme/combined shocks, feasible responses, failure and
recovery branches before asking the user to fill gaps. Check response choices for
authority, timing, funding, information leakage and goal conflicts. A ready initial
allocation is not a complete contingent policy. Do not claim five-minute monitoring,
automatic live trading or calibrated tail odds from this planning workflow.

For a lending or borrowing launch, read
[references/lending-worlds.md](references/lending-worlds.md) first: funding
condition, cap arithmetic, outside-option yield, cohort splitting, channel-based
awareness and what an hourly oracle can observe.

Use [assets/stress-policy-examples.json](assets/stress-policy-examples.json) only
for illustrative token and DEX branches. Their thresholds are not accepted defaults.
