# How evidence was graded

Two scales are used in this record, for two different purposes, plus one code set for unmet needs.
They are written out here so that a reader who disagrees with a row can locate the disagreement
precisely — in the placement, in the criterion, or in the underlying source.

Both scales grade **the state of the evidence**, not the biology. "Failed" means *adequately tested
and did not show benefit*, not *cannot work*. "Poorly studied" means *nobody has looked properly* —
it is not a soft negative.

## Verdict classes — applied to interventions (`data/intervention_register.csv`)

| Class | Meaning |
|---|---|
| **Works** | Replicated benefit in humans, currently used or currently supported |
| **Works — abandoned anyway** | Positive human evidence exists, but the intervention left practice for reasons other than lack of effect (toxicity, cost, displacement, commercial decision) |
| **Conflicting** | Credible sources disagree; the disagreement is preserved rather than resolved |
| **Uncertain** | Positive signal, but the evidence base cannot bear the weight (small trials, no control, no blinding, surrogate outcome, or author-declared low certainty) |
| **Failed** | Adequately tested against a fair comparator and did not show benefit |
| **Harm outweighs benefit** | Effect is real but the safety record makes it indefensible |
| **Poorly studied** | Plausible and unevaluated — the absence of evidence is not evidence of absence |

Two classes are deliberately separated that reviews usually merge. **"Works — abandoned anyway"** is
distinct from "Failed": an intervention with positive trials that left practice for toxicity, cost,
or commercial reasons is a different object from one that was tested and did not work, and only the
first is a candidate for re-examination. **"Conflicting"** is distinct from "Uncertain": conflicting
means two credible bodies of evidence point in opposite directions and the record refuses to pick;
uncertain means one direction is indicated but the evidence cannot support the claim.

## Evidence tiers — applied to statements in the map (`data/treatment_map.csv`)

| Tier | Meaning |
|---|---|
| **Established** | Replicated in humans across independent studies, or a fact about the disease that is not seriously disputed |
| **Probable** | Positive human evidence that is real but limited — single trial, one region, post-hoc, or unreplicated |
| **Uncertain** | Conflicting results, low-quality evidence base, or an effect whose size is not credible as reported |
| **Hypothesis** | Mechanistic, animal, subgroup-derived or uncontrolled — no adequate human test exists |
| **Unknown** | The question has not been asked in a form that could answer it |

The tiers are **not** a single ordered ladder. A row in *what might be worth studying* is not a
weaker version of a row in *what works*; it is a different kind of claim. Sub-labels in the tier
column name the specific reason a row sits where it does — for example *"Uncertain (same trial,
opposite readings)"* — so that placement can be disputed on stated grounds.

## Levels of evidence kept separate

Human randomised trial · human observational · case report or case series · animal · in vitro ·
mechanistic · traditional or historical record · hypothesis.

These are never pooled or averaged. A mechanistic rationale does not raise a tier, and a traditional
record is treated as a source of hypotheses, not as evidence of effect.

## Unmet-need codes

| Code | Unmet need |
|---|---|
| UN1 | Achieving remission beyond first-line therapy / refractory inflammatory disease |
| UN2 | Pain, fatigue and residual symptoms despite controlled inflammation |
| UN3 | Sustained drug-free remission |
| UN4 | Predicting which treatment will work for an individual |
| UN5 | Prevention in at-risk individuals |
| UN6 | Reducing treatment toxicity and comorbidity burden |
| UN7 | ACPA-negative and other subgroup-specific disease |
| UN8 | Repair of existing structural damage |

## Effect sizes

Effect sizes are reported as their source reported them, in the source's own metric, and are not
recalculated, converted, or pooled. No meta-analysis was performed for this record. Where a pooled
estimate is quoted, the heterogeneity is quoted with it; where an effect is not credible as stated,
that is recorded in the `caveat` column rather than resolved.

## The bar for a research lead

A signal was promoted to a research lead only if it survived verification against primary full text
and had a clear, testable reason for further investigation. The failure modes that disqualified
candidates are recorded in `data/lead_candidate_triage.csv`: the apparent gap was a retrieval
artefact; newer evidence already resolves the question; no testable signal exists; or the candidate
is subsumed by another. Each surviving lead states its own falsification criterion — what result
would reject it — in `data/next_steps_specification.csv`.
