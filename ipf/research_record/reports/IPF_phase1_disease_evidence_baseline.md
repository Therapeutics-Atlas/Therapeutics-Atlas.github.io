# Phase 1 — Disease Evidence Baseline: Idiopathic Pulmonary Fibrosis

**Open Therapeutics · IPF Open Evidence Record · Phase 1 of 6.**
Written 2026-09-02. Preserved unedited; later corrections are recorded in `corrections_log.csv`
rather than by rewriting this text.

**Scope binding.** This phase is governed by `IPF_SCOPE.md` (fixed 2026-09-02 after the Phase 0
verdict `GO WITH SCOPE LIMITS`) and by its six limits L1–L6: IPF only, with non-IPF fibrosis
admitted solely as labelled indirect evidence (L1); human clinical evidence as the spine, with
preclinical work never supporting an efficacy statement (L2); outcome dimensions kept separate as
schema fields, never pooled or converted (L3); traditional-medicine evidence handled as a
prespecified screening task in a later phase (L4); a dedicated register for completed-but-unreadable
studies, with missing results never read as absence of effect (L5); a retrieval date on every row
and explicit supersession marking (L6).

**What this phase does and does not do.** Phase 1 establishes what is known about the disease
itself, what current care achieves, and where that achievement stops — in numbers, not adjectives.
It ends in a coded list of unmet needs (UN1–UN12) that every later phase maps onto. It does **not**
map interventions (Phase 2), grade them (Phase 3) or propose research leads (Phase 4). No lead is
proposed here, and none should be read out of this document.

**Retrieval provenance.** All searches were run 2026-09-02 against PubMed (E-utilities) and
ClinicalTrials.gov API v2. The trial-registry backbone is the Phase 0 pull (`ipf_ctg_raw.csv`,
632 studies, retrieved 2026-09-02), re-queried for completion and results-posting dates. Search
strings, retrieved PMIDs and per-row retrieval dates are preserved in the data files listed in
§9. Two guideline documents were sought in primary full text: the 2022 diagnosis guideline was
retrieved (PMID 35486072); the 2015 treatment guideline (PMID 26177183) could not be retrieved
through any available route, so its individual recommendation strengths are **not quoted** here.

---

## 1. The endpoint-and-metric taxonomy (built first, deliberately)

The Phase 0 verdict required this before any intervention is described, because IPF trials report
several mutually non-convertible measures of the same clinical idea. The taxonomy is
`ipf_phase1_endpoint_taxonomy.csv` — 15 endpoint rows (E1–E15) across 12 outcome dimensions. Each
row records the measure, its metric variants, the threshold or MCID with its source, what a positive
result **licenses**, what it **does not license**, the known problems of the measure, and the
evidence level of the threshold itself.

The five findings that constrain every later reading of the evidence:

**1.1 There are four incompatible ways to express lung-function change**, and they are used
interchangeably in the literature: absolute mL change (E1), % predicted change (E2), categorical
relative decline ≥10% (E3), and slope. E1 has **no MCID defined in mL at all** — the MCID exists
only in % predicted (2–6 %pred, PMID 21940789). Placebo-arm decline differs roughly three-fold
across pivotal trials, so cross-trial comparison of mL differences is not valid. E3's relative and
absolute definitions "are not interchangeable; choice changes both event rate and effect estimate".

**1.2 The MCIDs are contested, and in one case the disagreement decides trial outcomes.** K-BILD
(E7) has a published MID of 8 units and a later estimate of 4.7 for improvement / 2.7 for
deterioration (PMID 23867809; PMID 32316976) — "a trial can be 'positive' or 'null' depending on
which is adopted". SGRQ-I is directional (3.9 improvement / 4.9 deterioration, PMID 32316976).
UCSD-SOBQ worsening MCID is 4–6, point estimate 6, derived in mild-to-moderate impairment
(PMID 42548365). FVC %pred MCIDs are anchored largely on death and hospitalisation and were
re-estimated substantially higher by anchor-only methods (PMID 34671666). Both disagreements are
preserved in the taxonomy rather than resolved.

**1.3 Trial-level surrogacy of lung function for mortality was not established by anything this
search retrieved.** Two separate searches for surrogate-endpoint validation returned biomarker
studies and position papers, not a trial-level validation. This is recorded as *not established in
retrieved evidence*, which is not the same as *refuted*. Consequently no FVC result in this record
may be read as a survival claim.

