> **Archived phase report — a dated record of what was believed at the time, not the current state of the project.**
> Statements superseded by later verification are listed in `data/corrections_log.csv`. Check that log before citing anything in this file.
> Current lead status is in `data/research_leads_status.csv`.

# Open Therapeutics #001 — Rheumatoid Arthritis
## Phase 1: Evidence-Based Baseline of the Current State of Knowledge

**Date:** 2026-08-31
**Scope:** Conventional biomedical evidence only. Traditional Chinese Medicine, alternative
medicine, natural products and candidate "overlooked" treatments are **deliberately excluded**
from this document and are reserved for later phases. Two exceptions appear below only because
they are already inside the conventional evidence stream and cannot honestly be omitted from a
description of the current landscape: implanted vagus nerve stimulation (a device with a
published sham-controlled RCT) and CAR T-cell therapy (an emerging cell therapy).

**Companion files**
- `ra_phase1_references.csv` — 77 curated primary sources with PMID, DOI, evidence level, and the
  specific finding each is cited for.
- `ra_phase1_open_questions.csv` — the ranked unanswered-question register from §13.

!Quantitative summary of the current therapeutic ceiling in RA. (a) NORD-STAR CDAI remission at 48 weeks in treatment-naive early RA (n=812 randomised). (b) Sustained DMARD-free remission in tREACH by autoantibody status. (c) ARCTIC REWIND: flare within 12 months after tapering TNF inhibitors to withdrawal versus stable therapy in patients in sustained remission. (d) Randomised prevention trials in seropositive at-risk individuals; TREAT EARLIER 5-year subgroups are post-hoc with 66 participants total. (e) Pooled prevalence of difficult-to-treat and multi-failure RA from a 23-study meta-analysis (27,987 patients); bar shows 95% CI for the difficult-to-treat estimate. Denominator in (e) is all RA patients.

---

## 0. Method and how to read this document

**Retrieval.** PubMed was searched programmatically across ~70 tagged concept queries covering
each of the nine questions posed, followed by named-target lookups for specific guidelines,
classification criteria, landmark trials and cohorts. 884 records were retrieved; 77 were
curated into the reference table after prioritising clinical practice guidelines, consensus
definitions, systematic reviews and meta-analyses, randomised trials, and high-impact primary
mechanistic work. Every numeric claim in this document was read from the source abstract, not
recalled.

**Known limitations of this retrieval.** (a) Screening was done on titles and abstracts, not full
texts — a small number of effect estimates may be contextualised differently in the full papers.
(b) PubMed's Boolean behaviour means several long concept queries returned nothing and had to be
re-issued in shorter form; concepts that never surfaced a good source are marked *not retrieved*
rather than *absent*. (c) A structured search for **patient-generated** research priorities
returned nothing usable, so §12 draws patient-relevant unmet needs from clinician-authored
reviews and cohort data. This is a real gap and should be closed in a later phase with a
targeted search of patient-partnership literature. (d) No formal risk-of-bias appraisal was
performed on individual studies. (e) No grey literature, regulatory documents, or trial
registries were searched.

**Evidence tiers used throughout.** Every substantive statement is tagged:

| Tag | Meaning |
|---|---|
| **[E]** Established | Consistent evidence from guidelines, multiple RCTs, or large well-replicated studies. Unlikely to reverse. |
| **[P]** Probable | Supported but with meaningful residual uncertainty — single trial, observational only, or contested effect size. |
| **[U]** Uncertain / contested | Studies disagree, or the evidence base is too thin to decide. |
| **[H]** Hypothesis | A mechanistic or causal proposal with supporting associative or preclinical data but no confirmatory human evidence. |
| **[N]** Negative / null | An intervention or hypothesis tested and *not* supported. Recorded deliberately (Principle 3). |

---

## 1. What rheumatoid arthritis is

**[E]** RA is a chronic immune-mediated inflammatory disease whose defining lesion is
inflammation of the synovial membrane of joints, producing a characteristic symmetric
polyarthritis of small joints with a tendency to progressive erosion of cartilage and bone. It is
systemic, not joint-limited: extra-articular manifestations include interstitial lung disease,
accelerated atherosclerosis, and a broad comorbidity burden.

**[E]** RA is not one disease. It divides at minimum into an **autoantibody-positive** form
(anti-citrullinated protein antibodies, ACPA, and/or rheumatoid factor, RF) and an
**autoantibody-negative** form. These differ in genetic association, environmental risk,
treatment response and long-term outcome — differences large enough that treating them as a
single entity in trial design is now questionable (see §9.3, §11.3).

**[E]** Classification for research uses the **2010 ACR/EULAR criteria** (score ≥6/10 across joint
involvement, serology, acute-phase reactants and symptom duration), which deliberately moved
classification earlier in the disease course than the 1987 criteria. These are *classification*
criteria for cohort comparability, not diagnostic criteria for individual patients — a distinction
frequently blurred in the literature.

---

## 2. Burden

