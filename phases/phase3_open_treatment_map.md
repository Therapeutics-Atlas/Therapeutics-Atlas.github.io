> **Archived phase report — a dated record of what was believed at the time, not the current state of the project.**
> Statements superseded by later verification are listed in `data/corrections_log.csv`. Check that log before citing anything in this file.
> Current lead status is in `data/research_leads_status.csv`.

# Open Therapeutics #001 — Rheumatoid Arthritis
## Phase 3: Open Treatment Map

**Date:** 2026-08-31
**Built from:** Phase 1 evidence baseline (77 sources) and Phase 2 treatment landscape (67 interventions
across 12 domains). No new broad literature searches were run for this phase; the register below is an
integration of material already retrieved, with the machine-readable register saved as
`ra_open_treatment_map.csv` (115 rows).

---

## How to read this map

The map has six sections. Each row carries an **evidence tier**, and
the tiers are not interchangeable — a row in *What might be worth studying* is not a weaker version of a
row in *What works*; it is a different kind of claim.

| Tier | Meaning |
|---|---|
| **Established** | Replicated in humans across independent studies, or a fact about the disease that is not seriously disputed |
| **Probable** | Positive human evidence that is real but limited — single trial, one region, post-hoc, or unreplicated |
| **Uncertain** | Conflicting results, low-quality evidence base, or an effect whose size is not credible as reported |
| **Hypothesis** | Mechanistic, animal, subgroup-derived or uncontrolled — no adequate human test exists |
| **Unknown** | The question has not been asked in a form that could answer it |

Sub-labels in the tier column (e.g. *"Uncertain (same trial, opposite readings)"*) name the specific
reason the row sits where it does, so a reader can disagree with the placement on stated grounds.

**Unmet-need codes** carried forward from Phase 1, used throughout:

| Code | Unmet need |
|---|---|
| UN1 | Refractory inflammatory disease |
| UN2 | Pain, fatigue and residual symptoms despite controlled inflammation |
| UN3 | Sustained drug-free remission |
| UN4 | Predicting which treatment will work for an individual |
| UN5 | Prevention in at-risk individuals |
| UN6 | Toxicity and comorbidity burden |
| UN7 | Subgroup-specific disease (seronegative, difficult-to-treat, pathotype-defined) |
| UN8 | Repair of established structural damage |

!Open Treatment Map: state of evidence per unmet need, and the register of candidates carried forward

**Panel a** counts the 67 mapped interventions against the unmet need each addresses. Two findings are
structural rather than incidental: 41 of 67 interventions target refractory inflammatory disease, and
**UN4 — predicting individual response — has no candidate intervention in any tradition**, modern,
traditional or experimental. **Panel b** places the 22 candidates carried into section 6 by the strongest
evidence that exists for each today. Horizontal position is a statement about evidence, not about
promise; the grouping is by *why* an item qualifies, and the items are alphabetical within group.
Nothing in this map is ranked.

---

## 1. What we know

22 statements that are reasonably well established about the disease itself. These are the
constraints any therapeutic hypothesis has to survive.

