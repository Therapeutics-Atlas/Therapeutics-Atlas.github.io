# Phase 0 — Disease Selection Reconnaissance: Idiopathic Pulmonary Fibrosis (IPF)

**Open Therapeutics · Phase 0 only.** This document assesses whether IPF is a suitable next
disease for a full Open Evidence Record. It is **not** a Treatment Map, contains **no Research
Leads**, and makes **no efficacy, safety or treatment recommendation**. It is not medical advice.

Assessment date: **2026-09-02**. Searches: ClinicalTrials.gov API v2 (condition = idiopathic
pulmonary fibrosis, retrieved 2026-09-02, n = 632 studies) and PubMed E-utilities (esearch/efetch).
Raw pulls: `ipf_ctg_raw.csv`, `ipf_pubmed.json`, `ipf_phase0_registry_summary.json`,
`ipf_phase0_volume.json`. Every quantitative claim below carries an NCT number or PMID.

---

## 1. Disease overview

| Item | Value | Source |
|---|---|---|
| Nature | Progressive fibrosing interstitial lung disease of unknown cause, defined by a usual interstitial pneumonia (UIP) pattern | ATS/ERS/JRS/ALAT guideline 2022, PMID 35486072 |
| Pooled global incidence | 5.8 per 100,000 (95% CI 4.8–6.8; 23 studies) | PMID 40775309 (SLR + meta-analysis, 2025) |
| Pooled global prevalence | 17.7 per 100,000 (95% CI 14.0–21.5; 20 studies); North America 27.2, Europe 14.6, Asia 14.8 | PMID 40775309 |
| Mortality in trial populations | 6.6% at 1 year, 13.7% at 2 years | PMID 24476390 (pooled placebo/control arms) |
| Course | Monotonic loss of lung function punctuated by acute exacerbations; no described state of spontaneous or drug-induced remission | PMID 35486072 |

Two structural features matter for this assessment. First, IPF is **rare** (≈18/100,000), which
caps trial size and makes mortality-powered trials arithmetically hard: with the observed 2-year
mortality, a two-arm trial needs ~508 events for 90% power to detect a 25% mortality reduction
(PMID 24476390). Second, the disease has **no remission construct at all** — unlike rheumatoid
arthritis, where "remission" exists as an operational definition, IPF has no state that any
guideline or trial defines as disease-inactive. This changes what an Open Treatment Map for IPF
can even claim.

---

## 2. The therapeutic ceiling — what the best available treatment actually achieves

Three drugs are approved for IPF in the United States: pirfenidone and nintedanib (both 2014) and
nerandomilast, a preferential PDE4B inhibitor approved in December 2025 — the first new IPF
approval in over a decade (FDA and manufacturer announcements, December 2025).

Curated primary results for 23 pivotal or landmark interventions are in
`ipf_phase0_pivotal_trials.csv` (verbatim result strings, NCT + PMID per row). The quantitative
ceiling:

| Regimen | Trial (year) | FVC metric | Difference vs placebo | Source |
|---|---|---|---|---|
| Nintedanib | INPULSIS-1 (2014) | annual rate of decline | **+125.3 mL** (95% CI 77.7–172.8) | PMID 24836310 |
| Nintedanib | INPULSIS-2 (2014) | annual rate of decline | **+93.7 mL** (44.8–142.7) | PMID 24836310 |
| Nerandomilast 18 mg | FIBRONEER-IPF (2025) | absolute change, 52 wk | **+68.8 mL** (30.3–107.4) | PMID 40387033 |
| Nerandomilast 9 mg | FIBRONEER-IPF (2025) | absolute change, 52 wk | **+44.9 mL** (6.4–83.3) | PMID 40387033 |
| Inhaled treprostinil | TETON-1 (2026) | median change, 52 wk | **+130.1 mL** (82.2–178.1) | PMID 42149993 |
| Inhaled treprostinil | TETON-2 (2026) | median change, 52 wk | **+95.6 mL** (52.2–139.0) | PMID 41812190 |
| Deupirfenidone 825 mg | ELEVATE-IPF (2026, phase 2b) | rate of change, 26 wk | **+91.0 mL** (12.2–169.7) | PMID 42085224 |
| Pirfenidone | ASCEND (2014) | categorical (≥10-point FVC%pred decline or death) | relative reduction **47.9%** | PMID 24836312 |

**Findings that constrain the ceiling.**