**[E]** Global Burden of Disease 2021 estimates for the year 2020: **17.6 million people**
(95% UI 15.8–20.3) living with RA worldwide; age-standardised prevalence **208.8 per 100,000**
(186.8–241.1), a **14.1% increase since 1990**; female-to-male age-standardised prevalence ratio
**2.45**. Age-standardised death rate 0.47 per 100,000 (**38,300 deaths**), a **23.8% decrease**
since 1990. DALYs 3.06 million, of which **76.4% were years lived with disability** rather than
years of life lost. Smoking was attributed 7.1% of RA DALYs. **Projected 31.7 million cases
(25.8–39.0) by 2050.**

**[U]** GBD's own estimates are not stable across cycles. GBD 2017 reported age-standardised
prevalence of **246.6 per 100,000** and incidence of 14.9 per 100,000, versus 208.8 in GBD 2021 —
a ~15% difference in a headline figure arising from modelling revision, not from a change in the
disease. Any single GBD number should be quoted with its cycle.

**[E]** The disability-dominant DALY profile plus falling mortality means the modern burden of RA
is primarily **lifelong morbidity**, and the case count is rising even as death rates fall.

**[E]** Access to modern therapy is profoundly unequal. In the COVAD-2 international survey of
1,997 RA patients, advanced therapy (b/tsDMARD) use was **29.6% overall** but **44.0% in Europe,
11.7% in Asia and 5.3% in Africa**, and **2.7% in low-HDI versus 38.8% in very-high-HDI
countries**. For a large share of the world's RA population, the relevant unmet need is access to
existing drugs, not the invention of new ones.

---

## 3. What causes RA — and what remains unknown

### 3.1 Genetics

**[E]** RA is polygenic with a dominant HLA contribution. The largest trans-ancestry GWAS
meta-analysis (29,880 cases, 73,758 controls) identified 42 novel loci for a total of **101 RA
risk loci** implicating 98 candidate genes; RA risk loci were enriched for the targets of approved
RA drugs, which is the strongest existing argument that RA genetics is drug-target-relevant.

**[E]** The **HLA-DRB1 "shared epitope"** alleles are the strongest single genetic risk factor,
and specifically for ACPA-positive disease.

**[U]** RA heritability is widely quoted as ~60%, but this figure comes from older twin series. A
population-based Danish twin study found monozygotic concordance of only **9.1% (1.9–24.3)** versus
dizygotic 6.4%, and partitioned variance into additive genetic **12% (0–76%)**, shared environment
**50% (0–72%)** and non-shared environment **38% (17–61%)**. The confidence intervals are so wide
that this study neither refutes nor confirms the classical estimate — the honest statement is that
**we do not know RA heritability with useful precision**, and the commonly cited 60% is less secure
than its ubiquity suggests.

### 3.2 Environment and gene–environment interaction

**[E]** Smoking is the best-established environmental risk factor, and interacts strongly with
HLA. In a case-control analysis, the relative risk for ACPA-positive RA in carriers of DRB1*04
shared-epitope alleles who smoked was **8.7 (5.7–13.1)**, with an attributable proportion due to
interaction of 0.4–0.6 — i.e. roughly half the risk in exposed carriers is attributable to the
interaction itself, not to either factor alone.

**[E]** Occupational inhalant exposures are consistently associated with RA. A meta-analysis of
crystalline silica found **OR 1.94 (1.46–2.58)**. A broader 2026 meta-analysis of occupational
inhalants (31 studies) found elevated risk across **silica, asbestos, solvents, pesticides,
fertilizers, animal dust and engine exhaust**, with relative risks in the **1.25–1.49** range.

**[H]** The convergence of smoking and inhalant exposures on the lung, plus the periodontal and
gut findings below, supports a **mucosal origins hypothesis**: that RA-initiating autoimmunity
begins at a mucosal surface years before joint disease, and that several distinct mucosal
"endotypes" (lung, oral, gut) may independently initiate the same eventual syndrome. This is a
hypothesis with substantial associative support and no confirmatory human causal evidence.

### 3.3 Microbiome

**[U]** Oral and gut dysbiosis is reproducibly *associated* with RA — a metagenomic case-control
study found altered oral and gut communities in RA that partially normalised after treatment,
with *Haemophilus* depleted and *Lactobacillus salivarius* enriched. **[U]** The direction of
causation is unresolved: treatment-responsive normalisation is equally consistent with dysbiosis
being a consequence of inflammation or of drug exposure. **[H]** The gut–joint axis as a causal
pathway remains a hypothesis.

**[H]** *Porphyromonas gingivalis* and periodontal citrullination as a specific initiating
mechanism remains a hypothesis; the retrieval for this document did not surface a human
intervention trial resolving it.

### 3.4 What is genuinely unknown about causation

1. **[U]** Why the same risk-factor profile produces disease in only a small minority of exposed
   people. No combination of known genetic and environmental factors predicts onset with clinically
   useful accuracy at the population level.
