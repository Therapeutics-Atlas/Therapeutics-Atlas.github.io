> **Archived phase report — a dated record of what was believed at the time, not the current state of the project.**
> Statements superseded by later verification are listed in `data/corrections_log.csv`. Check that log before citing anything in this file.
> Current lead status is in `data/research_leads_status.csv`.

# RA Open Therapeutics #001 — Targeted Verification of the Three Surviving Research Leads

**Scope.** This is not a new literature review and does not search for new leads. It tests, against the strongest accessible primary records, the specific claims on which each Phase 5 verdict depends. Ten full texts were retrieved (protocol and statistical sections read directly), and the trial registry was swept for records capable of falsifying the two "no trial exists" claims. Where the primary evidence contradicts the Phase 5 report, the correction is stated explicitly below.

Nothing here is a treatment recommendation and no efficacy claim is made for any intervention named.

!Verification outcomes

*Each row is one check demanded by the verification brief, with the finding read from the primary record named in ra_phase5v_verification_table.csv. Marker direction is this analysis's judgement of the effect on the Phase 5 claim, not a property of the source.*

## Records obtained and records that stayed closed

Full texts read: TREAT EARLIER 4-year analysis (Lancet Rheumatol 2024, PMID 39303731), TREAT EARLIER MRI-responder analysis (RMD Open 2025, PMID 41558803), TREAT EARLIER protocol (Trials 2020, PMID 33076964), STRAP primary (Lancet Rheumatol 2023, PMID 38251532), STRAP deep molecular profiling (Nat Commun 2025, PMID 40603860), R4RA primary (Lancet 2021, PMID 33485455) and R4RA biomarker analysis (Nat Med 2022, PMID 35589854), TRAFIC seliciclib phase 1b (Lancet Rheumatol 2021, PMID 33928262), ARCTIC (BMJ 2016, PMID 27530741), and the difficult-to-treat ultrasound cohort (PMID 42370095).

Not obtained: the TREAT EARLIER primary publication (Lancet 2022, PMID 35871815) and the 5-year analysis (Lancet Rheumatol 2026, PMID 42392130) are both paywalled with no accessible copy; their abstracts remain the only source. The 4-year paper substitutes for most of what the 5-year analysis would have shown, because — as established below — it reports the same participants.

---
## RL-01 — Methotrexate-based interception in ACPA-negative at-risk arthralgia

### Core claim being tested

That within TREAT EARLIER, an otherwise negative trial, a genuine and prespecified subgroup effect exists in ACPA-negative participants at increased risk, sufficient to justify a dedicated interception trial in that population.

### Primary evidence checked

The 4-year analysis (PMID 39303731) in full, including its statistical-analysis section, baseline table and risk-model footnote; the MRI-responder analysis (PMID 41558803) in full; the published protocol (PMID 33076964); the 5-year abstract (PMID 42392130).

### What the full evidence confirms

- The subgroup effect itself is real as reported. In ACPA-negative participants at increased risk, progression to clinical arthritis was 3/35 (9%) on methotrexate versus 10/31 (32%) on placebo.

- Antibody status was a randomisation stratification factor and antibody-stratified subgroup analyses were described in the statistical analysis plan written for the 2-year follow-up.

- The MRI-responder analysis independently supports a treatment effect on imaging inflammatory burden in the at-risk group.

### What it weakens or contradicts

- **The decisive refinement was not prespecified, by the authors' own statement.** The 4-year paper states that the hypothesis about risk stratification *within* the ACPA-negative group was formed before that analysis and was not part of the published analysis plan. The headline subgroup is therefore a prespecified stratification carrying a post-hoc refinement.

- **No treatment-by-antibody interaction test is reported anywhere.** The only interaction term in either paper is a time-by-treatment term used to check linearity in the mixed models. The subgroup claim rests on comparing within-stratum estimates, not on a demonstrated interaction.