1. **Every drug that beats placebo does so by 45–130 mL of FVC.** Twelve years and three
   approvals apart, the effect sizes are the same order of magnitude (fig 1a).
2. **No regimen stops decline.** In every trial the active arm still loses lung function
   (fig 1b). The single active arm approaching zero decline (deupirfenidone 825 mg, −21.5 mL) was
   measured over 26 weeks in a phase 2b trial, not 52 weeks.
3. **Nothing has restored lost function.** No completed IPF RCT reports recovery of previously
   lost FVC. Reversal of established fibrosis remains a preclinical hypothesis.
4. **Survival evidence is indirect.** ASCEND showed no significant all-cause mortality difference
   (P = 0.10); significance appeared only in a prespecified pooled analysis with two earlier trials
   (P = 0.01) (PMID 24836312). A meta-analysis reports pooled RR 0.55 (0.45–0.66) for all-cause
   mortality with antifibrotic treatment (PMID 34217681) — a pooled estimate across heterogeneous
   trials, not a trial result.
5. **Secondary endpoints repeatedly fail even when FVC succeeds.** Both TETON trials met FVC
   convincingly but showed no substantial difference in time to acute exacerbation, which stopped
   the testing hierarchy (PMID 42149993, 41812190). Nintedanib's exacerbation results ran in
   opposite directions in its two identical trials (HR 1.15 in INPULSIS-1 vs 0.38 in INPULSIS-2).
6. **Tolerability is a real cost.** Diarrhoea 41.3% vs 16.0% (nerandomilast); cough 54.8% vs 33.1%
   and discontinuation 40.5% vs 32.8% (TETON-1).
7. **Transplantation** remains the only intervention that changes the trajectory rather than its
   slope; its comparative survival effect was not quantified in this reconnaissance.

**Ceiling statement.** Current best therapy *slows measured lung-function decline by a
millilitre-scale margin*. It does not prevent progression, preserve function, restore function,
reverse fibrosis, induce remission, or cure. Whether it prolongs survival is supported by pooled
and observational evidence, not by any single adequately powered trial.

![Therapeutic ceiling in IPF]({{artifact:art_eb3bf65e-91f9-4b37-b3a3-a08e70d2c1be}})

---

## 3. Evidence base richness

| Measure | IPF | RA (completed record) | Ratio |
|---|---|---|---|
| PubMed records | 18,308 | 186,017 | 10.2× |
| Randomised-controlled-trial publications | 305 | 4,806 | 15.8× |
| Meta-analyses / systematic reviews | 291 | — | — |
| Guideline-type publications | 34 | — | — |
| TCM-tagged (MeSH) publications | 103 | — | — |

Registry (ClinicalTrials.gov, 2026-09-02): **632 studies** — 430 interventional, 198
observational. Interventional by phase: phase 1 96, phase 1/2 14, phase 2 146, phase 2/3 7,
phase 3 57, phase 4 12, early phase 1 10, not applicable 88. **488 distinct intervention
strings**; 324 trials include a DRUG intervention, 69 OTHER, 23 DEVICE, 22 BIOLOGICAL,
15 PROCEDURE, 12 BEHAVIORAL, 2 DIETARY_SUPPLEMENT. Trial starts by era: 18 (2000–04),
33 (2005–09), 69 (2010–14), 99 (2015–19), **208 (2020–26)** — the field is accelerating, and the
2025–2026 readouts materially change the landscape relative to any review written before 2024.

**Traditional and historical medicine.** A Chinese-language evidence-mapping study identified
**323 clinical studies of TCM in IPF, including 295 RCTs and 28 meta-analyses**, and characterised
the RCT base as generally low quality: small samples, short treatment courses, little attention to
acute exacerbation or complications, few studies of TCM alone, non-standardised syndrome
definitions, and outcome sets that mostly failed to distinguish primary from secondary endpoints
(PMID 39805768). This is a large body of evidence that PubMed alone (103 MeSH-tagged records)
substantially under-samples — a retrieval asymmetry, not an absence.

**Verdict on richness.** Sufficient for a complete evidence record, an order of magnitude smaller
than RA, and with a well-defined primary endpoint that makes cross-trial synthesis unusually
tractable.

---

## 4. Failed, abandoned and halted treatments

**65 interventional trials** are registered as terminated (52), withdrawn (12) or suspended (1).
Stated reasons, classified from the registry `whyStopped` field (full register:
`ipf_phase0_stopped_trials.csv`):