| Topic | Statement | Tier | Source |
|---|---|---|---|
| Disease burden | GBD 2021: 17.6M cases (15.8-20.3), age-standardised prevalence 208.8/100k, +14.1% since 1990, F:M 2.45, projected 31.7M by 2050 | Established | PMID 37675071 |
| Autoimmunity precedes disease | Anti-CCP and RF detectable in stored blood a median 2.5 years before symptom onset; ACPA seropositivity precedes clinical RA by 3-5 years on average | Established | PMID 14558078 |
| Gene-environment interaction | HLA-DRB1 shared epitope x smoking for ACPA-positive RA: RR 8.7 (5.7-13.1); attributable proportion due to interaction 0.4-0.6 | Established | PMID 19180475 |
| Polygenic architecture | GWAS meta-analysis 29,880 cases / 73,758 controls: 101 loci, 98 candidate genes; RA loci enriched for approved drug targets | Established | PMID 24390342 |
| Occupational inhalant exposures | Silica RA OR 1.94 (1.46-2.58) in both seropositive and seronegative disease; 31-study review of silica, asbestos, solvents, pesticides, animal dust, exhaust: RR 1.25-1.49 | Established | PMID 33622738 |
| Tight control beats routine care | TICORA: good response 82% vs 44%, DAS28 remission 65% vs 16% | Established | PMID 15262104 |
| Treatment strategies converge | BeSt 2-year: all four strategies converged at 42% remission; initial combination better suppressed joint damage | Established | PMID 17332886 |
| First-line ceiling | NORD-STAR 48-wk CDAI remission: abatacept 59.3%, certolizumab 52.3%, tocilizumab 51.9%, active conventional 39.2% | Established | PMID 37423264 |
| Remission is an operational definition | 2011 ACR/EULAR provisional definition; 2022 Boolean2.0 (PtGA <=2 cm) raised 6-month remission from 14.8% to 20.6% (early) and 4.2% to 6.0% (established) with no loss of predictive value | Established | PMID 36357161 |
| Remission is not absence of disease | Power Doppler positivity in clinical remission: flare OR 4.52 (2.61-7.84), progressive erosion OR 12.80; ACPA+ memory B cells persist activated in clinical remission including under JAK inhibition | Established | PMID 26290588 |
| Residual symptoms persist in remission | 55-record systematic review: residual disability, tender/swollen joints, pain, fatigue and impaired patient global persist in a substantial fraction meeting remission or LDA targets | Established | PMID 33862450 |
| Refractory disease is a minority but not rare | 23 studies, 27,987 patients: D2T prevalence 11.7% (9.5-14.3); >=3 b/tsDMARD failures 4.3%; >=4 failures 1.6%; poly-refractory 2.7% | Established | PMID 39909563 |
| Refractory disease splits in two | Among D2T patients with ultrasound, 57% persistent inflammatory refractory (PIRRA) and 43% non-inflammatory refractory (NIRRA); NIRRA had higher BMI and fibromyalgia prevalence | Established | PMID 38073124 |
| Fibromyalgia co-occurrence distorts measurement | 34.2% of 187 RA patients met 2016 FM criteria; FM independently associated with higher DAS28-CRP driven by subjective components, worse QoL, and more corticosteroid use despite less DMARD use | Established | PMID 42333272 |
| Comorbidity burden | COMORA (3,920 patients, 17 countries): depression 15%, asthma 6.6%, MI/stroke 6%, solid malignancy 4.5%, COPD 3.5% | Established | PMID 24095940 |
| Excess cardiovascular mortality | Meta-SMR for cardiovascular mortality 1.50 (1.39-1.61); ischaemic heart disease 1.59; cerebrovascular 1.52 | Established | PMID 19035419 |
| RA-ILD is a major mortality driver | Denmark: RA-ILD in 2.2% of incident RA; 1-year mortality 13.9% vs 3.8%, 10-year 60.1% vs 34.5% | Established | PMID 28213571 |
| Treatment carries measurable risk | Serious infection vs csDMARDs: standard-dose biologics OR 1.31 (1.09-1.58), high-dose 1.90 (1.50-2.39). ORAL Surveillance: tofacitinib vs TNFi MACE HR 1.33 (0.91-1.94), cancer HR 1.48 (1.04-2.09), non-inferiority not shown | Established | PMID 25599825; PMID 35081280 |
| Synovium is heterogeneous between patients | Single-cell atlas, 79 donors, >314,000 cells: six cell-type abundance phenotypes spanning lymphocyte-rich to lymphocyte-poor, dynamic and associated with treatment response | Established | PMID 37217642 |
| Access is grossly unequal | COVAD-2 (n=1,997): advanced therapy use 29.6% overall; 44.0% Europe, 11.7% Asia, 5.3% Africa; 2.7% in low-HDI vs 38.8% in very-high-HDI countries | Established | COVAD-2 |
| Most guidance rests on low-certainty evidence | 2021 ACR guideline: 44 recommendations, 7 strong and 37 conditional. EULAR points to consider for D2T RA: strength of recommendation C-D throughout | Established | PMID 34101387 |
| Patients and physicians do not measure the same thing | 73 blinded RCTs, 165 comparisons, 33,956 patients: physician global SMD -0.60 vs patient global -0.50; DeltaSMD -0.09 (-0.12 to -0.05), driven by swollen joint count; pain independently associated only with patient global | Established | PMID 42330661 |

---

## 2. What works

17 interventions supported by evidence that is reliable enough to act on. "Works" here means
replicated human benefit on a stated outcome — it does not mean sufficient, and for most rows the
Phase 1 ceiling still applies: roughly 40% of patients do not reach remission on the best first-line
strategy tested.

