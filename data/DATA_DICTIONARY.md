# Data dictionary

Every file is UTF-8 CSV with a header row. Free-text cells may contain commas and are quoted.
Numbers and effect sizes are reproduced as their source reported them and are never recalculated.
Where a cell is empty the value was not applicable or not retrievable — the two are distinguished in prose in the phase reports, not in the tables.

## `treatment_map.csv`

The Phase 3 open treatment map. 115 statements in six sections: what works, what does not work, what is uncertain, what we know about the disease, what we do not know, and what might be worth studying. Each row carries an evidence tier and a stated reason for its placement.

115 rows.

| Column | Example value |
|---|---|
| `section` | know |
| `item` | Disease burden |
| `statement` | GBD 2021: 17.6M cases (15.8-20.3), age-standardised prevalence 208.8/100k, +14.1% since 19… |
| `evidence_tier` | Established |
| `unmet_need` | — |
| `reason` | — |
| `source` | PMID 37675071 |
| `reason_class` | — |
| `evidence_tier_ord` | 4.0 |

## `intervention_register.csv`

67 interventions across 12 domains graded on one scale, with the strongest available evidence design, a verbatim key result, an unmet-need code, a caveat, and PMID/DOI. This is the underlying evidence table for the map.

67 rows.

| Column | Example value |
|---|---|
| `domain` | Modern — anchor drugs |
| `intervention` | Methotrexate monotherapy |
| `verdict_class` | Works |
| `verdict_detail` | Established benefit |
| `best_evidence` | Cochrane review |
| `evidence_base` | 7 RCTs, 732 pts |
| `population` | RA vs placebo |
| `outcome` | ACR50 at 52 wk |
| `key_result` | RR 3.0 (95% CI 1.5 to 6.0) |
| `direction` | benefit |
| `certainty` | not stated |
| `unmet_need` | UN1 |
| `caveat` | Placebo-controlled monotherapy data are old and short-term; ~30-40% do not reach low disea… |
| `pmid` | 24916606 |
| `doi` | 10.1002/14651858.CD000957.pub2 |

## `negative_results_register.csv`

17 interventions with a recorded negative result, preserved deliberately.

17 rows.

| Column | Example value |
|---|---|
| `intervention` | Acupuncture versus sham |
| `negative_result` | no significant difference on any outcome (Cochrane; CAM review) |

## `conflicts_register.csv`

9 disagreements between credible sources, with both sides and the reason the conflict is not resolved.

9 rows.

| Column | Example value |
|---|---|
| `conflict` | Acupuncture for RA pain |
| `side_a` | Cochrane and CAM review: no difference vs sham |
| `side_b` | Network meta-analyses: SMD −1.11 to −1.42 vs conventional therapy and non-acupoint sham |
| `status` | Unresolved; disagreement is about control validity |

## `research_leads_status.csv`

Current status of all six research leads, showing what each phase concluded, how verification changed it, the present form of the claim, the next step and what it is blocked on.

6 rows.