**1.4 The acute-exacerbation endpoint changed under the field's feet.** The 2016 revised definition
(PMID 27299520) "alters both numerator and prognosis, so historical and modern rates are not
comparable"; reported incidence varies widely (3-year 18.6%, PMID 39256473).

**1.5 There is no human endpoint for recovery or reversal.** E15 exists only to record the absence:
no established measure, no trial precedent, no regulatory pathway. Quantitative HRCT (E13) has no
accepted MCID, is not a registration endpoint, and its methods are not standardised across centres.

This taxonomy is the schema for Phases 2–3: an intervention row must state which E-code it moved,
under which metric variant, and over what duration.

---

## 2. Disease baseline

| Item | Value | Source |
|---|---|---|
| Definition | Progressive fibrosing interstitial pneumonia of unknown cause, defined by a usual interstitial pneumonia (UIP) pattern | 2022 ATS/ERS/JRS/ALAT guideline, PMID 35486072 |
| Pooled global incidence | 5.8 per 100,000 (95% CI 4.8–6.8; 23 studies) | PMID 40775309 (2025 SLR + meta-analysis) |
| Pooled global prevalence | 17.7 per 100,000 (95% CI 14.0–21.5; 20 studies); North America 27.2, Europe 14.6, Asia 14.8 | PMID 40775309 |
| Median survival, pre-antifibrotic era | 4.2 years (population-based) / 4.1 years (referral cohort) | PMID 9713446 (1998) |
| Mortality in modern trial populations | 6.6% at 1 year; 13.7% at 2 years | PMID 24476390 |
| Registry cumulative mortality | 5%, 24%, 37%, 44% at years 1–4 | AIPFR, PMID 28232409 |
| Acute exacerbation, 3-year incidence | 18.6% | PMID 39256473 |
| In-hospital mortality after acute exacerbation | ~29.5% | PMID 35614114 |
| Prognostic stratification | GAP stage III vs I: HR 4.64 | AIPFR, PMID 28232409 |
| Comorbidity burden | Pulmonary hypertension HR 2.0; lung cancer HR 2.6 for mortality | EMPIRE registry, PMID 30170904 |

Two things follow for the record. First, **trial populations are not the disease population**:
1–2-year mortality in trials (6.6% / 13.7%) is far below registry mortality (5% / 24%), which is
why mortality endpoints are hard to power in the enrolled population and why the evidence base is
concentrated in mild-to-moderate physiologic impairment (UN9). Second, **the natural-history
figures most often quoted (median survival ~4 years) predate antifibrotic therapy** and are dated
1998; under L6 they are labelled as era-specific and must not be presented as the current
prognosis.

---

## 3. Current standard of care

Full table with harms, sources and per-dimension evidence: `ipf_phase1_standard_of_care.csv`.

| Intervention | Category | Status (as of 2026-09-02, L6) | Best documented effect |
|---|---|---|---|
| Nintedanib | Approved, disease-directed | Approved for IPF; 2015 guideline made a conditional recommendation (recommendation text not retrievable — see §6) | FVC decline rate (RCT) |
| Pirfenidone | Approved, disease-directed | Approved for IPF; 2015 guideline conditional recommendation | Categorical progression (RCT) |
| Nerandomilast | Approved 2025, disease-directed | FDA approved December 2025 for progressive pulmonary fibrosis — a **PPF-wide label**, not IPF-specific; IPF trial is FIBRONEER-IPF | FVC decline rate (RCT) |
| Inhaled treprostinil | Phase 3 positive in IPF | Two positive phase 3 IPF trials reported 2026; regulatory status for IPF not established in retrieved evidence | FVC decline rate (RCT, median change) |
| Antacid medication / antireflux surgery | Adjunctive | **Conditional recommendations against both** for treating IPF (2022 guideline) | None demonstrated for disease course |
| Lung transplantation | Definitive | Standard of care for eligible patients; no randomised comparison exists | Survival (observational) |
| Pulmonary rehabilitation | Non-pharmacological | Standard supportive care; retrieved evidence base is a Cochrane review of ILD, **not IPF-exclusive** (indirect under L1) | Functional capacity / HRQoL, short term |
| Low-dose morphine | Symptom-directed (cough) | Randomised crossover evidence in IPF; not a guideline-recommended standard | Cough frequency at 14 days |
| Supplemental oxygen | Supportive | Widely used; IPF-specific randomised survival evidence not identified by this search | Not established in retrieved IPF-specific evidence |
| Prednisone + azathioprine + NAC | **Abandoned — harm** | Withdrawn after interim harm; recommended in practice before 2012 | Harm (RCT, interim) |