- **No multiplicity handling is reported** for any subgroup comparison in either paper.

- **The subgroup is operationally defined by imaging, not by serology.** The risk model has three variables — rheumatoid-factor positivity, number of locations with subclinical MRI inflammation, and MCP-extensor peritendinitis. In the ACPA-negative participants, 65 of the 66 classified as increased risk had more than two MRI-inflamed locations, versus none of the 116 at low risk. The stratum carrying the effect is an imaging-burden stratum that happens to be ACPA-negative.

- **The MRI-responder paper points the same way.** It reports the inflammatory-burden benefit in *both* antibody strata among increased-risk participants, absent only in the low-risk ACPA-negative group, and justifies its stratification on pathophysiological grounds rather than on an observed interaction.

- **The 5-year result is not independent replication.** It is the same 66 participants one year further on: HR 0.27 (95% CI 0.07–0.99) at 4 years becomes HR 0.24 (95% CI 0.07–0.87) at 5 years, on 13 events. Additionally, the increased-risk band defined in the 4-year paper (25–70% predicted risk) does not match how the 5-year abstract describes its risk threshold — a discrepancy that cannot be resolved without the 5-year full text.

### Remaining uncertainty

Whether ACPA status carries any effect-modifying information beyond the imaging burden it is correlated with. Because the ACPA-negative increased-risk group is almost perfectly an MRI-positive group, the two candidate modifiers cannot be separated in this dataset. A formal interaction test on the individual-participant data, and the 5-year full text with its analysis plan, would settle the prespecification and multiplicity questions.

### Verdict — **Reframe**

The signal survives but its stated basis does not. This should no longer be described as an ACPA-negative subgroup finding. The defensible statement is that in clinically suspect arthralgia with a high burden of subclinical MRI inflammation, a one-year methotrexate course was associated with fewer progressions to clinical arthritis in a small, non-prespecified, unadjusted, 13-event comparison, and the imaging effect appears in both antibody strata. Framed that way it remains testable — and the falsifying study becomes an imaging-selected interception trial, not a serology-selected one.

---
## RL-02 — Stromal-directed therapy has never been tested in molecularly selected patients

### Core claim being tested

That stromal-directed agents have been tested in RA, but no therapeutic trial has prospectively selected patients using a molecular stromal signature — so the hypothesis that stromal-high patients are the ones who would benefit has never been given a fair test.

### Primary evidence checked

TRAFIC (PMID 33928262) and its design paper in full; STRAP primary (PMID 38251532) and STRAP deep molecular profiling (PMID 40603860) in full; R4RA primary (PMID 33485455) and biomarker analysis (PMID 35589854) in full; a ClinicalTrials.gov sweep for fibroblast-, stromal-, cell-cycle- and signature-selected RA trials.

### What the full evidence confirms

- **The selection claim holds.** TRAFIC was a non-randomised, open-label dose-finding study (n=15) whose eligibility was disease activity on background anti-TNF therapy, with no molecular selection. The TCK-276 phase 1b (NCT05437419, n=32) was randomised and placebo-controlled but was a 7-day multiple-ascending-dose safety and pharmacokinetic study, again with eligibility by disease activity alone. No interventional RA trial found in the registry selects participants on a stromal or fibroblast molecular signature.

- **TRAFIC's efficacy stage appears never to have been reported.** The design paper describes a single-arm phase 2a stage at the dose established in phase 1b; no publication of that stage was located.

- **The stromal-resistance association is reproducible across independent cohorts.** R4RA identified a fibroblast-stromal signature associated with multidrug resistance, and STRAP independently reports pauci-immune patients failing B-cell depletion.

### What it weakens or contradicts

- **The pauci-immune signal is drug-specific, not global resistance.** STRAP's discussion states that pauci-immune patients had a poor response to rituximab, with none reaching ACR50 or above, but that their response to etanercept and tocilizumab was equivalent to the diffuse-myeloid and lymphomyeloid pathotypes. In a biologic-naive population, the absence of synovial immune cells predicted non-response to B-cell depletion specifically. This is real opposing evidence for framing the pauci-immune pathotype as a treatment-resistant population needing a new drug class.