2. **[U]** Why the joint. Nothing in the mucosal or genetic models explains the anatomical
   specificity — why systemic autoimmunity localises to synovium, symmetrically, and in a
   characteristic joint distribution.
3. **[U]** What triggers the transition from asymptomatic autoimmunity to clinical arthritis. This
   is the single most consequential gap, because it is the step a preventive intervention must
   block (§9.4).
4. **[U]** The cause of autoantibody-negative RA. It has weaker HLA association and a different
   outcome trajectory; whether it is one disease, several, or partly misclassification of other
   conditions is unresolved (§9.3).
5. **[U]** The 2.45:1 female excess is unexplained beyond association.

---

## 4. Natural history: RA begins before it is diagnosable

**[E]** Autoantibodies precede clinical disease by years. In a nested case-control study within
Swedish population cohorts, anti-CCP was detectable in stored blood from **33.7%** of people who
later developed RA, at a median of **2.5 years** before symptom onset; anti-CCP sensitivity was
**25%** more than 1.5 years before symptoms and **52%** within 1.5 years. Review-level synthesis
places the average ACPA lead time at **3–5 years**.

**[E]** This establishes a defined **at-risk phase** — seropositive arthralgia without clinical
arthritis — which is now a formal trial population.

**[E]** Risk within that phase can be stratified. EULAR/ACR risk stratification criteria developed
in 2,293 arthralgia patients achieved **AUC 0.80 (0.77–0.83)** using six clinical and serological
variables; adding MRI raised this to **0.87** for inflammatory arthritis and **0.93** for RA
specifically. **[U]** Whether this level of discrimination is sufficient to justify treating
asymptomatic people is a separate question, unresolved (§9.4).

**[H]** The dominant conceptual model is therefore a **continuum**: genetic susceptibility →
mucosal/environmental initiation → systemic autoimmunity → subclinical synovitis → clinical
arthritis → established, self-sustaining disease. The model is well supported descriptively; the
claim that the transitions are *causally sequential and interruptible* is a hypothesis, and the
prevention trials in §9.4 are its most direct tests.

---

## 5. Pathogenesis and disease heterogeneity

**[E]** Established synovitis involves infiltrating T and B lymphocytes, plasma cells, activated
macrophages, and a pathologically expanded and activated synovial fibroblast population, driving
TNF, IL-6 and GM-CSF-dependent inflammation and RANKL-mediated bone erosion. The clinical
efficacy of agents targeting TNF, IL-6, T-cell co-stimulation, CD20 B cells and JAK signalling is
itself the strongest evidence that each of these arms is causally involved in established disease.

**[E]** The synovium is heterogeneous between patients. A single-cell atlas of 79 donors and over
314,000 cells defined **six cell-type abundance phenotypes (CTAPs)** spanning lymphocyte-rich to
lymphocyte-poor/fibroblast-dominant synovium; these phenotypes are dynamic and associate with
treatment response. **[P]** This is the most credible current biological basis for the clinical
observation that patients respond differently to mechanistically different drugs.

**[H]** Fibroblast-driven, immune-independent disease persistence. Spatial transcriptomics of
non-remitting patients described **fibrogenic vascular niches** with high fibroblast COMP and
endothelial Notch-driven TGF-β signalling, and post-treatment immune depletion accompanied by
*expansion* of these niches. If correct, this would mean some patients' persistent disease is
maintained by stromal programmes that current immune-targeted drugs do not address — an important
and testable hypothesis, currently supported by descriptive human tissue data only.

**[H]** A mechanistic correlate of remission stability: MerTK⁺TREM2⁺ and MerTK⁺LYVE1⁺ synovial
macrophage subsets carry remission-associated signatures, and a low MerTK⁺ proportion in patients
in remission was associated with increased flare risk after treatment cessation. Small,
single-cohort, not yet a validated clinical test.

---

## 6. Diagnosis and the "window of opportunity"

**[P]** Earlier DMARD initiation gives better outcomes. In a matched case-control cohort, patients
starting DMARDs at a median 3 months of symptoms achieved DAS28 improvement of **2.8** at 36
months versus **1.7** in those starting at 12 months, with less radiographic progression. In the
BARFOT early-RA cohort (n=1,587) shorter symptom duration predicted better EULAR response.

**[U]** Whether the "window" is a true biological window (a time-limited period of reversibility)
or simply reflects less accumulated damage plus confounding by disease severity and referral
patterns is **not settled**. Two observations complicate the biological interpretation: the
BARFOT analysis found the duration–response gradient was **absent in smokers**, and the strongest
supporting study is a 20-patient-per-arm case-control design, not an RCT. No RCT has randomised
time-to-treatment.

**[E]** Diagnostic delay is nonetheless a real, measurable problem, and is one of the mechanisms
by which the treat-to-target strategy fails in practice.

---

## 7. How RA is currently treated

### 7.1 Strategy: treat-to-target

**[E]** The organising principle is **treat-to-target (T2T)**: define remission (or low disease
activity as an alternative in long-standing disease) as an explicit target, measure a composite
disease activity index at regular intervals (every 1–3 months while active), and escalate therapy
until the target is met. The T2T recommendations comprise 4 overarching principles and 10
recommendations in their 2014 update.