| Intervention | What the evidence shows | Tier | Need | Source |
|---|---|---|---|---|
| Methotrexate anchor therapy | Cochrane 7 RCTs, 732 pts: ACR50 RR 3.0 (1.5-6.0) at 52 wk. Remission in at most about half of patients across RCTs | Established | UN1 | PMID 24916606 |
| Sulfasalazine | Cochrane 6 RCTs, 468 pts: SMD -0.49 joints, -0.42 pain, ESR -17.6 mm; withdrawal for adverse reactions OR 3.0 | Established | UN1 | PMID 10796400 |
| Hydroxychloroquine | Cochrane 4 RCTs, 300 pts: SMDs -0.33 to -0.52; weakest csDMARD for disease activity, retained for combination use and metabolic effects | Established | UN1,UN6 | PMID 10796401 |
| Triple csDMARD therapy | RACAT/TEAR: 78% vs 63% still on assigned therapy at 1 year vs MTX+etanercept | Established | UN1,UN6 | PMID 23992257 |
| Switching class after b/tsDMARD failure | Cochrane living NMA, 19 RCTs, 4,779 pts: untried TNFi ACR50 OR 6.04 (2.49-16.3) high certainty; IL-6 inhibitors, abatacept, rituximab and JAK inhibitors also moderate-to-high certainty | Established | UN1 | PMID 41978157 |
| Treat-to-target strategy | TICORA and BeSt: intensive targeted control outperforms routine care on remission and damage | Established | UN1 | PMID 15262104 |
| Early treatment (association) | Very early (median 3 mo) vs late early (12 mo) DMARD start: DAS28 improvement 2.8 vs 1.7 at 36 months with less radiographic progression | Probable | UN1 | PMID 15334426 |
| Denosumab for erosion repair | Erosion healing 20% vs 6% at 24 months (p=0.045), with no effect on inflammation | Probable | UN8 | Denosumab RCT |
| Physical activity for fatigue | Cochrane 24 studies, 2,882 pts: SMD -0.36 (-0.62 to -0.10), 14.4 points on a 100-point scale, NNTB 7 — the best-evidenced fatigue intervention in RA | Established | UN2 | PMID 37850523 |
| Psychosocial interventions for fatigue | Same Cochrane review: SMD -0.24 (-0.40 to -0.07), NNTB 10 | Established | UN2 | PMID 37850523 |
| Resistance and dynamic exercise | 10 RCTs, 547 pts: isokinetic strength +23.7%, isometric +35.8% (both P<0.001); RAPIT high-intensity weight-bearing exercise slowed hip bone loss over 2 years | Established | UN2,UN6 | Exercise meta-analysis; RAPIT |
| Anakinra | Cochrane 5 RCTs, 2,876 pts: ACR20 38% vs 23%, ACR50 18% vs 7%, ACR70 7% vs 2% — works, displaced by more effective agents | Established | UN1 | PMID 19160281 |
| Iguratimod added to methotrexate | 31 RCTs, 2,776 pts: ACR20 RR 1.55 (1.14-2.13), ACR50 RR 2.04, ACR70 RR 2.19 (GRADE high), DAS28 WMD -1.65, adverse events no different from MTX alone | Probable | UN1 | Iguratimod meta-analysis |
| TwHF added to methotrexate | ACR20 RR 1.44 (1.28-1.62), ACR50 RR 1.88, ACR70 RR 2.12; independent meta-analysis remission RR 1.31 (1.11-1.55) — but efficacy correlated negatively with trial quality in the same analysis | Probable | UN1 | TwHF consensus; TwHF meta-analysis |
| TwHF monotherapy is non-inferior to methotrexate | 19 RCTs, 1,795 participants: ACR20 RR 1.06 (0.90-1.26) and ACR50 RR 1.03 (0.80-1.34), both moderate GRADE certainty | Probable | UN1 | TwHF international consensus |
| Implanted vagus nerve stimulation | RESET-RA, 242 pts refractory to b/tsDMARDs: ACR20 35.2% vs 24.2% sham at 3 months (p=0.0209); related serious adverse events 1.6% | Probable | UN1,UN2 | RESET-RA |
| Low-dose glucocorticoids — with quantified harm | GLORIA, 451 pts aged 65+: DAS28 0.37 lower (p<0.0001) and damage 1.7 points lower (p=0.003); adverse events of interest 60% vs 49%, adjusted RR 1.24 (p=0.02) | Established | UN1 | PMID 36384861 |

!Phase 1: the therapeutic ceiling

---

## 3. What doesn't work

19 approaches with reasonably strong negative evidence, or with benefit that is
outweighed by harm. **These rows are results, not absences** — each represents a question that was asked
properly and answered in the negative, and each is worth as much as a positive row when deciding where
to look next.