| Stated reason class | n | of which phase 2 or 3 |
|---|---|---|
| Efficacy / futility | 13 | 13 |
| Recruitment | 12 | 5 |
| Safety / benefit-risk | 10 | 9 |
| Business / sponsor / funding | 10 | 9 |
| Other | 10 | 2 |
| No reason stated | 5 | 4 |
| COVID-19 disruption | 3 | 2 |
| External result / standard-of-care change | 2 | 2 |

**Only 20% of halted IPF trials stopped because the drug failed.** An almost equal number stopped
for business, funding or recruitment reasons, and five state no reason at all (fig 2). For an
evidence record this matters directly: "abandoned" and "ineffective" are different classes, and in
IPF the registry itself shows they are roughly equally common.

**Documented failures with primary sources** (see `ipf_phase0_pivotal_trials.csv`):

- *Failed on efficacy.* Pamrevlumab / anti-CTGF (ZEPHYRUS-1, diff 70 mL, 95% CI −60 to 190,
  P = 0.29, PMID 38762797); ziritaxestat / autotaxin inhibitor (ISABELA, diff 22.7 mL,
  PMID 37159034); interferon gamma-1b (INSPIRE, mortality HR 1.15, 0.77–1.71, PMID 19570573);
  co-trimoxazole (EME-TIPAC, HR 1.2, 0.9–1.6, PMID 33289822); N-acetylcysteine monotherapy
  (PANTHER, −0.18 vs −0.19 L, P = 0.77, PMID 24836309); sildenafil (STEP-IPF, PMID 20484178);
  nintedanib + sildenafil (INSTAGE, SGRQ P = 0.72, PMID 30220235); recombinant pentraxin-2
  (phase 3 STARSCAPE NCT04552899 terminated at futility analysis after a positive phase 2,
  PMID 29800034).
- *Stopped for harm.* Prednisone + azathioprine + NAC (PANTHER: 8 vs 1 deaths, P = 0.01;
  23 vs 7 hospitalisations, PMID 22607134); warfarin (ACE-IPF: 14 vs 3 deaths, P = 0.005,
  PMID 22561965). Cyclophosphamide for acute exacerbation showed a non-significant excess of
  3-month mortality (45% vs 31%, difference 14.5%, 95% CI −3.1 to 31.6, PMID 34506761).
- *Positive but abandoned.* NAC on a prednisone + azathioprine background improved vital capacity
  by 0.18 L at 12 months (95% CI 0.03–0.32, IFIGENIA, PMID 16306520) — a result made unusable when
  the background regimen itself was shown to cause harm.
- *Mechanism classes exhausted.* Anticoagulation, immunosuppression, endothelin antagonism,
  IL-13 blockade, LOXL2 inhibition, CTGF blockade, autotaxin inhibition, αvβ6 integrin blockade,
  JNK inhibition, interferon and antimicrobial strategies have all been taken into phase 2 or 3
  and abandoned.

**A retrievability problem, distinct from an efficacy problem.** Of 239 completed interventional
trials, only 90 have results posted; **129 trials completed since 2010 have no posted results**.

![Anatomy of halted IPF trials]({{artifact:art_f7c08648-82fc-42a1-ab4c-30af9abfbf77}})

---

## 5. Contradictions and unresolved conflicts

These are recorded as conflicts, not resolved:

1. **A completed pharmacogenomic trial with no retrievable result.** A retrospective interaction
   between *TOLLIP* rs3750920 genotype and NAC response (PMID 26331942) motivated PRECISIONS
   (NCT04300920, n = 202), a prospective genotype-selected trial. The registry lists it as
   **completed with no results posted**, and no primary publication is indexed in PubMed as of
   2026-09-02 — only the design paper (PMID 36514019). The field's clearest test of biomarker-
   guided therapy is currently unreadable.
2. **Mortality benefit: pooled versus individual trials.** No individual antifibrotic RCT was
   powered for mortality and ASCEND's mortality endpoint was not significant (P = 0.10), yet
   meta-analysis reports RR 0.55 (0.45–0.66) (PMID 34217681). Both statements are defensible; they
   are not the same claim.
3. **Identical trials, opposite secondary results.** Acute-exacerbation hazard ratios of 1.15 and
   0.38 in INPULSIS-1 and INPULSIS-2 (PMID 24836310).
