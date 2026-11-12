# Evidence contract

A claim needs an ID, value (or null), unit, status, applicable population/time,
source IDs and a permitted use. A source needs a URL or local artifact, publisher,
retrieved-at time, coverage, measurement definition and raw hash when available.
Never store authorization headers, cookies or secrets in provenance.

| Status | Meaning | Allowed downstream treatment |
|---|---|---|
| observed | Source directly reports this measurement | Conditional on its definition, coverage and reliability |
| derived | Reproducible calculation from named inputs | Preserve formula, input IDs, units and uncertainty |
| assumed | User-accepted or explicitly proposed hypothesis | Sensitivity; proposed is not accepted |
| model_judged | Typed model assessment of supplied information | Conditional behavioral hypothesis, not empirical frequency |
| disputed | Relevant sources materially disagree | Reconcile or compare source-specific assumptions |
| unknown | Missing, inaccessible or unusable | Leave null; block dependent calibration or substitute only visibly |

Separate event time, observation time and retrieval time. Later observations must
not leak into an earlier actor decision or training/test cutoff. Expired observations
need a refresh or an explicit frozen historical interpretation.

Missing is not zero. FDV is not circulating market cap. Protocol TVL is not executable
pool depth. OHLCV bar volume may not be USD. Swap counts are not unique buyers.
Record quote/base direction, currency conversion, pool scope and aggregation window.

A transformation names its formula and inputs. For example, first-day drawdown uses
price near launch+24h and the maximum high within the first day, not the most recent
24h percentage. Missing birth history makes that test unknown. A source's indexing
start or pool creation time does not independently attest mint creation.

A derived claim cannot gain stronger evidentiary status than its weakest material
input. Conflicts need a resolution note or separate sensitivity branches, not an
invented consensus. A credible source can still measure the wrong population.

Attach each parameter to a claim or labelled assumption and state why it exists,
its admissible range and what increasing/decreasing it changes. Context-only facts
must not silently become numerical rules. Re-check claim permissions at world creation.

## Evidence changes with the decision

| Research problem | Evidence to request before choosing parameters |
|---|---|
| Launch capital allocation | Venue lifecycle/fees, funded positions, campaign contracts, comparable charts and exits |
| Lending/liquidation risk | Balances, debt, collateral rules, oracle/pricing source, rate model and liquidation mechanism |
| Protocol growth or adoption | Defined usage population, fees/revenue, retention, incentives and comparable periods |
| Governance or political catalyst | Primary decisions/calendars, confirmed statements, information timing and alternative outcomes |
| Wallet behavior | Dated trades/positions/funding coverage; size/activity cohorts, not inferred real-world identities |
| Social attention | Authentic source/account, timestamps, reach/overlap measurement; no automatic trade-conversion claim |

These specify evidence needs, not a guarantee that the simulation engine implements
each domain. Unsupported domains remain research-only until mechanics are validated.