| Intervention or claim | Negative finding | Tier | Source |
|---|---|---|---|
| Acupuncture vs sham | Cochrane 2 RCTs, 84 pts: no significant difference on ESR, CRP, VAS global, swollen or tender joints, GHQ or DAS. A CAM systematic review found no significant pain difference across 3 sham-controlled trials | Probable (contested — see Uncertain) | Cochrane acupuncture |
| Acupuncture for morning stiffness | Within a positive 32-RCT network meta-analysis, no acupuncture-related therapy outperformed DMARDs alone for morning stiffness | Probable | Acupuncture NMA |
| Low-dose naltrexone for pain | 7 RCTs in chronic pain: d = -0.11 (-0.96 to 0.74), P=0.31; adverse events IRR 1.4 (1.12-1.75). No RA-specific trial exists | Probable | LDN meta-analysis |
| Vitamin E | Sensitive joints MD -1.66 (-6.32 to 2.99), I2=93% — no benefit | Probable | Vitamin E meta-analysis |
| Balneotherapy mudpacks vs placebo | Cochrane 2015, 9 studies, 579 pts: pain MD 0.50 (-0.84 to 1.84) at very low level of evidence | Probable | Cochrane balneotherapy |
| Elemental diets | Cochrane dietary manipulation review: no difference in pain, function or stiffness | Probable | Cochrane diet |
| Food-allergen elimination (on average) | 94 seropositive patients, 12 weeks, double-blind: only subjective improvement overall, no difference between allergen-free and allergen-restricted diets | Probable | PMID 1740869 |
| Smoking-cessation interventions in RA | Cochrane: 2 studies, 57 patients, no evidence of benefit at very low certainty — despite smoking being an established causal risk factor | Unknown (untested, not disproven) | Cochrane smoking cessation |
| IV doxycycline | n=23: 1 responder vs 0 on placebo | Probable | Doxycycline RCT |
| Blood-flow-restricted low-intensity resistance training | SMD -0.01 — no effect | Probable | BFR meta-analysis |
| TwHF monotherapy as an improvement on methotrexate | Non-inferior, not superior: ACR20 RR 1.06 (0.90-1.26) | Probable | TwHF consensus |
| Iguratimod monotherapy as an improvement on methotrexate | 12 trials: ACR20 OR 1.04 (0.79-1.36) | Probable | Iguratimod meta-analysis |
| Methotrexate + glucocorticoid to prevent RA in ACPA-positive at-risk individuals | TREAT EARLIER: no prevention at 2 years (19% vs 18%, HR 0.81); at 5 years ACPA-positive 58% vs 65%, HR 0.7 — no effect | Established | TREAT EARLIER |
| Abatacept for durable prevention | APIPPRA: primary endpoint met on treatment (6% vs 29%) but 25% vs 37% progressed by 24 months; ALTO extension at median 55 months shows a 4.9-month arthritis-free survival difference that diminished | Established | APIPPRA; ALTO |
| Rituximab for prevention | PRAIRI: single 1000 mg infusion delayed arthritis onset by 12 months, HR 0.45 (0.154-1.322) — delay, not prevention | Established | PRAIRI |
| Tapering TNF inhibitors to withdrawal | ARCTIC REWIND: flare in 27/43 (63%) vs 2/41 (5%) on stable therapy; risk difference 58% (42-74) — not non-inferior | Established | ARCTIC REWIND TNFi |
| p38 MAPK inhibition | Early ACR20 signal did not sustain across outcomes; no drug emerged | Established | p38 programme |
| Total lymphoid irradiation | Symptomatically effective short-term; at 10 years 7/10 irradiated patients had died vs 2/9 controls, with 3 B-cell malignancies | Established | TLI long-term follow-up |
| Opioids as a strategy | Cochrane 11 studies, 672 pts: global impression RR 1.44 (1.03-2.03) but adverse events OR 3.90 (2.31-6.56); only one 20-patient study of a strong opioid | Probable | Cochrane opioids |

---

## 4. What is uncertain

22 items where the evidence conflicts, is too weak to settle the question, or where two
defensible readings of the same data disagree. **Conflicts are preserved here rather than resolved.**

