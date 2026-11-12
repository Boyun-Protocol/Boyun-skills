---
name: crypto-launch-research
description: Prepare evidence-based token-launch simulations and compare capital, marketing, partner, liquidity, buyback and no-launch plans. Define ownership, venue mechanics, independently funded actors, realizable proceeds and exit constraints before modeling profit.
---
# Launch research and economic planning

This is a research/simulation workflow. It does not deploy a token, trade, publish
announcements or contact partners. Use [assets/launch-plan.json](assets/launch-plan.json).

## Complete the economic question
Reuse the known venue, capital and horizon. Ask material missing choices in small
groups: success metric; founder income/ownership route; partner privileges/funding;
exit deadline and residual inventory tolerance. Give choices and explain the change
in economics. Treat founder cash, research/API spend and partners' money separately.
Include do-not-launch and staged/delayed launch when relevant, with comparable accounting.

## Verify the mechanism
Read current official venue/program documentation for issuance, curve, fees,
creator-fee collection, migration and liquidity ownership. Record effective date,
configuration and unsupported parts. A generic constant-product AMM is not a
faithful launchpad lifecycle. An earmarked liquidity budget is not deployed liquidity.

Define founder inventory acquisition, payer/recipient of every cost, token holdings,
fee entitlement and collection delay. Separate allocation, committed expense,
actual payment, recoverable reserve and invested principal. Avoid charging the same
expense twice or counting partner capital as the founder's contribution.

## Compare funded plans
Keep initial founder contribution fixed across alternatives. Vary a few meaningful
axes: many small vs few large partners; paid exposure vs market depth; entry sizing;
reserve and exit policy. Label proposed fee/reach/rate grids as hypotheses until
accepted or sourced. Explain why each parameter exists and its directional effect.

A campaign buys posts/exposure, not buyers. Model funded contractual deliveries,
audience overlap, attention limits and independent response. Paid KOL fees, token
holdings and reputational exposure are distinct incentives. Disclosure/reputational
cost is not automatically decisive; represent uncertainty and delayed consequences.

Partners with early information are not guaranteed allocations or coordinated
trades. Actors see only authorized information. Include counterfactuals for quiet
attention, event resolution, sell pressure and operational delay. Do not promise
returns or use survivors alone to estimate launch-success odds.

## Define the result before running
Use a founder ledger. If all founder-controlled cash accounts are consolidated,
net cash profit = prior owner withdrawals + ending withdrawable cash − owner
contributions. Exclude those prior withdrawals from ending cash. Cash already
reflects paid expenses and realized sales; do not subtract them twice.
Show tokens, locked balances and recoverable positions separately from withdrawable
cash. For a no-launch all-cash plan, unchanged capital means zero profit. Keep
mark-to-market value separate from realizable proceeds after impact, fees and costs.

Bound reserves and buybacks by cash, forbid unsupported shorting, and specify who
can sell when and through which mechanism. Compare medians/downside/tail outcomes
only under declared assumptions. Jev choice probabilities do not price liquidity.

Hand the reviewed economic specification to `$boyun-world-grounding`. If no engine
supports the required cash/venue mechanics, return that blocker rather than USD
profit invented from strategic utility scores. Preserve spend authorization and stop
conditions before any paid pilot; log requests, typed answers, usage and estimates.

## Compare response policies, not only launch allocations
Propose before/during/after-migration states using actual protocol transition evidence.
Discover rapid losses, cap/price upside levels, depth withdrawal, catalyst resolution,
reserve exhaustion and failed/delayed exits without waiting for the user to list them.
For each branch specify observation/reference, window, thresholds, actor authority,
funding, delay, partial/no fill, simultaneous-trigger priority and recovery. Offer
feasible choices and check them against the user's cash objective. A stop threshold
is not a guaranteed fill; migration is not inferred from market cap alone. Route to
`$boyun-world-grounding` for the general stress-policy template and DEX applicability.


## External market-maker contracts
Use [assets/market-maker-mandate.json](assets/market-maker-mandate.json) when an
external MM is proposed. Research official service scope, then retain unknown quote,
minimum capital and token/venue eligibility as unknown. Fees and working capital
are separate; reconcile them with operating budgets to prevent double-counting.
Distinguish a contracted agent from an independent principal, and record ownership,
custody/control, P&L, any loan/option liabilities, withdrawal and termination rights.
The founder cannot automatically pause a principal's own trading or withdraw its
assets. Separate alert detection, delivery, human reaction, provider cancellation,
transaction execution and confirmation. A human 'under30minutes' bound does not
supply an exact latency distribution. No service quote or private plan is shared
with a provider without the user's instruction to contact it.