Note the boundary problem this creates and which L1 exists to contain: the most recent approval in
this field carries a PPF-wide label. Evidence generated in mixed PPF/ILD populations enters this
record only as labelled indirect evidence, with the study population stated on the row.

---

## 4. Where treatment reaches its ceiling

Per-dimension table with sources, evidence tier and what remains unachieved:
`ipf_phase1_ceiling.csv`.

![Strongest retrieved human evidence per outcome dimension in IPF. Each row is one outcome dimension; position on the horizontal scale is the strongest class of human evidence retrieved for that dimension, and the annotation is the best documented number. Numbers are not comparable across rows: they are different metrics on different scales, per L3.]({{artifact:art_6aa17415-696c-40eb-9163-71b2638a3158}})

The numbers, by dimension:

1. **Rate of FVC decline (continuous).** Largest 52-week between-group difference in a phase 3 IPF
   trial: **130.1 mL (95% CI 82.2–178.1)**, inhaled treprostinil vs placebo, median change −43.3 vs
   −196.2 mL (TETON-1, NCT04708782, PMID 42149993). Every active arm of every positive trial still
   declines; across positive phase 3 arms, active-arm change ranges from −43.3 to −138.6 mL/52 wk.
2. **Prevention of categorical progression.** **47.9% relative reduction** in the proportion with
   ≥10-point FVC %pred decline or death at 52 weeks (ASCEND, NCT01366209, PMID 24836312). No trial
   has shown progression can be prevented outright; residual progression in treated arms remains
   substantial.
3. **Recovery of lost lung function.** Least-declining active arm reported anywhere: **−21.5 mL over
   26 weeks** (deupirfenidone 825 mg, ELEVATE-IPF, NCT05321420, PMID 42085224). No completed IPF RCT
   arm has reported a sustained positive change in FVC.
4. **Reversal of established fibrosis.** No result, because no endpoint (E15).
5. **Acute exacerbation.** Pooled **RR 0.63 (95% CI 0.53–0.76, I² = 0%)** with antifibrotic therapy
   (PMID 34217681) — predominantly observational. The TETON-1/-2 exacerbation endpoints were
   hierarchy-stopped, i.e. **not formally tested**, which under L3 is recorded as untested rather
   than as null.
6. **Cough.** **39.4% reduction** in objective awake cough frequency (95% CI −54.4 to −19.4;
   p = 0.0005) with low-dose morphine at day 14 (PACIFY COUGH, NCT04429516, PMID 38237620, n = 44).
7. **Dyspnoea / health-related quality of life.** No intervention has shown a difference exceeding
   the relevant MCID in a pivotal IPF trial in retrieved evidence (e.g. INSTAGE SGRQ −1.28 vs
   −0.36, null; PMID 30220235).
8. **Functional capacity.** No positive pivotal result (STEP-IPF: ≥20% 6MWD improvement 10% vs 7%,
   not significant; PMID 20484178).
9. **Survival.** **No randomised evidence of a survival benefit for any drug.** Best available:
   pooled RR 0.55 (95% CI 0.45–0.66, I² = 82%, mostly observational; PMID 34217681); registry
   HR 0.56 (0.34–0.92; PMID 28232409); causal-inference cohort HR 0.53 (0.28–1.03, p = 0.060;
   PMID 36997445).
10. **Durability.** Randomised comparison is limited to about **52 weeks** for every currently
    approved or recently positive agent.
11. **Definitive treatment.** Lung transplantation: **5-year survival 55.2%** in the most recent era
    analysed, up from 51.9% (p = 0.02), adjusted HR 0.83 (0.76–0.91) for the later era
    (PMID 37625610). It replaces the lung rather than treating the disease, and is bounded by
    candidacy and organ supply.
12. **Cure or durable remission.** None reported in any retrieved human evidence.