| Item | The unresolved state | Tier | Need | Source |
|---|---|---|---|---|
| Acupuncture for pain | Null vs same-acupoint sham (Cochrane) but SMD -1.11 (conventional) to -1.42 (electroacupuncture) vs conventional therapy and non-acupoint sham in a 10-RCT network meta-analysis. The dispute is about which sham is a valid control, not about the data | Uncertain (conflict preserved) | UN2 | Cochrane acupuncture; 2025 acupuncture NMA |
| Vitamin D in established RA | DAS-28 WMD -0.83 (-1.38 to -0.28) at self-declared moderate certainty in one meta-analysis; no significant effect on RA pain across 27 RCTs in another. May be outcome-specific rather than a true contradiction | Uncertain (conflict preserved) | UN1,UN2 | Two vitamin D meta-analyses |
| Vitamin D and omega-3 for prevention | VITAL (n=25,871): on treatment vitamin D HR 0.78 (0.61-0.99) and omega-3 HR 0.85 (0.67-1.08); two years after stopping, vitamin D HR 0.98 (0.83-1.17) and omega-3 HR 0.83 (0.70-0.99). Endpoint is all autoimmune disease, not RA | Uncertain (same trial, opposite readings) | UN5 | VITAL; VITAL extension |
| Mediterranean / anti-inflammatory diet | Cochrane: Cretan Mediterranean pain MD -14.00/100 (-23.6 to -4.37) and fasting+vegetarian pain MD -1.89/10; an overview of systematic reviews concludes little or no difference at low certainty; 7-RCT pooling gives pain -9.22 mm at very low certainty | Uncertain (conflict preserved) | UN2 | Cochrane diet; SR overview |
| Statins as RA disease-modifying therapy | Atorvastatin add-on DAS28 SMD -2.00 (-3.19 to -0.81) across 15 RCTs; parallel review -2.46 with I2=97%. An effect larger than most biologics from a lipid-lowering drug is more plausibly a pooling artefact | Uncertain (effect size not credible as stated) | UN1 | Two statin meta-analyses |
| Radiation synovectomy | Meta-analysis of 21 studies OR 4 (1.2-14) for knee response at 6 months; a 97-patient RCT found 48% response in both arms | Uncertain (randomisation contradicts pooling) | UN1 | Radiosynovectomy meta-analysis; RCT |
| TwHF safety | Trial-level pooling reassuring (infection RR 1.37, liver RR 1.14, renal RR 2.20, none significant) against 40 years of toxicology documenting oligospermia, testicular atrophy, amenorrhoea and infertility. Short trials in older cohorts cannot detect gonadal toxicity | Uncertain (different timescales, both real) | UN1,UN6 | TwHF safety pooling; TwHF toxicology |
| Curcumin | DAS28 MD -1.20 (-1.85 to -0.55) from 6 publications the authors describe as low quality — a biologic-sized effect from six small trials | Uncertain | UN1 | Curcumin meta-analysis |
| Omega-3 in established RA | Tender joint count SMD -0.59 (-0.79 to -0.39) across 18 RCTs, 1,018 pts, with no significant effect on DAS28, ESR or CRP — symptom effect without inflammatory effect | Uncertain | UN2 | Omega-3 meta-analysis |
| Probiotics | IL-6 SMD -0.83, TNF-alpha -0.41, CRP -0.67 (I2=80.8%); no pooled disease-activity or joint-count outcome reported | Uncertain (surrogate outcomes only) | UN1 | Probiotics meta-analysis |
| Periodontal treatment | Disease activity SMD -0.88 (-1.38 to -0.38) across 9 studies, 388 pts, at low/very low GRADE certainty with selection bias and unstable RA medication as heterogeneity sources | Uncertain | UN1,UN5 | Periodontal meta-analysis |
| Metformin add-on | 4 RCTs, 350 pts: CRP MD -5.55 (-7.46 to -4.52), DAS-28 MD -0.8, HAQ-DI -0.12 | Uncertain (promising, thin) | UN1,UN6 | Metformin meta-analysis |
| Tetracyclines | 10 RCTs: TJC SMD -0.39 (-0.74 to -0.05), 3 of 10 trials high quality | Uncertain | UN1 | Tetracycline meta-analysis |
| Mesenchymal stem cells | 64 patients, uncontrolled, DAS28 and HAQ lower at 1 and 3 years vs pretreatment while remaining on DMARDs; pooled MSC safety across autoimmune indications gives AE RR 2.35 (0.58-9.58) | Uncertain (no control group) | UN1 | MSC cohort; MSC safety pooling |
| Mindfulness | Clearest effect on depressed mood (MBCT depression SMD -0.72, -1.22 to -0.22) rather than pain or disease activity; unblindable with an active-control problem | Uncertain | UN2 | Mindfulness meta-analysis |
| Cannabis-based medicine | One 58-patient 5-week RCT: significant improvement in pain on movement, pain at rest, sleep quality and DAS28; no effect on morning stiffness. Nothing since 2006 | Uncertain (single small trial) | UN2 | Sativex RA RCT |
| Selenium | VAS pain MD -12.68 mm (-19.08 to -6.28) from 7 small studies; narrow therapeutic window | Uncertain | UN2 | Selenium meta-analysis |
| Tai chi | Cochrane 7 trials, 345 participants: pain MD -2.15 (-3.19 to -1.11), a 22% absolute improvement, but from 2 studies and 81 participants at very low quality; disease activity inconclusive; ~75% of trials did not report random sequence generation | Uncertain | UN2 | Cochrane tai chi |
| Total glucosides of paeony | 8 RCTs, 1,209 pts: improved ACR20/50/70 as csDMARD add-on and reduced adverse effects, at limited methodological quality | Uncertain | UN1,UN6 | TGP meta-analysis |
| Sinomenine | 10 trials, 1,185 pts vs NSAIDs: more improved patients and more RF disappearance (P<0.00001; P=0.008), better morning stiffness and ESR; no difference in swollen joints, grip strength or CRP. NSAID comparator cannot support a disease-modifying claim | Uncertain | UN1 | Sinomenine meta-analysis |
| The window of opportunity | Earlier treatment associates with better outcomes, but the strongest study is a 20-per-arm case-control, no RCT has randomised time-to-treatment, and the duration-response gradient is absent in smokers (BARFOT, n=1,587) | Uncertain (association established, mechanism not) | UN1 | PMID 15334426; BARFOT |
| Whether ACPA-negative RA is one disease | Different genetics and environmental associations; 10-year drug-free remission 26.6%, diagnosis change 12.8%; apparently preventable where ACPA-positive disease is not | Uncertain | UN7 | Olmsted seronegative cohort; TREAT EARLIER 5-year |

!Phase 2: effect size against methodological rigour

The pattern in this figure is the single most important interpretive caveat in the whole map: across the
Phase 2 corpus, the largest reported effect sizes come from the least rigorous evidence, and the
best-designed syntheses report the smallest effects. Any large effect reported from a small or
low-quality trial in this map should be read as a hypothesis about an effect, not as an effect.

---

## 5. What we don't know

13 gaps. A gap is different from a negative result: nothing here has been shown not to
work — the question has not been asked in a form capable of answering it.

