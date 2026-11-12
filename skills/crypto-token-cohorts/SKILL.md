---
name: crypto-token-cohorts
description: Research recent token launches and build dated comparison cohorts using public or authorized market data. Apply age, market-cap, first-day drawdown, volume, liquidity and narrative screens with explicit unknowns, collapse controls and survivorship limitations.
---
# Token cohort research

Use [assets/token-cohort-plan.json](assets/token-cohort-plan.json). Thresholds and
windows belong to the current brief; never inherit another launch's numbers.

## Define before discovery
Reuse the decision, chains, venues, cutoff and access constraints. Ask only missing
criteria: recent-launch window, cap evidence threshold, desired narrative balance,
and whether the question concerns all launches or conditional survivors.
A survivor-only comparison cannot answer the probability of a successful new launch.

Keep broad categories (animals, characters, events, apps, companies, parodies,
politics) alongside the focal theme. Categories may overlap; designate one primary
label only when totals require it. Record keyword/manual classification uncertainty.
An explicitly lower-cap focal exception stays labelled and out of cap-qualified totals.

## Collect once, preserve the funnel
Use documented public endpoints when sufficient; otherwise inspect the provider's
public interface through the approved browser skill. Verify present capabilities
and limits; an observed chart endpoint is not a supported permanent API contract.
Never bypass authentication/rate limits. Log query, retrieval time, pagination,
failures and raw-response hashes without credentials.

Keep discovered universe, qualified candidates, final manageable shortlist, collapse
controls and unknown-history records separate. Deduplicate by chain+mint, retaining
all pools. A token's oldest observed pool/indexed candle is a date proxy, not verified
mint birth. Multi-pool quotes, migrated venues and quote currencies need reconciliation.

## Apply defensible screens
- Market cap: retain current reported cap and historical reported cap highs with
  source/time/method. Keep FDV separate. Price × current implied supply is only a
  proxy, not proof of historical circulating cap. Unknown historical supply stays unknown.
- First day: use the declared launch-time reference, first-day peak and price near
  launch+24h. Report candle resolution, coverage, outlier treatment and endpoint tolerance.
  Down ≥90% means `(P24 / Ppeak) - 1 <= -0.90`; use the requested threshold, not always90%.
  Recent24hchange is not this statistic. Partial birth history or stale endpoints → unknown.
- Market quality: report cap, reference-pool liquidity, volume, buys/sells and freshness
  separately. Missing liquidity is not zero; current depth is not historical depth.
- Context: chain and venue volumes, trend windows and protocol TVL help scope the market.
  Volume is not retail demand and TVL is not exit capacity. Do not double-count aggregator
  routing and underlying pools. Material provider discrepancies remain unresolved or
  produce separate comparisons, never an averaged calibration target.

## Deliver and hand off
Deliver a small ranked slate plus the full traceable funnel, exclusion reasons and
raw evidence. Distinguish primary-category counts from overlapping labels. Expose
thin/quiet/stale markets and evidence strength; avoid a cap-only ranking.

Use snapshots to propose stress ranges and comparable populations, not KOL conversion,
causal marketing ROI, real identities or wallet motivations. A chart-filtered sample
is neither a complete census nor a calibrated distribution of launch outcomes.
Hand permitted findings and unsupported inferences to `$boyun-world-grounding` when
building a world. Keep actual case data out of this skill and public examples.

## Preserve path and transition evidence
If the decision includes rapid declines, upside targets or migration, expand the
research plan to transition timestamps, stage-specific metrics and adequately fine
trade/quote paths. Fifteen-minute bars cannot validate a five-minute decline. Keep
observed cap thresholds distinct from confirmed migration state; record pool/venue
changes, quote freshness and gaps. Sample extremes and failed/recovered cases rather
than studying endpoints alone. Missing paths remain unknown, not 'no crash'.