**The shape of the ceiling.** Phase 3 randomised evidence in IPF exists for exactly one thing: the
*rate* at which a surrogate declines, over one year. Everything patients experience — breathlessness,
quality of life, exercise capacity — is either untested at pivotal scale or tested and null. Survival
and exacerbation benefits are observational. Recovery, reversal, remission and cure have no positive
result, and two of them have no endpoint. Under L3 these are twelve separate claims about twelve
separate dimensions and none of them substitutes for another.

---

## 5. The retrievability problem (preserved, not resolved)

Register: `ipf_phase1_retrievability_register.csv` (149 rows, one per completed interventional
study without posted results, each with completion date, months since completion, linked PubMed
records, what was searched, classification and retrieval date).

![Reporting status of completed interventional IPF studies by registry-recorded completion date. Classification combines registry results-posting with PubMed linkage by trial identifier; "publication likely" means a linked record dated at or after completion whose primary-outcome status was not verified. Registry pull and PubMed linkage retrieved 2026-09-02.]({{artifact:art_073a5a56-fa7e-4c11-92df-4e90f6c27f2c}})

Of **239 completed interventional IPF studies** in the registry pull:

- **90** have results posted on ClinicalTrials.gov;
- **39** have no posted results but have a PubMed record dated at or after completion and linked to
  the trial identifier — classified *publication likely, primary outcome unverified*;
- **110** have neither. Of these, **97 completed more than 12 months ago**, together enrolling
  **4,182 participants**, and **21 of the 97 were phase 2 or phase 3**. The remaining 13 are within
  a 12-month reporting window and are not counted as reporting failures.

Method and its limits: classification compares publication year against registry completion year,
because linkage alone is misleading — the exemplar case (PRECISIONS, NCT04300920) links only to a
design paper published years before completion. "No results found" therefore means: no posted
registry results, and no trial-identifier-linked PubMed record dated at or after completion, as of
2026-09-02. It does **not** mean no publication exists; a paper that omits the trial identifier, is
not indexed in PubMed, or appears in a non-indexed venue would be missed. Under L5 none of these
110 studies may be read as a negative result, and none may be read as a positive one.

**Why this belongs in the baseline rather than in a later phase.** Any Phase 2 treatment landscape
built only from retrievable evidence would be built on 54% of the completed randomised record
(129 of 239 with posted results or a likely publication). The register makes the missing half
visible as a named quantity so later phases can state what fraction of the evidence on any given
intervention is unreadable, and so the deficit is not silently absorbed into "no evidence of
benefit".

---

## 6. What Phase 1 could not establish

Recorded as uncertainty, per project principle 11:

- **Trial-level surrogacy of FVC for mortality** — not established in retrieved evidence; two
  targeted searches returned no validation study. Not refuted either.
- **The 2015 treatment guideline's individual recommendation strengths** — PMID 26177183 full text
  was not retrievable through open-access, PMC or publisher routes. Nintedanib and pirfenidone are
  recorded as conditionally recommended (a statement traceable to secondary sources) but the
  recommendation text is not quoted from primary full text, and the strength of each individual
  recommendation is treated as unverified.
- **IPF-specific randomised evidence for supplemental oxygen** — none identified by this search;
  absence of retrieval, not demonstrated absence.
- **Regulatory status of inhaled treprostinil for IPF** — not established in retrieved evidence as
  of 2026-09-02.
- **Whether any MCID transfers across severity strata** — the retrieved MCID studies are derived in
  mild-to-moderate impairment and in trial cohorts.
- **Primary-outcome content of the 39 "publication likely" trials** — linkage was verified, the
  papers' primary outcomes were not.

---

## 7. Unmet needs (UN1–UN12)

Full table with dimension, endpoint codes, evidence basis and status:
`ipf_phase1_unmet_needs.csv`. Every later phase maps onto these codes.