| Gap | Why it is open | Tier | Need | Source |
|---|---|---|---|---|
| Which drug for which patient | No validated treatment-allocation tool exists. Synovial RNA-seq models reach AUC 0.75-0.87 for response and multidrug resistance but none has been prospectively tested as an allocation rule; drug selection remains sequential trial-and-error at 3-6 months per failed cycle | Probable for prediction; no evidence for clinical utility | UN4 | R4RA; STRAP |
| No intervention exists for response prediction | Across 67 interventions in 12 traditions surveyed in Phase 2, zero address UN4. This is an empty intervention space, not a contested one | Established (about the corpus) | UN4 | ra_phase2_treatment_map.csv |
| Who can safely stop treatment | No patient who ever needed a bDMARD achieved sustained DMARD-free remission, versus 37% at 5 years of those who never did. Withdrawal trials are run in the population where DFR essentially never occurs | Uncertain (ascertainment bias argued, not proven) | UN3 | Leiden EAC/tREACH |
| Why ACPA-negative at-risk disease appears preventable | TREAT EARLIER 5-year: RA in 3/35 (9%) vs 10/31 (32%) in ACPA-negative at-risk participants, HR 0.24 (0.07-0.87), NNT 4; no effect in ACPA-positive. Single post-hoc subgroup, n=66 | Probable (single post-hoc subgroup) | UN5,UN7 | TREAT EARLIER 5-year |
| What maintains inflammation in PIRRA | A stromal/fibroblast signature marks multidrug resistance; spatial data describe fibrogenic vascular niches with COMP-high fibroblasts and Notch-driven TGF-beta signalling expanding after immune depletion. Never tested interventionally | Hypothesis | UN1 | R4RA molecular; spatial transcriptomics |
| What to do for NIRRA | 43% of difficult-to-treat patients have high disease activity scores without objective inflammation. They receive escalating immunosuppression with no mechanistic rationale and no established alternative | Established as a phenomenon; no established treatment | UN2 | D2T ultrasound cross-sectional |
| True attributable fraction of modifiable exposure | Population twin data: additive genetic variance 12% (0-76%), shared environment 50% (0-72%) — compatible with a far larger modifiable component than the commonly quoted ~60% heritability implies | Uncertain | UN5 | Population twin study |
| Whether tolerance can be induced rather than immunity suppressed | Peresolimab is the first clinical test of agonising an inhibitory checkpoint in RA; Treg and low-dose IL-2 approaches have reviews but no controlled RA efficacy trial; CAR-T experience in RA is minimal | Hypothesis / early clinical | UN3 | Peresolimab; Treg reviews |
| Why the joint, and why symmetrically | No current causal model explains the anatomical specificity or symmetry of RA | Unknown | — | Phase 1 open question 10 |
| Causal direction of the gut-joint axis | Dysbiosis reported in preclinical and established RA and partially normalised after treatment; causal direction unresolved. No RA efficacy trial of faecal microbiota transplantation or helminth therapy exists | Hypothesis | UN5 | Gut-joint reviews |
| How to repair existing damage | Denosumab (erosion healing 20% vs 6%) is the only intervention in the entire survey addressing structural repair, and it does not affect inflammation | Probable for one agent; unknown otherwise | UN8 | Denosumab RCT |
| Whether subgroup-specific treatment strategies exist | Only 2 of 67 interventions map to UN7, both incidentally. No intervention has been developed or tested for a defined RA subgroup | Established (about the corpus) | UN7 | ra_phase2_treatment_map.csv |
| Whether sleep is a modifiable target | 5 studies, 262 patients, no consistent or conclusive evidence, despite sleep disturbance being near-universal in RA | Unknown | UN2 | Sleep SR |

---

## 6. What might be worth studying

**Not ranked, not endorsed, not claimed to be effective.** Inclusion here means only that an item has a
specific, stated reason to be looked at again — a positive result that was abandoned for non-scientific
reasons, a subgroup signal inside an otherwise negative trial, an anomaly, or a gap with a concrete
rationale. Several of these will turn out to be nothing. The grouping below is by the *type* of reason,
which is a category, not an ordering.

### Abandoned despite evidence (4)

| Candidate | What exists today | Tier | Need | Source |
|---|---|---|---|---|
| Autologous HSCT in refractory RA | >=ACR50 at some point in 49/76 (67%) with severe refractory disease; abandoned when biologics arrived, without a head-to-head comparison | Uncertain (uncontrolled, superseded without comparison) | UN1,UN3 | HSCT series |
| Dapsone | 1980s-90s RCTs: improvement in 5 of 7 clinical measures and ESR. Never re-tested with modern methods or outcomes | Uncertain (old positive RCTs) | UN1 | Dapsone RCTs |
| Prosorba protein A immunoadsorption | 99 patients, mean 15.4 years' disease, >5 prior DMARDs: ACR response 28.9% vs 10.6% on sham (p=0.005; 41.7% vs 15.6% among completers). Withdrawn on cost and practicality as biologics arrived | Probable (positive sham-controlled RCT, not replicated since) | UN1 | Prosorba RCT |
| The 1991 fasting + vegetarian diet trial | 27 vs 26 patients: significant improvement in tender joints, Ritchie index, swollen joints, pain, morning stiffness, grip strength, ESR, CRP, white cell count and HAQ, sustained at one year, with only pain improving in controls. Single-blind, residential, unmatched control setting | Uncertain (strongest historical dietary result, never adequately replicated) | UN2 | PMID 1681264 |

### Unexplained absence from practice (3)

