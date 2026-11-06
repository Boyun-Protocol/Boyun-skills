---
name: boyun-financial-reports
description: Write decision-grade reports for stateful Boyun financial simulations, especially paired bull and bear regimes. Use for actor-driven financial worlds with event progression, execution state, or cross-world comparisons.
---

# Boyun financial simulation reports

Create a decision-grade, auditable report package for stateful financial
simulations. The standard package contains **World Creation**, **Bear Case**,
**Bull Case**, a **Technical Report**, and a **User Q&A Record**. The first three
explain the worlds and their outcomes to decision-makers; the technical report
explains how the runs were produced and verified; the Q&A record preserves the
user decisions that shaped the experiment. A linked contents page belongs near
the start of each substantial PDF. Keep machine-readable inputs, evidence,
receipts, and chart data alongside the documents.

Follow the step-by-step [financial reporting playbook](references/FINANCIAL_REPORTING_PLAYBOOK.md)
for document responsibilities, interview and evidence capture, tool workflow,
technical and cost reporting, chart design, and the worked MACRON example. Follow
[REPORT_STRUCTURE.md](references/REPORT_STRUCTURE.md) and
[REPORT_DEPTH_STANDARD.md](references/REPORT_DEPTH_STANDARD.md)
for project packaging, evidence and analytical standards. The playbook
generalizes the MACRON example; adapt it to the actual actors, events, data, and
mechanisms available in each case.

Before writing, inspect the run artifacts, scenario inputs, event records,
settlements, and generated charts. Read the shared
[simulation evidence standard](references/SIMULATION_EVIDENCE_STANDARD.md)
and [lifecycle guidelines](references/LIFECYCLE_SIMULATION_GUIDELINES.md)
when applicable. For reference-article review and research-style treatment, use
[references/research-style.md](references/research-style.md). It records the
eight featured DL Research web editions reviewed on 3 November 2026, their useful
conventions and limits. Do not claim a readership ranking or an exhaustive PDF
review; do not inherit promotional or causal claims from editorial references.

## Allocate the reader-facing financial analysis across three documents

**World Creation** documents the experiment before its outcomes are interpreted:

- The question, run identity, evidence cutoff, model and execution boundary.
- Actors and their goals, resources, information, and material relationships to
  real-world entities. Distinguish sourced relationships from modeled or assumed
  ones.
- Rules, action contracts, event schedule, regime inputs, policy interventions,
  and important missing mechanisms. Explain how evidence or an explicit causal
  assumption supports each material input and transfer to outcomes.
- The shared baseline and comparison design, including whether a no-launch arm
  exists and what it holds constant.
- Run status and coverage: identify native execution versus offline/reconstructed
  work, completed versus incomplete periods, attempted versus completed actions,
  and any unsupported or missing records. Link the source artifacts and receipts.

**Bear Case** and **Bull Case** each describe that regime on its own terms. Include
the regime assumptions and their rationale; the world's progression and dated
turning points; material events; actor actions and reactions; execution and
settlement outcomes; and implications for the decision. Explain differences from
the other case using same-time observations where possible. State which comparison
is matched, which inputs changed, and any confounding. Include no-launch results
when run; never imply a baseline was tested if it was not.

The cases should make the path legible, not just report an endpoint: show what
actors knew at the time, which choices were available, what they attempted, what
filled or failed, and what state change followed. Do not fill gaps in the event
record with a plausible narrative.

## Technical report and user Q&A record

State the actual recorded simulation duration and confirmed model-call count
plainly. At the final saved time, report whether the simulated project still has
observed activity, with the window and evidence used; the end of a recording is
not itself the end of the project. If activity or termination cannot be determined,
say so. Keep the reader-facing account focused on the recorded outcome rather
than a history of changes to the requested duration.

The technical report records run identity, provider/model/configuration, complete
and attempted work, calls and cost units, receipts, retries and unknown dispatches,
runtime/stopping reasons, replay/checkpoint validation, execution mechanics,
coverage, and a reproduction path. Attribute a stop to a provider only when its
receipt or logs support that cause. Distinguish provider cost from a tariff-based
estimate and planning estimate. Reader-facing outcome reports cannot substitute
for this run-level accounting.

The Q&A record preserves original questions and materially consequential user
answers or corrections, links each to changed inputs, and marks proposals,
assumptions, decisions, and unanswered questions separately. Do not silently
rewrite user intent or imply approval for actions the user did not authorize.

## Findings, odds, and charts

For each decision-relevant finding, provide a stable claim identifier where the
artifact system supports it, the observed value and unit, the relevant world or
event denominator, the comparison, evidence links, and why the result matters.
Separate a measured mechanism from a plausible hypothesis, name a credible
alternative explanation, and say what evidence could falsify the claim. Label
recorded simulation facts, external empirical observations, assumptions or policy
interventions, associations, hypotheses, and unsupported conclusions distinctly.
Free-text model rationales do not establish causality and must not be invented.