| Code | Unmet need | Dimension | Endpoints |
|---|---|---|---|
| UN1 | No intervention has been shown to recover lost lung function; the best active arm still declines | Recovery | E1, E2, E15 |
| UN2 | Reversal of established fibrosis has never been demonstrated, measured or defined as a human endpoint | Reversal | E13, E15 |
| UN3 | No randomised evidence that any drug prolongs survival | Survival | E11 |
| UN4 | No intervention has shown a dyspnoea or HRQoL benefit exceeding the relevant MCID in a pivotal trial | Symptoms / HRQoL | E6, E7, E8 |
| UN5 | Cough has one small, 14-day randomised positive result and no durable treatment | Symptoms (cough) | E9 |
| UN6 | No adequately powered randomised evidence for preventing or treating acute exacerbations; the one randomised treatment attempt signalled harm | Acute exacerbation | E10 |
| UN7 | Durability of effect beyond 52 weeks has never been randomised | Durability | E1, E14 |
| UN8 | The field's endpoint methodology is unresolved: incompatible metrics, contested MCIDs, no retrieved surrogacy validation | Measurement | E1–E3, E6, E7 |
| UN9 | The randomised evidence base is concentrated in mild-to-moderate impairment; severe disease is under-represented | Population coverage | E2, E5, E8 |
| UN10 | Results of 110 of 239 completed trials cannot be found; 97 (4,182 participants) are beyond the reporting window | Retrievability | all |
| UN11 | No validated predictive biomarker identifies who benefits from what; the one prospective genotype-selected trial has not reported | Response heterogeneity | E1, E2 |
| UN12 | Non-pharmacological and supportive-care evidence is largely ILD-wide rather than IPF-specific | Supportive care | E5, E6 |

UN8 and UN10 are methodological rather than biological, and both are prior to the others: UN8
determines whether any claim about UN1–UN7 can be interpreted, and UN10 determines how much of the
existing answer is readable at all.

---

## 8. Corrections entered in this phase

`corrections_log.csv`, three entries:

- **C1** — Phase 0's open question Q3 called PRECISIONS (NCT04300920) "unretrievable". The registry
  completion date is 2026-03-02, so the trial is **within** the 12-month reporting window;
  reclassified to *no results found (within reporting window)*. Phase 0's underlying statements
  (completed, no results posted, only a design paper indexed) remain accurate. Q3 remains open.
- **C2** — Phase 0's "129 completed since 2010 without posted results" counted by trial **start**
  date. By registry-recorded **completion** date the figure is 134, of which 102 also lack any
  post-completion publication. Phase 1's counts (239 / 90 / 39 / 110 / 97) supersede the Phase 0
  counts for all retrievability claims.
- **C3** — `scope_limits.csv` v1 merged retrievability and dating into one limit; `IPF_SCOPE.md`
  separates them as L5 and L6, and the register file was reissued with six rows to match.

Per project principle 12, later phases use the corrected forms.

---

## 9. Files produced by this phase

| File | Contents |
|---|---|
| `ipf_phase1_endpoint_taxonomy.csv` | E1–E15: measure, metric variants, threshold/MCID + source, licenses / does not license, known problems, evidence level |
| `ipf_phase1_ceiling.csv` | 12 outcome dimensions: best documented human result, source, evidence tier, what remains unachieved, comparability caveat |
| `ipf_phase1_standard_of_care.csv` | 10 current or abandoned care elements: status, dimensions with and without evidence, best number, harms |
| `ipf_phase1_retrievability_register.csv` | 149 completed studies without posted results: dates, linkage, classification, what was searched, retrieval date |
| `ipf_phase1_unmet_needs.csv` | UN1–UN12 with endpoint mapping and evidence basis |
| `corrections_log.csv` | C1–C3 |
| `fig1_ipf_phase1_ceiling.png` | Strongest retrieved evidence class per outcome dimension |
| `fig2_ipf_phase1_retrievability.png` | Reporting status of completed trials by completion era |

## 10. Limitations of this phase

Search was single-database (PubMed) plus one registry (ClinicalTrials.gov); EU CTR, jRCT, ChiCTR
and CTRI were not searched, so the retrievability register is a lower bound on unreported work and
may over-count non-reporting for trials registered elsewhere. Ceiling numbers were curated from the
Phase 0 pivotal-trial register plus this phase's retrieval; they are the best *retrieved* results,
not a systematic-review-grade best-evidence synthesis, and a formal Phase 2 landscape may add
agents this phase did not see. Trial classification in the register is algorithmic (date and
identifier linkage) and was adjudicated by hand only for the exemplar case. Numbers across
dimensions in §4 are not comparable with one another by construction (L3). No traditional-medicine
evidence was screened in this phase, by design (L4).