**[E]** T2T is supported by randomised evidence. **TICORA** randomised 111 patients to intensive
tight control versus routine care: good response in **82% versus 44%**, DAS28 remission in **65%
versus 16%**, at no additional cost. **BeSt** showed that four different strategies converged by
2 years (42% in remission overall) but that initial combination therapy better suppressed joint
damage — i.e. **the strategy of tight control mattered more than the specific initial drug
choice**.

### 7.2 Pharmacological sequence

**[E]** Current EULAR recommendations (2025 update: 5 overarching principles, 9 recommendations,
reduced from 11 in 2022) place **methotrexate plus short-term glucocorticoids** as initial
therapy; if the target is not reached in 3–6 months, add a bDMARD (TNF, IL-6R, CD20 or T-cell
co-stimulation targeting) or a JAK inhibitor, the latter after explicit consideration of
cardiovascular and malignancy risk factors. The 2021 ACR guideline covers the same territory with
**44 recommendations, of which only 7 are strong and 37 conditional** — a direct, official
statement that most of the RA treatment algorithm rests on low-certainty evidence.

**[E]** Methotrexate remains the anchor drug, but yields remission in **at most about half** of
patients as monotherapy across RCTs.

**[E]** In treatment-naive early RA, NORD-STAR compared active conventional therapy against three
biologics; CDAI remission at 48 weeks was **abatacept 59.3%, certolizumab 52.3%, tocilizumab
51.9%, active conventional therapy 39.2%**. Even the best arm left **~41% of patients not in
remission** (figure, panel a).

**[E]** After b/tsDMARD failure, a Cochrane network meta-analysis (19 RCTs, 4,779 participants)
found that switching to a **not-previously-tried TNF inhibitor** produced ACR50 with **OR 6.04
(2.49–16.3), high certainty**, with IL-6 inhibitors, abatacept, rituximab and JAK inhibitors also
effective. Sequential switching works — but empirically, not by prediction (§10).

### 7.3 Safety, which constrains the strategy

**[E]** Biologics carry increased serious infection risk relative to conventional DMARDs:
standard-dose **OR 1.31 (1.09–1.58)**, high-dose **1.90 (1.50–2.39)**, low-dose not significantly
elevated (0.93, 0.65–1.33) in a 106-trial network meta-analysis.

**[E]** **ORAL Surveillance**, a post-authorisation safety trial in cardiovascular-risk-enriched
RA, compared tofacitinib with TNF inhibitors: MACE **HR 1.33 (0.91–1.94)** and cancer **HR 1.48
(1.04–2.09)**; non-inferiority was **not** demonstrated. This single trial reshaped JAK inhibitor
labelling and positioning worldwide.

**[E]** Long-term low-dose glucocorticoids have a genuinely mixed benefit–harm profile. **GLORIA**
randomised patients aged ≥65 to prednisolone 5 mg/day for 2 years: DAS28 lower by **0.37** and
damage progression lower by **1.7 points**, but adverse events of interest in **60% versus 49%**
(RR 1.24), mostly non-severe infections. This is a real trade-off, not a settled question.

**[E]** RA-ILD treatment evidence is largely observational. A systematic review of 69 studies and
7,879 RA-ILD patients found methotrexate associated with **reduced** ILD progression and mortality
(contradicting a common clinical assumption that methotrexate should be avoided in RA-ILD), and
identified abatacept, rituximab and nintedanib as promising. **[U]** Confounding by indication
cannot be excluded from observational data of this kind.

---

## 8. What "remission" means in RA

**[E]** Remission in RA is an **operational definition, not a biological state**. The 2011
ACR/EULAR provisional definition offered a Boolean form (tender joint count, swollen joint count,
CRP and patient global assessment each ≤1) and an index-based form (SDAI ≤3.3).

**[E]** These definitions were revised in 2022 because the patient global assessment component was
excluding patients whose inflammation was fully controlled. **Boolean2.0**, which relaxes patient
global to ≤2 cm, raised 6-month remission rates from **14.8% to 20.6%** in early RA and from
**4.2% to 6.0%** in established RA without loss of predictive validity for radiographic and
functional outcomes. Two consequences follow, and both matter for this project:

1. **[E]** Reported "remission rates" are not comparable across studies using different
   definitions. A 5-percentage-point swing in remission rate can be produced by a definitional
   change alone.
2. **[E]** Remission by these criteria is a **low bar relative to health**: only 6% of established
   RA patients met it at 6 months even under the relaxed definition.

**Remission explicitly does not mean:**

- **[E]** *Absence of inflammation.* Power Doppler ultrasound synovitis is detectable in patients
  meeting clinical remission criteria and predicts outcome: flare **OR 4.52 (2.61–7.84)** and
  progressive erosion **OR 12.80** at patient level.