| Candidate | What exists today | Tier | Need | Source |
|---|---|---|---|---|
| IL-17 inhibition in RA | Pooled ACR20 RR 1.67 (1.40-2.00) in TNF-inadequate responders across 10 studies; class established in PsA and axSpA but not used in RA. No retrieved source documents why | Uncertain (positive pooled data, unexplained absence) | UN1 | IL-17 pooling |
| Iguratimod outside East Asia | Largest non-Western RCT base in the survey (31 RCTs, 2,776 pts; ACR70 RR 2.19 at GRADE high certainty as MTX add-on) and essentially unknown in Western practice; no independent non-Chinese/Japanese trial retrieved | Probable, but geographically confined evidence | UN1 | Iguratimod meta-analysis |
| Sirukumab and other shelved biologics | Positive phase 3 ACR20 (40% vs 24%; 53.5%/54.8% vs placebo) without licensure; ocrelizumab DAS28 response RR 3.77 (2.47-5.74) with RA development stopped while the same molecule succeeded in MS | Established efficacy; development discontinued | UN1 | Sirukumab; ocrelizumab RA trials |

### Subgroup or anomaly signal (4)

| Candidate | What exists today | Tier | Need | Source |
|---|---|---|---|---|
| ACPA-negative at-risk prevention | TREAT EARLIER 5-year post-hoc: HR 0.24 (0.07-0.87), NNT 4 in ACPA-negative at-risk participants where ACPA-positive showed nothing. n=66, post-hoc, never independently replicated | Probable but single post-hoc subgroup | UN5,UN7 | TREAT EARLIER 5-year |
| Anakinra / IL-1 blockade in defined subgroups | Cochrane-confirmed efficacy (ACR20 38% vs 23%) displaced by more effective agents on average. Whether an IL-1-driven subgroup exists has not been tested with modern stratification | Established for average effect; hypothesis for subgroup | UN1,UN7 | PMID 19160281 |
| Never-bDMARD patients as the drug-free remission population | 37% (5 y) vs 0% sustained DMARD-free remission depending only on whether a bDMARD was ever needed. Withdrawal trials have been run in the wrong population if this is a marker rather than a consequence | Uncertain (ascertainment bias argued, not proven) | UN3 | Leiden EAC/tREACH |
| The food-intolerance subgroup | In a 94-patient double-blind elimination study negative on average, 9 patients improved and then flared markedly on rechallenge with changes in objective activity measures. Never retested in >30 years | Hypothesis (rechallenge-defined subgroup within a negative trial) | UN2,UN7 | PMID 1740869 |

### Early uncontrolled signal (1)

| Candidate | What exists today | Tier | Need | Source |
|---|---|---|---|---|
| CD19-directed immune reset | CD19xCD3 bispecific engager on compassionate use in 6 multidrug-resistant patients: rapid decline in disease activity in all six, activated memory B cells replaced by IgD+ naive B cells, no clinically relevant CRS | Hypothesis (n=6, uncontrolled) | UN1,UN3 | CD19xCD3 case series |

### Untested gap (9)

| Candidate | What exists today | Tier | Need | Source |
|---|---|---|---|---|
| Helminth therapy and faecal microbiota transplantation | Both follow directly from the mucosal-origins hypothesis; neither has any RA efficacy trial | Hypothesis | UN5 | Gut-joint reviews |
| Non-immunosuppressive strategies for NIRRA | 43% of difficult-to-treat patients have no objective inflammation, higher BMI and 15-38% fibromyalgia prevalence, and currently receive escalating immunosuppression. No trial has randomised a non-immunosuppressive strategy in an imaging-defined NIRRA population | Established as a phenomenon; no intervention tested | UN2 | D2T ultrasound cross-sectional |
| RA-specific cannabinoid and low-dose naltrexone data | LDN is negative for pain overall (d=-0.11) with a positive fibromyalgia subgroup (d=-0.34), and ~34% of RA patients meet fibromyalgia criteria. Cannabis has one 58-patient RA trial from 2006. Both are used off-label without RA-specific evidence | Uncertain (subgroup rationale, no RA trial) | UN2 | LDN meta-analysis; Sativex RCT; FM prevalence cohort |
| Sleep as a target | Near-universal symptom, 5 studies and 262 patients in total, no conclusion possible | Unknown | UN2 | Sleep SR |
| Stromal / fibroblast-directed therapy in PIRRA | Fibroblast COMP and endothelial Notch-driven TGF-beta signalling expand after immune depletion in non-remitting patients. If disease becomes stromally autonomous, no immune-targeted drug can resolve it | Hypothesis (mechanistic, never tested interventionally) | UN1 | Spatial transcriptomics |
| Total glucosides of paeony as a tolerability agent | Reported to improve ACR responses and reduce adverse effects when added to csDMARDs. The adverse-effect reduction is the less studied of the two claims and maps to a top patient priority | Uncertain (limited methodological quality) | UN6 | TGP meta-analysis |
| Transcutaneous (non-invasive) vagus nerve stimulation | Open-label pilot, 16 patients, 4 days: DAS28-CRP 4.1->3.8 (p=0.02) in the high-activity cohort and no effect in the low-activity cohort. The implanted route now has a positive sham-controlled pivotal trial; the non-invasive route has never been sham-tested in RA | Hypothesis (uncontrolled pilot) with a proven mechanism upstream | UN1,UN2 | tVNS pilot; RESET-RA |
| Treg and low-dose IL-2 therapy | The approaches most directly aimed at drug-free remission have the thinnest RA clinical evidence base of any modern strategy — reviews only, no controlled RA trial | Hypothesis | UN3 | Treg reviews |
| Whether TwHF's active constituents can be separated from gonadal toxicity | Efficacy comparable to methotrexate with a 40-year reproductive toxicology record. The efficacy and the toxicity have not been attributed to the same or different constituents in the retrieved evidence | Probable for efficacy; established concern for toxicity | UN1,UN6 | TwHF consensus; TwHF toxicology |