| Column | Example value |
|---|---|
| `lead` | RL-01 |
| `question` | Methotrexate-based interception in at-risk arthralgia |
| `phase4` | Research Lead |
| `phase5` | Survives (reframed) |
| `verification` | Reframe |
| `current_status` | OPEN — reframed |
| `current_form` | Selection is by baseline MRI inflammatory burden (multiple sites of tenosynovitis with or … |
| `next_step` | Re-analysis of existing individual-participant data: does baseline MRI burden modify treat… |
| `blocked_on` | Discretionary data request to the trial's corresponding author; no repository route exists… |

## `corrections_log.csv`

Nine statements this project made and then retracted, with the correction, its cause, and the identifiers involved. C-series raised in Phase 5; V-series raised in targeted verification.

9 rows.

| Column | Example value |
|---|---|
| `id` | C1 |
| `raised_in` | Phase 5 |
| `corrects` | Phase 4 (RL-02) |
| `superseded_statement` | No interventional stromal- or fibroblast-directed trial had been conducted in RA. |
| `correction` | False. TRAFIC was an open-label phase 1b dose-finding study of the CDK inhibitor selicicli… |
| `cause` | The Phase 4 registry sweep used fibroblast, anti-fibrotic and FAP terms and missed cell-cy… |
| `key_ids` | PMID 33928262; ISRCTN36667085 |

## `lead_candidate_triage.csv`

All 22 candidate signals considered for lead status, with outcome and reason for rejection.

22 rows.

| Column | Example value |
|---|---|
| `key` | acpa_neg_prevention |
| `signal` | MTX interception in ACPA-negative at-risk arthralgia |
| `phase3_evidence_tier` | human RCT (post-hoc/stratified) |
| `triage_outcome` | LEAD |
| `triage_note` | RL-01 |
| `key_evidence` | TREAT EARLIER 4-yr PMID 39303731; 5-yr ACPA-stratified PMID 42392130; comparator preventio… |

## `lead_verdicts_phase5.csv`

Phase 5 verdicts per lead before targeted verification. Superseded in part by the verification round; kept for audit.

6 rows.

| Column | Example value |
|---|---|
| `lead` | RL-01 |
| `title` | Methotrexate-based interception in ACPA-negative at-risk arthralgia |
| `verdict` | SURVIVES (reframed) |
| `deciding_evidence` | TREAT EARLIER 5-year ACPA-stratified analysis (PMID 42392130): 3/35 (9%) vs 10/31 (32%) pr… |
| `strongest_opposing` | Same-trial MRI responder analysis (PMID 41558803): MRI treatment response was predicted by… |
| `critical_uncertainty` | Whether the ACPA-negative advantage is a differential treatment effect or a difference in … |
| `hypothesis` | In ACPA-negative individuals with clinically suspect arthralgia, subclinical joint inflamm… |
| `next_step` | A prospective interception RCT enrolling ACPA-negative CSA with MRI-confirmed multi-site t… |

## `verification_checks.csv`

Each claim checked against primary full text during targeted verification, with the outcome per claim.

16 rows.

| Column | Example value |
|---|---|
| `lead` | RL-01 |
| `lead_claim` | Methotrexate interception in ACPA-negative at-risk arthralgia |
| `check` | Subgroup prespecified? |
| `outcome` | partly confirmed |
| `finding` | ACPA-stratified analyses in the published 2-yr SAP; risk-split within ACPA-negative formed… |
| `verdict` | REFRAME |
| `primary_source` | PMID 39303731 (4-yr TREAT EARLIER, full text) |

## `next_steps_specification.csv`

The proposed next step for each open lead, with data source, access route, strengthen and falsify criteria, and known barriers.

3 rows.

| Column | Example value |
|---|---|
| `lead` | RL-01 |
| `step_id` | RL-01-A |
| `step_type` | Re-analysis of existing IPD (no new data collection) |
| `question` | Does baseline MRI inflammatory burden modify the effect of methotrexate, or only predict p… |
| `data_or_record` | TREAT EARLIER randomised trial: 236 randomised, 217 (92%) completed 4-year follow-up, 182 … |
| `custodian_access_route` | Deidentified participant data on request to the corresponding author, considered on an ind… |
| `analysis_or_action` | Cox model on progression to clinical arthritis over 4 years with a treatment x continuous … |
| `strengthen_criterion` | Interaction term significant with effect concentrated at higher burden AND placebo-arm PPV… |
| `falsify_criterion` | No interaction AND placebo-arm PPV similar to methotrexate-arm PPV: burden is prognostic, … |
| `immediate_next_decision` | If predictive: decide whether an imaging-burden-selected interception trial is warranted a… |
| `main_barrier` | Access is discretionary; the analysis must be preregistered given the post-hoc history of … |
| `source_verified` | Lancet Rheumatol 2024 4-year analysis (data-sharing statement, Findings); RMD Open 2025 re… |

## `public_record_check.csv`

Each public source checked when establishing whether the two next steps can be executed without contacting the original teams, and whether it closes its question.

14 rows.

| Column | Example value |
|---|---|
| `lead` | RL-01 |
| `source` | Lancet Rheumatol 2024, 4-year TREAT EARLIER (PMID 39303731) — data-sharing statement |
| `finding` | Requests for deidentified participant data can be made to the corresponding author on publ… |
| `enables` | Identifies the only access route; no repository, no standing access policy. |
| `public_only` | no |

## `open_questions.csv`

Ten open questions carried forward from the Phase 1 baseline review.

10 rows.

| Column | Example value |
|---|---|
| `rank` | 1 |
| `question` | Which patients can safely stop treatment, and can that group be enlarged? |
| `why_it_matters` | Withdrawal trials are run in bDMARD-treated populations, in which sustained drug-free remi… |
| `what_would_resolve_it` | Withdrawal RCT enriched for never-bDMARD, autoantibody-negative patients in sustained remi… |
| `current_evidence_tier` | Uncertain (ascertainment bias argued, not proven) |
| `key_sources_doi` | 10.1016/S2665-9913(24)00234-0; 10.1136/ard-2023-224476 |

## `references.csv`

77 references with identifiers.

77 rows.

| Column | Example value |
|---|---|
| `doi` | 10.1016/j.ard.2026.01.023 |
| `pmid` | 41826212 |
| `year` | 2026.0 |
| `journal` | Annals of the rheumatic diseases |
| `title` | EULAR recommendations for the management of rheumatoid arthritis with synthetic and biolog… |
| `evidence_level` | Guideline |
| `topic` | Treatment |
| `key_finding` | 2025 EULAR update: 5 principles, 9 recommendations; MTX + short-term GC first line; bDMARD… |