4. **Placebo-arm decline is not stable.** Across the trials in fig 1b, placebo-arm FVC loss ranges
   from −112.5 mL (26 wk, ELEVATE) to −330 mL (48 wk, ZEPHYRUS-1) — roughly 3-fold. This alone can
   manufacture or erase an apparent treatment effect between trials.
5. **Phase 2 success does not predict phase 3.** Pentraxin-2 met its phase 2 FVC endpoint and
   improved 6-minute walk distance by 31.3 m (90% CI 17.4–45.1, P < 0.001, PMID 29800034), then
   failed phase 3 at futility. Pamrevlumab followed the same trajectory.
6. **Immunosuppression: universal harm or subgroup harm?** Triple therapy caused excess death
   overall (PMID 22607134), while observational work reports interaction with telomere length
   (PMID 30566847, abstract not indexed). No prospective stratified test exists.
7. **Corticosteroids in acute exacerbation.** Standard practice rests on observational data with
   inconsistent direction, including a reported increased mortality signal in IPF patients
   (OR 1.075, 1.044–1.107) alongside associations favouring particular dosing strategies
   (PMID 39721758).
8. **Anti-acid therapy.** An omeprazole pilot reported cough frequency 39.1% lower but with a CI
   crossing the null (66.0% lower to 9.3% higher, PMID 30610155), against guideline positions
   informed by observational data pointing both ways.
9. **TCM: volume without resolvable signal.** 295 RCTs, none of which the mapping study judged
   methodologically adequate (PMID 39805768). Whether any contains a testable signal is unknown
   and, importantly, *answerable by screening rather than by new trials*.

---

## 6. Major unanswered therapeutic questions

Ten questions with their current evidence status and the smallest useful next step are in
`ipf_phase0_open_questions.csv`. In brief: Q1 is any part of established fibrosis reversible in
humans; Q2 does antifibrotic therapy prolong survival and by how much; Q3 does *TOLLIP* genotype
identify NAC responders (PRECISIONS unretrievable); Q4 is immunosuppression harmful universally or
only in a telomere-defined subgroup; Q5 do the approved antifibrotics plus a new-mechanism agent
add up (add-on versus switch has never been randomised); Q6 why do positive phase 2 signals fail in
phase 3 so consistently; Q7 is there any evidence-based treatment for acute exacerbation; Q8 can
cough and dyspnoea be treated without accelerating harm; Q9 does the 295-RCT TCM base contain any
testable signal; Q10 is 52-week FVC change an adequate basis for the whole field.

Note that **Q1, Q2, Q3, Q5, Q6, Q7 and Q10 are answerable, in whole or part, from data that
already exist** — no new clinical trial is required to make progress on them.

---

## 7. Research Lead potential — assessed, not asserted

No Research Leads are proposed in Phase 0. What is assessed here is whether the evidence structure
*could* support leads meeting the project's bar (a signal real in a primary record, not resolved by
newer evidence, not a retrieval artefact, and yielding a specific answerable question).

Structural features that would plausibly generate candidates:

- **Missing results at scale.** 129 completed-since-2010 trials with no posted results, including
  one prospective biomarker-stratified trial. Retrieval tasks, not experiments.
- **A stratification track that was started and dropped.** *MUC5B*, *TOLLIP* and telomere biology
  give IPF genuine subgroup hypotheses; only one has ever been tested prospectively, and its result
  is unretrievable.
- **An untested combination question.** Nerandomilast was tested *on top of* background
  antifibrotics (77.7% of participants) but add-on versus switch versus maximal monotherapy has
  never been randomised.
- **A methodological signal with direct consequences.** 3-fold placebo-arm drift and four different
  FVC metrics in use across pivotal trials.
- **A large unscreened traditional-medicine corpus** with pre-specifiable inclusion criteria.

Features that would *limit* lead generation: the mechanism space has been unusually thoroughly
worked through by industry; there is little "positive but abandoned" material of the kind that
dominated the RA record (the one clear case, IFIGENIA, is confounded by a harmful background
regimen); and the endpoint is a surrogate, so almost any signal is a signal about FVC rather than
about survival or symptoms.

**Assessment: leads are plausible but will be of a different type than in RA** — dominated by
retrieval, re-analysis and methodology rather than by neglected candidate therapies.

---

## 8. Feasibility within the Open Therapeutics workflow