### Conflict to resolve (1)

| Candidate | What exists today | Tier | Need | Source |
|---|---|---|---|---|
| Sham design in acupuncture trials | Whether same-acupoint sham is an inert control is an empirical question that determines whether a large body of positive evidence is real or artefactual, and it has not been settled by any retrieved study | Unknown (methodological) | UN2 | Cochrane acupuncture; 2025 NMA |

---

## Cross-cutting distinctions preserved from earlier phases

### Patient-generated priorities
The James Lind Alliance priority-setting work and the patient-versus-physician comparison literature
place **pain, fatigue and the ability to live normally** at the top of the patient agenda, while the
research corpus is organised around inflammatory disease control. Physician global assessment and
patient global assessment diverge systematically, and the divergence is largest in exactly the patients
whose residual symptoms are not inflammatory. The map reflects this mismatch quantitatively: 41 of 67
interventions address UN1 (refractory inflammation); 23 address UN2 (pain, fatigue, residual symptoms),
and most of those sit in the *Uncertain* or *Poorly studied* classes.

### Abandoned-but-effective treatments
Four interventions in this map have positive controlled human evidence and left practice anyway
(Prosorba immunoadsorption, dapsone, the 1991 fasting/vegetarian diet trial, autologous HSCT), and three
more have positive pooled or trial-level data but never entered RA practice (IL-17 inhibition,
sirukumab and comparable shelved biologics, iguratimod outside East Asia). In no retrieved source is the
discontinuation decision documented as an efficacy failure. This is a distinct category from "failed" and
is kept separate throughout.

### Subgroup effects
Four candidates exist only as subgroups inside trials whose overall result was null or was never
stratified: the food-intolerance subgroup defined by rechallenge, IL-1 blockade in a defined subgroup,
ACPA-negative at-risk prevention, and the never-bDMARD population in which drug-free remission actually
occurs. Phase 1 recorded that autoantibody-negative disease should be stratified rather than pooled;
that instruction applies to every row in this map that reports an average effect.

### Conflicts left open
Two conflicts are recorded without resolution, without forcing a conclusion. First, acupuncture: positive in syntheses
using conventional-therapy or non-acupoint controls, negative against sham for pain, with an active
methodological dispute over whether any sham needle is an inert control. Second, an interleukin-targeting
class with statistically positive pooled RA responses that did not become an RA therapy, with no
retrieved source documenting why.

### Negative results retained
Section 3 exists so that the 19 properly-answered negative questions are not silently dropped from the
project's memory. Where a later phase proposes a mechanism that has already been tested and failed, that
section is the first place to check.

---

## Limitations of this map

1. **Abstract-level evidence.** Phases 1 and 2 screened and extracted from abstracts and synthesis
   conclusions, not full texts. Numeric values quoted here were read from source abstracts, but effect
   estimates, subgroup definitions and risk-of-bias detail were not verified against full papers.
2. **English-language databases only.** PubMed and OpenAlex were searched. CNKI, Wanfang and other
   Chinese-language databases were not, which systematically under-samples the TCM literature — in both
   directions, since that literature contains both unretrieved positive trials and unretrieved
   methodological criticism.
3. **Retrieval is not exhaustive.** Several targeted searches returned nothing and were left unretrieved
   rather than substituted. Absence from this map is weak evidence of absence from the literature.
4. **The verdict classes are judgements.** Assignment of an intervention to "Works", "Uncertain" or
   "Failed" is the analyst's reading of the cited source, not a formal GRADE assessment.
5. **No new searching in Phase 3.** This phase integrated existing material rather than searching anew. Anything
   published or retrievable but not surfaced in Phases 1-2 is absent here too.

---

## What this document does not do

It does not rank the candidates in section 6, does not propose Research Leads, and does not claim that
any intervention is effective. Every efficacy statement is an attribution to a specific cited study at a
stated evidence tier. Determining whether any of these signals is real requires the appropriate
scientific and clinical validation, which no amount of evidence synthesis can substitute for.

---

*Companion files: `ra_open_treatment_map.csv` (this map, machine-readable, one row per item),
`ra_phase2_treatment_map.csv` (67 interventions with verbatim key results),
`ra_phase1_references.csv` (77 sources), `ra_phase1_open_questions.csv`.*