When calibration to real-world outcomes is absent, real-world odds are **unknown**.
Report the actual number of worlds and observed frequencies (for example, three
of four), disclose dependence and shared initial conditions, and avoid calibrated
probability language. Do not convert a small sample to a 100-world display or
invent a probability to make a chart complete. Keep provider scores, assumed event
odds, sampled frequencies, and empirically calibrated frequencies distinct.

Use charts only when they clarify a material pattern in actor actions, reactions,
state progression, or trends. Every chart needs a nearby interpretation with the
number, unit, denominator and window; the supported mechanism or labeled
hypothesis; and the practical implication. Preserve missing values, failures,
negative outcomes, and uncertainty. Avoid decorative charts and unsupported
forecast bands or tail statistics. Figures should regenerate from versioned run
data; verify their values against the source outputs and inspect their rendering.

Give each world a memorable short name and a code whose budget components are
defined in plain language. Show price, executed trade count and volume over time
when recorded, with a full timeline of meaningful events and actor decisions;
compare each attribute across worlds at aligned times. Identify partial hours and
unobserved horizons. Break down crowd choices and distinguish option scores,
sampled choices, attempts, fills, and settlements. Do not invent partner
negotiations, reasons, probabilities, or peer benchmarks that were not recorded.
Explain a relevant real-world comparator with its source, date, unit, and sample
definition, or state that no defensible comparator is available. Cite real-world
and run-data sources at first use. Keep editorial research and report-writing
references in internal skill materials, outside reader reports. Follow the
playbook for readable fonts, purposeful color/background, chart spacing, Gantt-like
timelines, PDF/mobile inspection, and technical cost/coverage reporting.

## Comparison and delivery checks

- Mark each case as native and complete, native and incomplete, or offline /
  reconstructed, using run receipts and actual coverage. State the dates and
  hours covered, missing intervals, and what the status permits readers to infer.
- Align comparisons at the same timestamps and disclose when coverage differs.
  Do not compare one arm's endpoint with another arm's earlier state as if they
  were simultaneous.
- Reconcile actor-level and group-level cash, inventory, fees, and recoverable
  claims where supported. Keep marked inventory, liquid cash, and economic profit
  distinct; unsupported valuation stays unavailable.
- Report attempts, fills, rejections, failures, and absent activity with correct
  denominators. No attempts means rejection rate is unknown.
- Preserve the exact experiment design. Disclose changed policies, sampling,
  stress multipliers, budgets, and other confounds. Do not claim a regime effect
  or causal campaign impact from unmatched arms.
- Give every edge case a coverage state such as observed, tested, planned, or
  unsupported. An unrun case is an open question, not a simulated event.
- Confirm all three documents have their table of contents near the front (pages 1–3), their
  numeric claims reconcile to run data, and their evidence links resolve.

## Lessons from the NEAR lending casebook (2026-11-05)

A second worked example, for a collateralized-lending launch rather than a token
launch: `tools/build_lending_casebook.py` builds six documents from six frozen
90-day worlds. It reuses the MACRON renderer through optional `project`,
`footer_note`, `cover_note`, `cast_panel` and `x_unit` fields. See
LENDING_CASE_RUNNER.md.

- **Generate every number from run data.** Put the aggregation in a data module
  (`lending_casebook_data.py`) and build sentences with f-strings from it. Doing
  this exposed two errors in hand-written summaries: interest totals that left
  out interest paid to suppliers, and a drawdown the ledger never observed.
- **Report the statistic the simulation sampled.** If the oracle reads hourly
  closes, intrahour lows are not simulated events. Give the sampled drawdown,
  and name the unsampled wick as untested.
- **Separate revenue layers.** Borrower interest (paid + still owed), supplier
  income and the protocol's share are different quantities. Compare spending
  with the protocol share, not with total interest.
- **Label claims as mechanical or behavioral.** Results set by rules and caps
  can be decision-grade. Results set by actor choices need a second actor model.
  In this case Laya and Jev reversed every behavioral result, and neither
  responded to a 2.5× rate change.
- **An unrun regime gets its own short document** stating it was not run and how
  to run it. Do not substitute another regime under its title.
- **Name worlds with a code whose parts are defined**, e.g. `C-P100-R8-J` =
  choppy path, $100K per-borrower cap, 8%-base rate curve, Jev. Disclose
  comparisons that change two inputs at once.
- **Inspect rendered HTML, not only PDFs.** reportlab names every SVG clip path
  `clip`; inline charts shared one ID and lost their top rows. The renderer now
  makes the ID unique per exhibit. Check timelines and stacks in a browser.
- **Contents page placement:** the sticker-style renderer puts the contents on
  page 3 (cover, short version, contents). Keep that documented placement, or
  move the short version after the contents when pages 1–2 are required.
- **`.gitignore` matches `DATA/`.** A generic `data/` rule matches
  `DATA/` case-insensitively on macOS. Force-add a package's exhibit data.

Do not silently replace this package with the legacy static-estimator report
layout. The `boyun-case-report` skill remains appropriate for that estimator and
routes stateful financial simulations here.