- **[E]** *Absence of symptoms.* A systematic review of 55 records documented residual functional
  disability, tender and swollen joints, pain, fatigue and impaired patient global in a substantial
  fraction of patients meeting remission or low-disease-activity targets. Residual pain, with
  central sensitisation and comorbid fibromyalgia as contributors, persists after inflammation is
  controlled.
- **[E]** *Absence of autoimmunity.* ACPA-expressing switched-memory B cells persist in patients in
  clinical remission, and retain a highly activated phenotype despite effective disease control
  including under JAK inhibition.
- **[E]** *Drug independence.* Remission in current practice is nearly always drug-maintained (§9).

---

## 9. Is true cure currently possible?

**Short answer: [E] no, not as a reliable, achievable goal — with one qualified and important
exception in a specific subgroup.**

### 9.1 Cure requires drug-free remission, and withdrawal usually fails

**[E]** **ARCTIC REWIND** randomised patients in remission on TNF inhibitors to stable therapy or
tapering to withdrawal. Flare within 12 months: **27/43 (63%) versus 2/41 (5%)**, risk difference
**58% (42–74)**. Tapering was **not** non-inferior (figure, panel c).

**[E]** This is why guidelines are cautious. The 2022 EULAR update stated that DMARDs "may be
tapered but should not be stopped"; the 2025 update retains the caution that stopping often leads
to flare.

### 9.2 But the "cannot stop" rule may be an artefact of who was studied

**[U]** A 2024 cohort analysis of the Leiden Early Arthritis Clinic and tREACH found that **no
patient who had ever required a bDMARD achieved sustained DMARD-free remission**, versus **37% at
5 years** (Leiden) and **15% at 3 years** (tREACH) among patients who never required one. The
authors argue the blanket recommendation reflects **ascertainment bias**: withdrawal trials are run
in bDMARD-treated populations, which are precisely the populations in which drug-free remission
essentially never occurs. If this is right, the achievability of drug-free remission has been
systematically underestimated in the patients where it is actually possible.

**This is one of the most important leads in Phase 1 and should be carried forward.**

### 9.3 Drug-free remission is real, and concentrated in seronegative disease

**[E]** In tREACH, DMARD-free remission at 2 and 5 years was **17.2–25.7% in autoantibody-positive
RA**, **28.4–42.1% in autoantibody-negative RA**, and **43.1–58.5% in undifferentiated arthritis**;
*sustained* drug-free remission was **7.6% / 21.4%**, **20.5% / 38.1%** and **35.4% / 55.4%**
respectively at 2 and 5 years (figure, panel b).

**[E]** In a population cohort of 176 seronegative RA patients, the 10-year cumulative incidence
of **drug-free remission was 26.6%**, of b/tsDMARD initiation 19.9%, and of **diagnosis change
12.8%** — the last figure being a caution that some apparent seronegative "cures" are
reclassifications.

**Interpretation [P]:** something close to cure occurs in a meaningful minority of
autoantibody-negative and undifferentiated disease. Whether that reflects a genuinely curable
biology, a self-limiting disease that would have remitted anyway, or diagnostic heterogeneity is
**unresolved** and is a first-order question (§13).

### 9.4 Prevention: onset can be delayed; prevention is not established

| Trial | Intervention | Result |
|---|---|---|
| **PRAIRI** | Single 1000 mg rituximab in ACPA+/RF+ individuals | Arthritis onset **delayed by 12 months**; HR 0.45 (0.154–1.322) at 12 months — **[N]** not a significant reduction in eventual onset |
| **TREAT EARLIER** (2 yr) | 1 yr methotrexate + single GC injection in clinically suspect arthralgia with subclinical MRI inflammation | **[N] Did not prevent arthritis: 19% vs 18%, HR 0.81 (0.45–1.48).** But **[E]** sustained improvement in HAQ, pain, morning stiffness, presenteeism and MRI inflammation |
| **TREAT EARLIER** (5 yr) | as above | **[P]** In **ACPA-negative** at-risk participants: RA in **3/35 (9%) vs 10/31 (32%)**, HR **0.24 (0.07–0.87)**, **NNT 4**. In ACPA-positive: **[N]** no effect (58% vs 65%, HR 0.75) |
| **APIPPRA** | 12 months abatacept in ACPA+/RF+ arthralgia | **[E]** During treatment 6% vs 29% progressed; **[N]** by 24 months 25% vs 37% — benefit **not sustained** after stopping |
| **ALTO** (APIPPRA extension, median 55 mo) | as above | **[P]** Arthritis-free survival difference persisted at 4 years (**4.9 months, 0.1–9.6**) but was diminishing |

(figure, panel d)

**[E] Synthesis.** Three randomised trials in at-risk individuals converge on the same answer:
**immunosuppression during the at-risk phase suppresses progression while it is being given, and
the effect largely dissipates when it stops.** This is delay, not prevention. The one signal that
looks different in kind is the ACPA-negative TREAT EARLIER subgroup — a post-hoc subgroup with
small numbers (66 participants total) and therefore **[P]**, not **[E]**, but with an NNT of 4 it
is a high-value lead worth independent replication.

