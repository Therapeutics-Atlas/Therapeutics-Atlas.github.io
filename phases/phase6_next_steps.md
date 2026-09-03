> **Archived phase report — a dated record of what was believed at the time, not the current state of the project.**
> Statements superseded by later verification are listed in `data/corrections_log.csv`. Check that log before citing anything in this file.
> Current lead status is in `data/research_leads_status.csv`.

# RA Open Therapeutics #001 — Phase 6: Next Research Step for the Two Open Leads

**Scope.** This phase searches for no new leads and repeats no literature review. It asks one question per lead: what is the smallest step that could resolve the uncertainty on which the lead now turns. Priority was given to re-analysis of existing data, retrieval of missing records, and biomarker validation over any new clinical study. One new primary record was retrieved because it was the only way to answer a question the brief posed directly (the TRAFIC registry entry). No treatment is recommended and no efficacy is claimed.

!Phase 6 decision structure for both leads

## RL-01 — Imaging-burden-selected methotrexate interception in at-risk arthralgia

**1. Current hypothesis after verification.** Among people with clinically suspect arthralgia and subclinical joint inflammation, it is the *burden of subclinical MRI inflammation* — not ACPA status — that identifies who benefits from a one-year methotrexate course. Phase 5 verification reframed the lead onto this basis because the 4-year TREAT EARLIER paper states that the risk split within the ACPA-negative group was not prespecified, no interaction test was reported, and no multiplicity adjustment was applied; the 4-year and 5-year analyses rest on the same 66 participants and 13 events.

**2. Most important remaining uncertainty.** Whether MRI inflammatory burden is *predictive* (modifies the treatment effect) or merely *prognostic* (marks who progresses, treated or not). This is the whole lead: an interception strategy needs a marker of who benefits, not a marker of who declines. The published responder analysis (RMD Open 2025, PMID 41558803) reports that patients who responded best to methotrexate in year one were identified by multiple sites of tenosynovitis with or without osteitis, with positive predictive values of 77% and 79% that were similar in ACPA-positive and ACPA-negative participants. That analysis was conducted *within the treated arm* and contains no interaction term, so it cannot distinguish prediction of treatment response from prediction of spontaneous improvement.

**3. Smallest and most informative next step.** A re-analysis of the existing TREAT EARLIER individual-participant data — no new patients, no new imaging, no new scoring. The trial randomised 236 participants (182, 77%, ACPA-negative), 217 (92%) completed 4-year follow-up, and baseline MRI is already RAMRIS-scored. Two nested analyses:

- **(a)** A treatment × continuous MRI-burden interaction on progression to clinical arthritis over four years, in all 236 randomised participants, with ACPA entered as a second interaction term to test whether serology adds anything once burden is in the model.

- **(b)** The decisive cheap check: apply the published responder definition *unchanged to the placebo arm* and compare the resulting PPV/NPV with the published methotrexate-arm values.

**4. Why this rather than a trial.** Everything required already exists and is already measured. No clinical study should be designed until it is known whether the selection marker it would use is predictive at all.

**5. What would strengthen, what would falsify.** *Strengthens:* a significant treatment × burden interaction with the effect concentrated at higher burden, together with a placebo-arm PPV materially below the treated-arm 77–79%. *Falsifies:* no interaction and a placebo-arm PPV close to the treated-arm value — MRI burden would then be prognostic only, the responder analysis would be describing regression toward health rather than drug effect, and the lead loses its stated basis.

**6. Immediate next decision if the step succeeds.** Only this: whether an imaging-burden-selected interception trial is warranted, with the selection threshold read off the interaction analysis rather than chosen by convention. Nothing downstream of that decision is planned here.

**7. Barriers.** Access is discretionary — the 4-year paper's data-sharing statement offers deidentified participant data on request to the corresponding author, considered individually, with no public repository; the statistical analysis plan and protocol of the 2-year analyses are published. Given the post-hoc history of this subgroup, the re-analysis must be preregistered with the interaction model specified in advance. Power is the binding constraint: the index stratum contributed 13 events, and the whole-trial event count over four years was not extractable from the records accessible here — establishing it is the first thing the analysis would do. Finally, the trial's own risk model incorporates MRI findings, so risk category and burden are collinear and the model must use continuous burden rather than the published risk split. It is also possible the Leiden group has this analysis underway; that should be checked before duplicating it.

## RL-02 — Molecular stromal-signature-selected stromal-directed therapy

**1. Current hypothesis after verification.** A fibroblast/stromal-dominant synovial signature marks a treatment-relevant subgroup in which stromal-directed agents could work, and no trial has ever selected patients on such a signature. Phase 5 confirmed the narrow claim (no prospective stromal-signature selection has been done) but weakened the framing: in STRAP, the pauci-immune group's failure was specific to B-cell depletion, and their response to etanercept and tocilizumab matched the other pathotypes.

**2. Most important remaining uncertainty.** Two questions, in this order. *(i)* Does any human efficacy or synovial pharmacodynamic signal for a stromal-directed agent exist at all? *(ii)* Is 'stromal-high' a distinct endotype, or simply a restatement of B-cell-poor synovium — that is, a marker of rituximab non-response rather than of a treatable stromal biology?

**3. Smallest and most informative next steps.**