**Favourable.** Literature volume ~10× smaller than RA. Registry data are machine-readable and were
pulled completely in one pass. A single current guideline anchors the standard of care
(PMID 35486072). One primary endpoint (FVC) dominates, so a quantitative treatment map is possible
in a way it was not for RA's composite disease-activity scores. The disease boundary is
diagnostically defined (UIP pattern).

**Unfavourable / risk.**

1. **Boundary creep.** The regulatory and scientific centre of gravity is moving from IPF to
   *progressive pulmonary fibrosis* (PPF) and ILD generally; nerandomilast's label covers PPF. Much
   2024–2026 evidence is mixed-population and must be labelled indirect.
2. **A very large preclinical literature.** Most of the 18,308 records are mechanistic. Without an
   explicit exclusion rule the record would drown in animal and in-vitro work — exactly the
   "biological plausibility as efficacy" failure the project prohibits.
3. **Language asymmetry.** The bulk of TCM evidence sits in CNKI/VIP/Wanfang/SinoMed, which the RA
   project explicitly recorded as a coverage gap. For IPF that gap is larger in relative terms
   (295 RCTs).
4. **A moving target.** Three phase 3 readouts and one approval landed in 2025–2026. Any statement
   must be dated.
5. **Surrogate-endpoint dependence.** Grading "works" is genuinely ambiguous when the only
   consistent evidence is millilitre-scale FVC differences.

---

## 9. Comparison with the completed RA record

| Dimension | RA (completed) | IPF (prospective) |
|---|---|---|
| Evidence volume | 186,017 papers; 4,806 RCTs | 18,308 papers; 305 RCTs |
| Interventions mapped | 67 across 12 domains | ~488 distinct intervention strings in the registry; expect a comparable curated set |
| Best achievable outcome | Remission (operationally defined) in a substantial minority | Slowed decline only; no remission construct exists |
| Dominant verdict class | Uncertain (21/67), then Works (14) | Expect Failed / Harm to dominate — a testable prediction for Phase 2 |
| "Works — abandoned anyway" | 8 interventions | Few candidates identified; the one clear case is confounded |
| Core unmet need | Refractory / non-inflammatory disease and response prediction (UN4 had zero candidate interventions) | The disease itself: progression, reversal, survival |
| Endpoint structure | Composite disease-activity indices, patient-clinician discordance | One surrogate continuous endpoint, measured four different ways |
| Negative-evidence richness | 17-entry negative register, 9 preserved conflicts | 65 halted trials, 13 futility, 10 safety, 2 harm-stopped, 129 unreported |
| Traditional-medicine base | TwHF best-evidenced; CNKI/Wanfang not searched (declared gap) | 295 TCM RCTs, uniformly low quality (mapped, PMID 39805768) |
| Register the disease needs that RA did not | — | **A retrievability register**: completed trials whose results cannot be read |

**The two diseases pose different research problems.** RA's map was about *heterogeneity* — many
effective options, unclear which patient gets which, plus a residual-symptom population with no
mechanism. IPF's map would be about *a ceiling* — one mechanism class that works marginally,
everything else failed, and outcomes that cannot be distinguished from surrogate movement. That
makes IPF a genuinely different test of the method, not a repetition.

---

## 10. Scoring

Per-dimension rationale in `ipf_phase0_scoring.csv`.

| Dimension | Score (1–5) |
|---|---|
| Unmet therapeutic need | **5** |
| Evidence base richness | **4** |
| Failed / contradictory evidence richness | **5** |
| Research Lead potential | **4** |
| Feasibility within scope | **4** |
| **Total** | **22 / 25** |

---

## Final verdict

# GO WITH SCOPE LIMITS

IPF is worth a full Open Evidence Record, but four scope decisions must be fixed before Phase 1
begins, because each of them changes what the record would contain.

### 1. Verdict
**GO WITH SCOPE LIMITS.**

Required limits:

- **L1 — Disease boundary.** IPF only, as defined by the 2022 ATS/ERS/JRS/ALAT criteria. Evidence
  from PPF, non-IPF ILD or other fibrotic diseases enters only as explicitly labelled *indirect
  evidence*, with the population stated in the row itself. This is not optional: the 2025 approval
  and much recent evidence are PPF-wide.
- **L2 — Evidence-type gate.** Human clinical evidence is the spine of the record. Preclinical work
  is admitted only where it is cited to explain a specific human observation, and never as support
  for an efficacy statement. Without this rule the 18,308-record literature is unmanageable.