**[U]** Even the symptom and MRI benefits in TREAT EARLIER raise an unresolved question: is
treating symptoms in people who will not develop RA an appropriate use of methotrexate?

### 9.5 Bottom line on cure

**[E]** For seropositive, established, bDMARD-requiring RA, no current strategy reliably produces
lasting drug-free disease absence. **[P]** For autoantibody-negative and undifferentiated
early disease, sustained drug-free remission occurs in 20–55% depending on definition and
follow-up, which is at least *phenotypically* indistinguishable from cure. **[U]** Whether this is
cure, natural remission, or misclassification is unknown. **[H]** Whether cure could be induced in
seropositive disease — e.g. by deep B-cell depletion, tolerance induction, or targeting the
stromal programmes in §5 — is a hypothesis with no confirmatory human evidence.

---

## 10. Why do some patients not respond?

### 10.1 The scale of the problem

**[E]** EULAR defines **difficult-to-treat (D2T) RA** by three simultaneously required criteria:
failure of ≥2 b/tsDMARDs with different mechanisms of action; active or progressive disease *or*
significant quality-of-life impact; and management perceived as problematic by rheumatologist or
patient.

**[E]** A meta-analysis of 23 studies and 27,987 patients found pooled D2T prevalence of **11.7%
(9.5–14.3)**; **≥3 b/tsDMARD failures in 4.3%** and **≥4 failures in 1.6%** (figure, panel e). In
a separate cross-sectional study of 1,469 patients, D2T was 16.8% and **poly-refractory disease —
failure of every available drug class — was 2.7%**.

**[E]** In the BSRBR-RA registry (13,502 patients), **6%** reached a third biologic class over a
median of 8 years, associated with female sex, smoking, obesity and deprivation.

### 10.2 Non-response is at least two different problems

**[E]** The most important conceptual advance here is the separation of **persistent inflammatory
refractory RA (PIRRA)** — multi-drug failure with objectively demonstrable ongoing inflammation —
from **non-inflammatory refractory RA (NIRRA)** — persistent symptoms and high disease activity
scores *without* objective inflammation.

**[E]** This distinction is empirically large. Among D2T patients with recent ultrasound, **57%
were PIRRA and 43% NIRRA**; NIRRA patients had higher BMI, **fibromyalgia in 15% versus 3%**, lower
swollen joint counts and lower CRP. The meta-analysis above put PIRRA at **~47.1% of D2T cases**.
**Roughly 40–50% of "treatment-refractory RA" is not refractory inflammation** — it is symptom
burden that immunosuppression cannot be expected to fix, and escalating immunosuppression in these
patients exposes them to risk without plausible benefit.

**[E]** Contributing factors to D2T status are substantially non-immunological. Comparing 52 D2T
patients with 100 controls: limited drug options due to adverse events **94% vs 57%**, comorbidity
**69% vs 37%**, concomitant fibromyalgia **38% vs 9%**, and **lower socioeconomic status at disease
onset OR 1.97**.

### 10.3 Biological mechanisms of true refractory inflammation

**[P]** Synovial cellular composition predicts response. **R4RA** randomised rituximab versus
tocilizumab stratified by synovial B-cell status: in *histologically* B-cell-poor synovium there
was no significant difference (CDAI50 45% vs 56%), but in *RNA-sequencing-defined* B-cell-poor
synovium tocilizumab was superior (**63% vs 36%, difference 26% [2–50]**). Molecular
stratification worked where histology did not.

**[P]** Molecular analysis of R4RA found ~**40% non-response to any individual biologic** and
**5–20% refractory to all**, with a **stromal/fibroblast signature marking multidrug resistance**;
machine-learning models achieved AUC 0.74 (rituximab), 0.68 (tocilizumab), 0.69 (multidrug
resistance). **STRAP** (n=208) reported synovial models with AUC 0.75–0.76, external validation in
R4RA AUC 0.71–0.79, and a 524-gene panel reaching AUC 0.82–0.87.

**[H]** Fibroblast/stromal autonomy as the mechanism of PIRRA (§5) — the most biologically specific
current hypothesis for why some inflammation is immune-drug-resistant.

### 10.4 What is missing

**[E]** **No biomarker is in routine clinical use for selecting an RA drug.** Despite the AUCs
above, no synovial or blood biomarker has been prospectively validated as a treatment-allocation
tool. Drug selection in 2026 is empirical sequential trial-and-error, and each failed cycle costs
3–6 months of uncontrolled inflammation. This is arguably the largest single actionable gap in RA
therapeutics.

---

## 11. Why do some patients relapse after remission?

**[E]** Drug withdrawal is the dominant proximate cause: 63% flare within 12 months of TNF
inhibitor withdrawal versus 5% on stable therapy (§9.1).

**[E]** Remission is not immunological quiescence, so there is persisting substrate for relapse:
subclinical ultrasound synovitis (flare OR 4.52), and persistent, activated ACPA⁺ memory B cells
(§8).