- **RL-02-A — retrieve the missing TRAFIC evidence first.** This phase pulled the registry record. ISRCTN36667085 lists a target size of 39 (part 1 up to 21 participants, part 2 n=18), an **actual enrolment of 15**, recruitment status *No longer recruiting*, a recorded completion date of **31/12/2023**, and a single linked publication — the 2021 phase 1b paper (PMID 33928262), which reported exactly 15 participants. Part 2 was to measure EULAR and ACR20 response, sublining synovial macrophage number, and RAMRIS at week 12 — precisely the efficacy and pharmacodynamic readouts this lead needs. Against that, the 2021 paper describes the phase 2a efficacy evaluation as *ongoing* at the time of writing, and a targeted search found no publication from it. **The status of the efficacy stage is therefore unresolved in the public record**, and the enrolment figure matching the phase 1b total suggests part 2 may never have enrolled. The step is a records enquiry to the sponsor (Newcastle Hospitals NHS Foundation Trust / Newcastle CTU) and retrieval of the MRC end-of-grant report for MR/L005123/1. Cost is close to zero and the answer changes what follows.

- **RL-02-B — test whether the signature is a real endotype, using cohorts that already exist.** Define a *drug-agnostic* stromal/fibroblast score on baseline synovial RNA-seq in one cohort, lock it, apply it unchanged to the other, and test its association with non-response separately within each drug arm. STRAP randomised 226 patients (etanercept 73, tocilizumab 74, rituximab 79); R4RA randomised 164 (rituximab 83, tocilizumab 81). The published classifiers cannot be reused for this: they were built to predict response to specific drugs, and the object needed here is drug-agnostic.

**4. Why not a new intervention study.** The lead's premise is that a selectable subgroup exists. STRAP's own data already argue against the simplest version of that premise. Selecting patients into a trial on a signature that has not been shown to transfer across cohorts, and whose only demonstrated association is with non-response to one drug class, would test the agent and the biomarker simultaneously and be uninterpretable if it failed.

**5. What would strengthen, what would falsify.** *Strengthens:* the locked score transfers to the held-out cohort and is associated with non-response to at least two mechanistically distinct classes; or a recovered TRAFIC phase 2a shows a synovial pharmacodynamic effect at the maximum tolerated dose. *Falsifies:* the association is confined to rituximab or the score fails to transfer — 'stromal-high' would then be a B-cell-poor marker, not an endotype, and no signature-selected study is justified; or a recovered phase 2a shows no synovial pharmacodynamic effect, which weakens the direction independently of any selection question.

**6. Immediate next decision if the steps succeed.** If the score transfers: whether a prospective signature-stratified biopsy study is justified — and only then whether any stromal-directed agent is actually available to test in it. That second question is not assumed to have an answer.

**7. Barriers.** STRAP and R4RA come from the same investigator group with overlapping pipelines, and STRAP's models were already validated in R4RA, so cross-cohort transfer is only *partly* independent validation — a genuinely external cohort would be better and may not exist. Both hold raw data by request (R4RA's in a non-public repository); both expose interactive exploration interfaces that permit some work without a data transfer agreement. TRAFIC's data beyond the manuscript and appendix are withheld for commercial sensitivity, so even aggregate recovery may be refused. Registry enrolment fields can be stale, so the record is suggestive rather than conclusive. Power is the limiting factor for RL-02-B — multidrug-resistant subsets within arms of 73–83 are small — and should be computed before any data request is made.

## Comparing the two — actionability is not promise

**More actionable now: RL-01.** One dataset, one custodian, one standard statistical test on data already collected and already scored, with a result that is decisive in either direction. RL-02-A is cheaper still — a records enquiry — but its informativeness is contingent: if the phase 2a stage never ran, the enquiry returns nothing to analyse. RL-02-B is a real analysis across two custodians with a power problem that must be settled first.

**More likely to become an effective treatment: not determinable from current evidence.** The two leads are not comparable on that axis and this phase does not rank them. The asymmetry worth stating is structural rather than evidential: RL-01 concerns an established, inexpensive, well-characterised drug in a preventive setting, so a positive interaction result would have a short translational path — but the 4-year and 5-year data leave open whether the effect is prevention or delay, which caps what a positive result could mean. RL-02 concerns an unlicensed mechanism with, at present, **no demonstrated human efficacy signal at all**; its ceiling is unknown in both directions and its path is long. A cheap next step is not evidence of a promising drug, and an expensive next step is not evidence of an unpromising one.

## Does the evidence justify a new experiment or trial?

**No new clinical trial is justified for either lead at this point.** For RL-01 the marker that would define eligibility has not been shown to be predictive. For RL-02 neither the agent's human activity nor the selectability of the target population has been established, and one of those two questions may already have been answered in unreported data. Every step proposed here is a re-analysis, a records retrieval, or a biomarker validation on existing cohorts.

## Added to the project record this phase

- **Open question (retrieval target), RL-02:** the TRAFIC phase 2a efficacy stage has no publication, no linked results, and a registry enrolment figure equal to the phase 1b total, while the phase 1b paper called it ongoing. This is an unresolved discrepancy in the public record, not an established negative — it should be logged as such and revisited if the sponsor responds.

- **Methodological caveat, RL-02:** cross-validation of a synovial signature between STRAP and R4RA is not fully independent validation. Any future claim of 'validated' stromal stratification should state which cohort, which drug, and whether the validation was internal or external.

## Limits of this phase

- No new literature review was performed; the evidence base is the Phase 5 record plus the ten full texts already retrieved, plus one registry record fetched here.

- The TRAFIC conclusion rests on a registry record and the absence of a publication. Registry fields can be incomplete or stale; only the sponsor can settle it.

- Power figures for both proposed analyses are not computed here — the event count for TREAT EARLIER over four years and the multidrug-resistant subset sizes in STRAP/R4RA were not extractable from the accessible records, and establishing them is part of each step rather than a precondition stated in advance.

- Step-by-step specification of each proposed step, with its access route, criteria and barriers: ra_phase6_next_steps_table.csv
