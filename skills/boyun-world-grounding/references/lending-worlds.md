# Grounding a lending-launch world

Learned from the NEAR lending case (2026-11-05). Repository guide:
`docs/decision-lab/LENDING_CASE_RUNNER.md`; case record:
`docs/decision-lab/cases/near-lending/` (41 recorded user answers in `intake.json`).

## Choices to settle with the user before building

1. **Funding condition.** Is opening supply already deposited, or do partners
   decide whether to fund inside the run? Without negotiated terms, label
   "deposited at opening" a hypothetical starting condition, not a commitment.
2. **Debt and collateral assets.** Name the exact asset (e.g. Circle native USDC,
   not bridged USDC) and keep identities separate.
3. **Incentive basis.** Points on supply actually borrowed versus on deposits.
   No token value or redemption unless supplied.
4. **Treasury.** Day-one cash versus later optional cash; a capped loss reserve
   versus none; who pays which campaign item, and only on delivery.
5. **Team authority.** Which levers the team may pull during the run. Unsupported
   levers (rate or cap changes, pauses, injections) need engine actions first.
6. **Market paths.** Offer real historical windows (bear, bull, choppy,
   crash-day) instead of invented prices. Each selected window is one run.

Show setup progress and the current stage in each question.

## Arithmetic to run before any model call

- **What binds.** Compare supply capacity, borrow capacity (collateral × price
  × max LTV), the per-borrower cap × number of borrowing accounts, and the
  aggregate cap. In the first case, $1.7M of supply faced a $300K effective
  ceiling, so utilization could not exceed about 15–25% whatever actors chose.
- **Outside option.** Supplier yield ≈ utilization × borrow rate × (1 −
  protocol share). Compare it with a dated snapshot of the main competing venue
  (Rhea paid 9.88% on native USDC). Matching it at 25% utilization needed about
  a 46% borrow rate, which settled the rate-curve question without a run.
- **Liquidator capacity.** Liquidator cash and per-hour exit depth versus maximum
  debt. Mark both as assumptions unless depth is measured.

## Cast construction

- One funded account per decision-maker. A cohort of 80 people as one account
  under one per-borrower cap understates its demand; split it.
- Give each actor a short private motive (≤160 characters). It is passed to the
  model with the observation; without it, different partners look identical.
- Awareness by channel: each outsider follows named channels and becomes able to
  act only when one of them actually delivers. Do not assume follower-to-user or
  click-to-deposit rates.

## Prices and what the ledger can see

Replay real hourly closes, scaled so the window opens at the snapshot price;
this keeps moves and timing, not the historical level or liquidity. Record
both the close-based drawdown and the intrahour low. If the oracle samples
hourly closes, the intrahour low is not simulated. One 2025 crash wicked −40%
but closed its hour about −9%.

## Actor model cross-check

Laya is free and local; Jev is paid and needs an explicit spend cap. In the
first case they reversed every behavioral result (Laya borrowed at any rate; Jev
never borrowed), and neither changed its choices when the rate rose 2.5×.
Before stating any behavioral finding, run the same world on a second model.
Label each finding mechanical (set by rules) or behavioral (set by choices).
Real demand evidence (signed borrower intents, a capped pilot) beats more
simulation.