**[P]** Subclinical inflammation at the time of remission is a measurable predictor of flare — the
strongest currently available clinical predictor.

**[H]** Candidate immunological mechanisms of flare, each from small human studies:
- Low synovial MerTK⁺ macrophage proportion in remission associates with post-cessation flare risk.
- An experimental-medicine study using drug withdrawal to synchronise flare identified three
  circulating cell subsets that herald flare onset, rising but phenotypically dysfunctional Tregs,
  and **clonal T-cell (not B-cell) expansion** after drug cessation.

**[U]** Whether relapse after withdrawal reflects re-activation of a persistent pathogenic memory
compartment, loss of an active regulatory brake, or resumption of a stromal programme is not
established, and these are not mutually exclusive.

**[E]** Non-biological contributors are real and under-studied in this framing: lower
socioeconomic status, smoking, obesity and comorbidity all associate with worse trajectories
(§10.2).

---

## 12. Biggest unmet needs

Ordered by the size of the affected population multiplied by the severity of the gap.

1. **[E] Access to existing therapy.** 2.7% b/tsDMARD use in low-HDI versus 38.8% in
   very-high-HDI countries. Nothing else in this list affects as many people.
2. **[E] Symptom burden that persists in "remission".** Pain, fatigue and functional disability
   remain in a substantial fraction of patients meeting remission targets. Current targets measure
   inflammation; patients experience symptoms. There is no established therapeutic strategy for
   residual non-inflammatory symptoms, and 43% of "refractory" patients fall into this category.
3. **[E] Absence of drug-free remission for seropositive established RA.** Lifelong
   immunosuppression, with its infection risk (OR 1.31–1.90), is the current expected outcome.
4. **[E] No predictive biomarker for drug selection.** Sequential empirical switching wastes
   months of disease control per failed cycle.
5. **[E] Refractory disease with no remaining options.** 1.6–2.7% of patients have failed
   effectively everything available.
6. **[E] Comorbidity and premature mortality.** COMORA (3,920 patients, 17 countries): depression
   15%, asthma 6.6%, myocardial infarction or stroke 6%, solid malignancy 4.5%, COPD 3.5%.
   Cardiovascular mortality meta-SMR **1.50 (1.39–1.61)**. RA-ILD occurs in 2.2% of incident RA
   with 5-year mortality **39.0% versus 18.2%** and 10-year **60.1% versus 34.5%** compared with
   matched controls.
7. **[E] Prevention.** Delay is achievable; prevention is not established.
8. **[E] Diagnostic delay**, especially where rheumatology access is limited.

**[U] Whether the mortality gap is closing is contested.** A Rochester/Olmsted population cohort
(1955–2000) found RA mortality did not fall in parallel with the general population, widening the
gap; a British Columbia analysis comparing 1996–2000 and 2001–2006 incident cohorts reported
improved relative 5-year mortality in the later cohort. Both are population cohorts in
high-resource settings with different eras and methods. Also note that the meta-analysis of
cardiovascular mortality found **no significant excess when restricted to inception cohorts (SMR
1.19, 0.86–1.68)**, raising the possibility that part of the classical excess-mortality signal is
a prevalent-cohort artefact.

---

## 13. Most important unanswered questions

Ranked by expected value to patients if answered. Full version with "what would resolve it" in
`ra_phase1_open_questions.csv`.

1. **Which patients can safely stop treatment, and can that group be enlarged?** The Leiden
   ascertainment-bias argument (§9.2) implies current withdrawal evidence may not apply to the
   patients in whom drug-free remission is actually possible. Resolvable by a withdrawal trial
   enriched for never-bDMARD, autoantibody-negative patients with no subclinical synovitis.
2. **What is the mechanism that terminates the at-risk phase, and why is ACPA-negative at-risk
   disease apparently preventable while ACPA-positive is not?** The TREAT EARLIER 5-year subgroup
   (NNT 4) is the strongest signal in the prevention literature and is currently a single post-hoc
   subgroup of 66 people. Replication is the highest-value single experiment identified in Phase 1.
3. **Can synovial or blood molecular stratification be turned into a validated
   treatment-allocation tool?** AUCs of 0.75–0.87 exist; prospective biomarker-stratified
   randomisation does not.
4. **What maintains inflammation in PIRRA, and is it stromal?** If fibroblast/endothelial
   programmes sustain disease independently of the immune arms all current drugs target, a
   genuinely new drug class is required rather than another immune target.
5. **What should be done for NIRRA — the 43% of refractory patients without inflammation?** This
   population is currently receiving escalating immunosuppression with a poor mechanistic
   rationale. No therapeutic strategy is established. **This is the largest mechanism-free unmet
   need in RA and the most plausible entry point for non-immunosuppressive interventions.**
6. **Is autoantibody-negative RA one disease?** It has different genetics, different environmental
   associations, a 26.6% 10-year drug-free remission rate, a 12.8% diagnosis-change rate, and
   apparent responsiveness to preventive intervention. Trials that pool it with seropositive
   disease may be averaging away real effects.