- **Validation is narrower than the Phase 5 report implied.** STRAP's tocilizumab and rituximab response models were validated in the independent R4RA cohort (AUC 0.713 and 0.786); the etanercept model was not externally validated, and R4RA's own multidrug-resistance model (AUC 0.69) rests on internal nested cross-validation only. There is no validated classifier for response to any stromal-directed agent, because no such agent has been trialled with response as an endpoint.

- **The histological label maps only partially onto molecular structure.** Unsupervised clustering of STRAP RNA-seq gave four clusters that only partially correspond to the three histological pathotypes, with pauci-immune fibroid patients split across two clusters — so "pauci-immune" as read by histology is not a clean stand-in for a stromal molecular signature.

- **Registry coverage is partial.** STRAP, R4RA and TRAFIC are ISRCTN-registered and fall outside the swept registry, so the absence of a signature-selected trial is established for ClinicalTrials.gov and by literature search, not exhaustively.

### Remaining uncertainty

Whether a molecularly defined stromal-high population is genuinely refractory across drug classes, or whether the apparent resistance is an artefact of B-cell-depletion trials enriched for it. Whether TRAFIC's phase 2a stage was run at all, and if so what it showed.

### Verdict — **Confirm, further narrowed**

The claim as narrowed in Phase 5 survives verification. It should now be stated with the drug-specificity caveat attached: the untested question is whether patients selected prospectively on a stromal molecular signature respond to a stromal-directed agent, not whether pauci-immune patients are resistant to treatment in general — STRAP shows they are not, to TNF and IL-6 blockade.

---
## RL-03 — Untested non-immunosuppressive strategy in imaging-negative refractory RA

### Core claim being tested

That a substantial fraction of difficult-to-treat RA patients have high symptom burden without detectable synovitis; that they are nonetheless escalated through immunosuppressive lines; and that no prospective trial has tested withholding escalation or pursuing a non-inflammatory management strategy in them.

### Primary evidence checked

The difficult-to-treat ultrasound cohort in full (PMID 42370095); ARCTIC in full (PMID 27530741); PREDICTRA (PMID 32404343 / NCT02198651); PMID 38085537 on baseline ultrasound and D2T outcome; a registry sweep for de-escalation, tapering and imaging-guided strategy trials in refractory RA.

### What the full evidence confirms

- **The population estimate holds.** Of 85 patients, 45 met difficult-to-treat criteria, of whom 20 (44%) were non-inflammatory refractory. The source is a single-centre retrospective cohort in which scanning covered hands, wrists and symptomatic joints and was performed by one clinician, so the estimate is fragile in precision though not obviously in direction.

### What it weakens or contradicts

- **The imaging classifier is leaky in both directions.** In the same cohort, 17 of 37 (46%) patients classed as *controlled* refractory had subclinical synovitis on ultrasound, and fibromyalgia was common across all groups (48%, 40% and 17.5%). "Imaging-negative" is therefore neither a clean inflammatory-off state nor specific to the refractory group.

- **Imaging has repeatedly failed as a treatment-decision biomarker, in both directions.** ARCTIC concluded that systematic ultrasound in follow-up is not justified — though in early, DMARD-naive RA rather than in refractory disease. PREDICTRA, a randomised phase 4 taper-versus-withdrawal trial in sustained remission, found that baseline MRI inflammation was **not** associated with flare. PMID 38085537 found baseline ultrasound scores did not predict difficult-to-treat outcome. The premise that imaging status can safely select who does or does not need immunosuppression has now failed prospectively three times.