- **L3 — Outcome-dimension separation enforced in the schema.** Separate fields for FVC slope,
  acute exacerbation, mortality, symptoms/quality of life, functional capacity and any claim of
  reversal. No row may make a single undifferentiated "works" statement. The FVC metric
  (annual rate / absolute change / median change / categorical) must be recorded per row, because
  the pivotal trials use all four.
- **L4 — Traditional-medicine handling declared in advance.** Include TCM as a domain, but treat
  the 295-RCT base as a *screening* task with inclusion criteria fixed before results are read
  (objective FVC or DLCO endpoint, minimum duration, minimum sample size, risk-of-bias
  assessment). Declare the Chinese-language database coverage actually achieved, as the RA record
  did for its gap.

### 2. The three most important reasons
1. **The ceiling is real, quantified and low.** Three approvals and twelve years apart, every
   effective drug produces a 45–130 mL FVC difference; no trial has stopped decline, restored
   function or shown reversal, and survival evidence remains pooled rather than trial-level. This
   is precisely the kind of gap the project exists to map, and it can be stated in numbers rather
   than impressions.
2. **The negative-evidence landscape is exceptionally rich and largely undigested.** 65 halted
   trials in which futility (13) and non-scientific reasons (business/funding 10, recruitment 12,
   none stated 5) are comparably common; two interventions stopped for excess death; a documented
   phase-2-to-phase-3 collapse pattern; and **129 completed trials since 2010 with no posted
   results**, including one prospective biomarker-stratified trial. A record that preserves this is
   valuable independently of whether any lead survives.
3. **The open questions are answerable from existing data.** Seven of ten questions in
   `ipf_phase0_open_questions.csv` can be advanced by retrieval, re-analysis or registry emulation
   rather than new trials — which is exactly the project's stated preference for the smallest
   useful next experiment.

### 3. The biggest risk
**That the record becomes a record of a surrogate endpoint rather than of a disease.** Every
positive result in IPF is a millilitre-scale FVC difference; secondary endpoints (exacerbation,
mortality, symptoms) were non-significant or hierarchy-stopped even in the successful 2025–2026
trials, and placebo-arm decline varies ~3-fold between trials. If the map grades interventions on
FVC alone, it will silently equate "slows a surrogate" with "helps patients" — the exact
conflation the project's principles forbid — and its verdict classes will inherit the field's own
unresolved methodology. L3 above is the mitigation; a secondary risk is boundary creep into PPF
(L1), which would quietly convert an IPF record into a general fibrosis record.

### 4. If GO — the core question Phase 1 should start from
> **What, precisely, is the best documented outcome any IPF patient has achieved with any
> treatment — separately for symptoms, rate of decline, prevention of progression, recovery of
> lost function, acute exacerbation, and survival — and what is the primary evidence for each?**

Starting here forces the endpoint taxonomy to be built before any intervention is graded, which is
the one methodological decision that determines whether the rest of the record is trustworthy. Its
first two deliverables should be an endpoint-and-metric taxonomy (including the four FVC metrics
and the mortality-power arithmetic from PMID 24476390) and a **retrievability register** of
completed-but-unreported trials — a register the RA record did not need and this one does.

### 5. If HOLD / NO-GO
Not applicable. For completeness: were IPF rejected, the better next-disease profile would be a
condition with a *treated but unsatisfied* population rather than a ceiling — a substantial group
of patients receiving effective standard therapy who remain unwell (as RA's non-inflammatory
refractory population was), plus an outcome measure that is clinical rather than surrogate. IPF is
the opposite profile, which is a reason to do it rather than to defer it.

---

### Limitations of this Phase 0 assessment

Abstract-level extraction only; no full texts were read and no effect estimates were verified
against publications. ClinicalTrials.gov only — EU CTR, jRCT, ISRCTN and Chinese registries were
not searched, so trial counts are a lower bound. PubMed only for literature; Chinese-language
databases were not searched, so the TCM figures come from one mapping study rather than from
primary retrieval. Stop-reason classification is keyword-based on registry free text and was not
manually adjudicated per trial. Several relevant records had no abstract indexed (PMID 35486072,
39393084, 31917621, 30566847, 36386223) and their contents were not inferred. Scores are analyst
judgements, not computed quantities.