7. **What is the true heritability and, more usefully, the true attributable fraction of modifiable
   exposures?** The twin data are compatible with a shared-environment contribution as large as
   50%.
8. **Is the window of opportunity biological or artefactual?** No trial has randomised
   time-to-treatment; the smoker-negative gradient in BARFOT argues against a simple biological
   window.
9. **Can immune tolerance be induced, rather than immunity suppressed?** Peresolimab (PD-1 agonism)
   is the first clinical test of deliberately *stimulating* an inhibitory checkpoint in RA; CAR
   T-cell approaches are entering autoimmunity. Both are early.
10. **Why the joint, and why symmetrically?** Unfashionable, unfunded, and the answer would
    reframe everything above.

---

## 14. Negative and null results register (Principle 3)

Preserved deliberately as useful knowledge.

| Finding | Tier | Source |
|---|---|---|
| Methotrexate + glucocorticoid for 1 year does **not** prevent arthritis in at-risk individuals overall (19% vs 18% at 2 years) | **[N]** | TREAT EARLIER |
| The same intervention shows **no** effect in ACPA-**positive** at-risk individuals at 5 years (58% vs 65%) | **[N]** | TREAT EARLIER 5-year |
| Abatacept's preventive benefit is **not sustained** after treatment stops (25% vs 37% at 24 months) | **[N]** | APIPPRA |
| Single-dose rituximab **delays** but does not significantly reduce eventual arthritis onset (HR 0.45, CI crosses 1) | **[N]** | PRAIRI |
| Tapering TNF inhibitors to withdrawal in sustained remission is **not** non-inferior to continuing (63% vs 5% flare) | **[N]** | ARCTIC REWIND |
| **Histological** synovial B-cell status did **not** significantly stratify rituximab vs tocilizumab response (45% vs 56%); only RNA-seq-defined status did | **[N]** | R4RA |
| Low-dose biologics were **not** associated with increased serious infection (OR 0.93, 0.65–1.33) | **[N]** | Singh network meta-analysis |
| Cardiovascular mortality excess was **not** significant when restricted to inception cohorts (SMR 1.19, 0.86–1.68) | **[N]** | Aviña-Zubieta meta-analysis |
| The symptom-duration/response gradient was **absent in smokers** | **[N]** | BARFOT |
| Otilimab (anti-GM-CSF) was statistically superior to placebo but only modestly (ACR20 ~51–55% vs 33–42%) | **[P/N]** | contRAst 1/2 |
| Four different early-RA treatment strategies **converged** by 2 years (42% remission), differing mainly in damage suppression | **[N]** | BeSt |

---

## 15. Register of active contradictions

Recorded rather than resolved, per Principle 10.

1. **GBD 2017 vs GBD 2021 prevalence** (246.6 vs 208.8 per 100,000 age-standardised) — same
   consortium, different cycles.
2. **Heritability ~60% (classical twin literature) vs additive genetic 12% (0–76%)** with shared
   environment 50% in a population twin study.
3. **"DMARDs should not be stopped" (guideline) vs 37% sustained drug-free remission at 5 years in
   never-bDMARD patients** (cohort) — the ascertainment-bias dispute in §9.2.
4. **Mortality gap widening (Olmsted) vs closing (British Columbia).**
5. **Methotrexate as an RA-ILD hazard (common clinical belief) vs methotrexate associated with
   reduced ILD progression and mortality** in a 69-study synthesis.
6. **Histology-based vs transcriptomics-based synovial stratification** giving opposite conclusions
   within the same trial.

---

## 16. What this baseline implies for later phases

Three structural observations, stated now because they should constrain how Phase 2 searches for
overlooked therapeutic possibilities:

1. **The biggest mechanism-free gap is non-inflammatory refractory disease and residual symptoms in
   remission.** Roughly 43% of refractory patients and a substantial fraction of patients in
   remission have symptoms that immunosuppression does not address, and for which there is *no
   established therapeutic strategy at all*. Any candidate intervention that plausibly acts on
   pain, fatigue or central sensitisation rather than on cytokine signalling is addressing a real,
   quantified, currently unmet need — and would be evaluable against existing outcome measures.
2. **The seronegative / autoantibody-negative subgroup behaves differently in every dataset
   examined** — prevention, drug-free remission, genetics, environment. Interventions should be
   evaluated *within* serostatus strata, and historical trials that pooled strata may have masked
   real effects.
3. **Remission as currently defined is a weak endpoint** (6% of established RA at 6 months, and
   consistent with ongoing ultrasound synovitis, symptoms and autoimmunity). Any claim that an
   intervention "induces remission" must specify which definition, and any strong claim requires
   objective inflammation measurement, not composite scores alone.

**No therapeutic recommendation is made in this document.** All efficacy statements are
attributions to specific cited studies with their evidence tier, not endorsements.

---

*Sources: `ra_phase1_references.csv` (77 records, each with PMID and DOI). Every quantitative
value in this document was read from the cited abstract during preparation.*