- **The central "no prospective trial" claim is falsified.** NCT05717179 (Italian Society for Rheumatology, n=158, recruiting since February 2023, completion February 2029) randomises patients with CDAI >10 despite DMARD therapy and a maximum of 2 swollen joints out of 44 — essentially the target population — to ultrasound-guided versus clinically guided treatment decisions, with non-inferiority on low disease activity or remission at 24 weeks as the primary endpoint. This is the strategy trial the lead said did not exist. The Phase 5 report's claim was based on a registry sweep that did not retrieve it.

### Remaining uncertainty

NCT05717179 tests *withholding* escalation when imaging is negative; it does not test any positively-directed non-inflammatory management strategy, and its results will not be available for several years. Whether such a strategy helps this population is still untested. But given that imaging status has failed to predict treatment outcome in three prospective settings, the biomarker on which the whole lead depends is now the weak link.

### Verdict — **Downgrade**

The observation that a large minority of difficult-to-treat patients have no detectable synovitis stands and remains clinically important. But the lead's specific research question is already under prospective randomised test, and the classifier it relies on has failed repeatedly as a decision biomarker. This no longer meets the bar for an open Research Lead. It should be carried in the Treatment Map as a documented observation with a pointer to NCT05717179, to be revisited when that trial reports.

---
## Explicit corrections to the Phase 5 report

1. **RL-03's central gap claim was wrong.** The Phase 5 report stated that no prospective trial has tested a de-escalation or non-escalation strategy in imaging-negative refractory RA. NCT05717179 does exactly this. The apparent gap was a retrieval gap.

2. **A citation was misattributed.** The Phase 5 report cited PMID 41328586 as the next-generation cell-cycle-inhibitor trial in RA patients. That record is a review that summarises the trial. The trial itself is a separate randomised, placebo-controlled, multiple-ascending-dose study (PMID 39002122, NCT05437419).

3. **STRAP's stratification was described imprecisely.** Phase 5 called it histological. STRAP's prospective classification used semiquantitative immunohistochemistry scored by a masked pathologist *combined with* a validated 73-gene RNA-seq B-cell panel.

4. **"Externally validated machine-learning signatures" was too broad.** External cohort validation exists for the STRAP-derived tocilizumab and rituximab models in R4RA. It does not exist for the etanercept model, and R4RA's multidrug-resistance model is internally cross-validated only.

5. **RL-01's prespecification status was overstated as unresolved; it is now resolved against the lead.** The 4-year paper states plainly that the risk-stratified analysis within the ACPA-negative group was not in the published analysis plan. No interaction test and no multiplicity adjustment are reported.

6. **RL-01's 5-year and 4-year results are not two pieces of evidence.** They are the same 66 participants at two time points.

---
## Standing after verification

| Lead | Phase 5 | After verification |
|---|---|---|
| RL-01 Methotrexate interception | Survives (reframed) | **Reframe** — imaging-burden-selected, not ACPA-selected; post-hoc, no interaction test, 13 events |
| RL-02 Stromal-signature selection | Survives (narrowed) | **Confirm, further narrowed** — claim holds; pauci-immune resistance is drug-specific |
| RL-03 Imaging-negative refractory RA | Survives | **Downgrade** — question already under randomised test; imaging failed as decision biomarker three times |

Two leads remain open, one on a materially different footing than Phase 5 described. They are not ranked: they concern different populations, different evidence types and different stages of testability.

## Limits of this verification

- Two decisive TREAT EARLIER publications could not be retrieved. Their abstracts, plus the 4-year full text reporting the same participants, are what the RL-01 conclusions rest on.

- No individual-participant data were available, so the interaction tests that RL-01 needs could not be performed here — only their absence in the published record documented.

- Registry coverage is partial in both directions: ISRCTN, EudraCT/CTIS, ChiCTR, UMIN and jRCT were not swept. The RL-02 gap claim is therefore established but not exhaustively.

- Outcome labels in the figure and table are this analysis's judgement of each finding's effect on the Phase 5 claim, not a property of the cited source.
