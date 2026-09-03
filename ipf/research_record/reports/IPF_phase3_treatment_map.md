# Phase 3 — Open Treatment Map: Idiopathic Pulmonary Fibrosis

Open Therapeutics / Open Evidence Record. Date: 2026-09-02. Scope: `IPF_SCOPE.md` (locked).
Inputs: Phase 0 selection, Phase 1 baseline, Phase 2 landscape and registers. No new grading rules
were introduced in this phase; every tier in the map is inherited from the row it derives from.

The map is a statement-level table (`ipf_phase3_treatment_map.csv`, 75 statements) plus a
per-intervention spine (`ipf_phase3_map_spine.csv`, 73 graded interventions) that links
every graded intervention to the statements it appears in. Statements carry the outcome dimension
they are about; a statement about one dimension licenses nothing about another.

---

## 0. What this phase did before assembling anything

Two defects in the earlier record were found and corrected first, because the map would otherwise
have propagated them.

**Endpoint codes (corrections entry C10).** Endpoint codes cited in the Phase 2 report and in
several landscape rows did not correspond to the Phase 1 taxonomy (`ipf_phase1_endpoint_taxonomy.csv`).
Only the codes were wrong — dimension names, verdicts, tiers and effect estimates were unaffected.
Both Phase 2 files were re-issued.

**A retrieval artefact in our own record (corrections entry C11).** Phase 2 graded 17 entities with
a phase-3 registry label as "Poorly studied — no IPF-specific human outcome evidence retrieved".
Inspection showed that some of those programmes have published primary reports. A targeted retrieval
check was run on all 17 before any Phase 4 screening, and six were reclassified from retrieved
abstracts with verbatim quotes:

| Entity | Was | Now | Basis |
|---|---|---|---|
| ziritaxestat | Poorly studied | **Failed** (Established) | ISABELA 1/2 phase 3, null on annual FVC decline (PMID 37159034) |
| ART-123 (thrombomodulin alfa) | Poorly studied | **Failed** (Probable) | day-90 survival 72.5% vs 89.2% placebo in acute exacerbation (PMID 31917621) |
| deupirfenidone | Poorly studied | **Uncertain** (Probable) | ELEVATE-IPF phase 2b positive at 26 weeks (PMID 42085224) |
| admilparant (BMS-986278) | Poorly studied | **Uncertain** | phase 2 IPF-cohort CI includes zero; significant estimate is the PPF cohort (PMID 39393084) |
| INS018_055 (rentosertib) | Poorly studied | **Uncertain** (Hypothesis) | phase 2a, safety primary endpoint, exploratory FVC signal (PMID 40461817) |
| NAL ER (nalbuphine ER) | Poorly studied | **Works — cough (E9) only** (Probable) | CORAL phase 2b and CANAL crossover (PMID 41569557, 38320144) |

The `co-trimoxazole or doxycycline` registry label was resolved as the CleanUP-IPF strategy evidence
and cross-referenced to the two agent rows rather than counted separately. The Phase 1 cough ceiling
row was updated: the best documented placebo-adjusted reduction in objective cough frequency is now
CORAL's 60.2% relative reduction versus 16.9% with placebo at 6 weeks, not low-dose morphine at day 14.

The eleven other phase-3-labelled entities returned no IPF randomised report and remain
"Poorly studied". **The methodological consequence is carried into the map as statement M5.9**: the
Phase 2 per-entity search under-retrieves for agents whose registry label is a code name or a
two-drug string, so the 208 remaining "Poorly studied" rows are an upper bound on genuine absence of
evidence rather than a count of it.

Verdict distribution after these corrections: **7 Works, 11 Failed, 8 Harm outweighs benefit,
1 Conflicting, 46 Uncertain, 208 Poorly studied.**

No change to `IPF_SCOPE.md` or to any prespecified rule was required. The map inherits Phase 2
tiers; Phase 3 did not re-tier anything.

---

## 1. S1 — What works

Seven interventions, none of them tiered above **Probable**, each graded on one outcome dimension.

| ID | Statement | Outcome dimension | Tier | Source |
|---|---|---|---|---|
| M1.1 | Nintedanib slows the rate of FVC decline over 52 weeks in IPF. No effect on survival was demonstrated. | rate of FVC decline (E1) | Probable | PMID 24836310 |
| M1.2 | Pirfenidone reduces the proportion of patients reaching a >=10 percentage-point FVC decline or death at 52 weeks, and slows FVC decline. Two of three phase 3 trials met their primary endpoint. | prevention of categorical progression (E3), rate of FVC decline (E1) | Probable | PMID 24836312 |
| M1.3 | Nerandomilast slows FVC decline at 52 weeks in IPF. Its mortality and acute-exacerbation endpoints were not statistically significant, and its 2025 approval is a PPF-wide label rather than IPF-specific. | rate of FVC decline (E1) | Probable | PMID 40387033 |
| M1.4 | Inhaled treprostinil slows FVC decline at 52 weeks in IPF. | rate of FVC decline (E1) | Probable | PMID 41812190 |
| M1.5 | Nalbuphine ER reduces objective cough frequency in IPF-associated cough over 3-6 weeks, replicated across two randomised trials. | symptoms - cough (E9) | Probable | PMID 41569557 |
| M1.6 | Pulmonary rehabilitation and exercise training improve exercise capacity and health-related quality of life in the short term. Durability beyond about six months is not established and no effect on lung-function decline, exacerbation or survival is claimed. | functional capacity (E5), HRQoL (E6) | Probable | PMID 33164264 |
| M1.7 | Lung transplantation is the only intervention in this record with evidence of extended survival in IPF. The evidence is observational registry data and a randomised comparison is not feasible. | survival (E11) | Probable | PMID 37625610 |

Three things this section deliberately does not say. No statement here claims preservation of lung
function, recovery of lost function, reversal of fibrosis, or cure. No drug statement here claims a
survival benefit — the only survival evidence in the record is observational, for transplantation.
And every drug statement rests on FVC or an FVC-based composite, which is the unresolved surrogacy
question preserved as M3.11.

---

## 2. S2 — What does not work

Twenty statements: eleven adequately-tested-and-negative, eight where harm exceeded benefit, and one
statement about the 48 programmes that stopped before producing any result.

| ID | Statement | Outcome dimension | Tier | Source |
|---|---|---|---|---|
| M2.1 | Interferon gamma-1b did not improve progression-free survival in IPF in an adequately sized randomised trial; a later survival trial was also null. | progression-free survival (time to disease progression or death) | Probable | PMID 14711911 |
| M2.2 | Bosentan was null on its own primary endpoints in two phase 3 randomised trials in IPF. | hospital-free survival and overall survival | Probable | PMID 21474646 |
| M2.3 | Co-trimoxazole did not improve FVC in an adequately sized randomised trial in IPF. | forced vital capacity (FVC) | Probable | PMID 23143842 |
| M2.4 | Adding co-trimoxazole or doxycycline to usual care did not improve time to non-elective respiratory hospitalisation or death (CleanUP-IPF); this registry label is the same evidence as the two agent rows. | hospitalisation or death (composite; E10/E11) | Established | PMID 33974018 |
| M2.5 | N-acetylcysteine monotherapy was null on FVC change in an adequately sized randomised arm (PANTHER-IPF); post hoc genotype subgroup analyses remain an open question rather than a positive result. | Change in forced vital capacity, percentage of predicted vital capacity, percentage of predicted carbon monoxide diffusi | Probable | PMID 24836309 |
| M2.6 | Simtuzumab did not improve progression-free survival in IPF in an adequately sized randomised trial. | progression-free survival (time to all-cause death or categorical decrease from baseline in FVC % predicted) | Probable | PMID 27939076 |
| M2.7 | SAR156597 (IL-4/IL-13 bispecific) was null on FVC in an adequately sized randomised trial in IPF. | absolute change from baseline in forced vital capacity (FVC) % predicted at 52 weeks | Probable | PMID 30337444 |
| M2.8 | Zinpentraxin alfa (recombinant pentraxin-2) was null on 52-week FVC change in phase 3 after a positive phase 2 result. | absolute change from baseline to Week 52 in FVC | Probable | PMID 38354066 |
| M2.9 | Pamrevlumab was null on 52-week FVC change in an adequately sized phase 3 trial (ZEPHYRUS-1) after a positive phase 2 result on the same endpoint. | change from baseline in percentage of predicted forced vital capacity (FVC) at week 48 | Probable | PMID 38762797 |
| M2.10 | Ziritaxestat did not improve the annual rate of FVC decline in either of two phase 3 trials (ISABELA 1/2), which were terminated early on benefit-risk grounds. | rate of FVC decline (E1) | Established | PMID 37159034 |
| M2.11 | Thrombomodulin alfa did not improve day-90 survival after acute exacerbation of IPF; survival was numerically lower than placebo (72.5% vs 89.2%). | survival after acute exacerbation (E10/E11) | Probable | PMID 31917621 |
| M2.12 | Prednisone + azathioprine + N-acetylcysteine caused excess death and hospitalisation in IPF and was withdrawn at interim analysis (PANTHER-IPF); it had been recommended practice before 2012. | mortality and hospitalisation (harm) | Probable | PMID 22607134 |
| M2.13 | Warfarin anticoagulation increased death, hospitalisation and other events in IPF and the trial was stopped for harm. | composite outcome of time to death, hospitalization (nonbleeding, nonelective), or a 10% or greater absolute decline in  | Probable | PMID 22561965 |
| M2.14 | Ambrisentan increased disease progression and respiratory hospitalisation in IPF and the trial was stopped early. | Time to disease progression (death, respiratory hospitalization, or categorical decrease in lung function) | Probable | PMID 23648946 |
| M2.15 | Riociguat showed excess harm in IPF with suspected pulmonary hypertension and the trial was terminated. | change in 6-min walking distance (6MWD) | Probable | PMID 31416769 |
| M2.16 | Carlumab (anti-CCL2) worsened the rate of FVC change in IPF and the trial was stopped. | rate of percentage change in forced vital capacity (FVC) | Probable | PMID 26493793 |
| M2.17 | BG00011 (anti-alpha-v-beta-6) showed excess serious adverse events and worse outcomes in IPF and development stopped. | FVC change from baseline | Probable | PMID 35771569 |
| M2.18 | Cyclophosphamide added to glucocorticoids increased 3-month mortality in acute exacerbation of IPF (EXAFIP). | 3-month all-cause mortality | Probable | PMID 34506761 |
| M2.19 | Corticosteroid exposure is associated with excess mortality in IPF in pooled, predominantly observational data; no randomised monotherapy trial exists and confounding by indication cannot be excluded. | overall mortality | Uncertain | PMID 40277510 |
| M2.20 | 48 development programmes in this record stopped before establishing a result. Their failure domain is the absence of an answer, not a negative answer: recruitment or operational failure (11), unknown reason (10), regulatory or commercial decision (9), safety or toxicity (7), stated futility (4) and trial design (3). | not applicable - no result reached | Unknown | ipf_phase2_negative_results_register.csv |

The distinction that matters most in this section is between the eleven Failed rows and the 48
stopped programmes. A null primary endpoint in an adequately sized trial is an answer. A programme
that stopped for recruitment failure, funding withdrawal or an unstated reason is not — and it is
not a positive signal either.

---

## 3. S3 — What is uncertain

Fourteen statements covering the 46 Uncertain interventions, the one Conflicting intervention, and
four disagreements carried unresolved from the conflicts register.

| ID | Statement | Outcome dimension | Tier | Source |
|---|---|---|---|---|
| M3.1 | Eight investigational agents have a positive randomised signal in IPF that has not been tested at phase 3: AP01 (inhaled pirfenidone), BMS-986020, GSK3008348, LTI-03, TRK-250, bexotegrast, omipalisib and taladegib. Each rests on one small randomised trial. | mostly rate of FVC decline (E1) or biomarker endpoints | Uncertain | PMID 36948586; PMID 30201408; PMID 32216814; PMID 42538332; PMID 37738329; PMID 38843105; PMID 30765508; PMID 41043447 |
| M3.2 | Deupirfenidone is positive on a 26-week FVC endpoint in one phase 2b trial (ELEVATE-IPF), including against an active pirfenidone arm; no phase 3 result exists. | rate of FVC decline (E1) | Probable | PMID 42085224 |
| M3.3 | Admilparant's phase 2 IPF-cohort estimate has a confidence interval that includes zero; the statistically significant estimate comes from the separate progressive pulmonary fibrosis cohort of the same trial and is indirect evidence for IPF under scope limit L1. | rate of FVC decline (E1) | Uncertain | PMID 39393084 |
| M3.4 | Rentosertib (INS018_055) reported an exploratory FVC increase at its highest dose in a phase 2a trial whose primary endpoint was tolerability. The efficacy signal is not a tested hypothesis. | rate of FVC decline (E1) - exploratory | Hypothesis | PMID 40461817 |
| M3.5 | Eight agents were null in IPF trials that were too small or too short for the null to be decisive: GLPG1205, azithromycin, cromolyn sodium (RVT-1601), etanercept, imatinib, inhaled carbon monoxide, macitentan and tralokinumab. These are unresolved, not refuted. | various; mostly FVC (E1) or progression composites | Uncertain | PMID 36328358; PMID 34015241; PMID 35050837; PMID 18669816; PMID 20007927; PMID 29100885; PMID 23682110; PMID 28787186 |
| M3.6 | Six repurposed approved drugs have IPF evidence that cannot carry a conclusion: omeprazole, salbutamol, sirolimus and valganciclovir have small positive randomised results; losartan has non-randomised evidence only; metformin has observational evidence that is null. | various | Uncertain | PMID 30610155; PMID 29409488; PMID 36853800; PMID 33740394; PMID 22810758; PMID 30025392 |
| M3.7 | Cell therapies and blood-derived biologics in IPF rest on non-randomised or very small randomised human evidence: mesenchymal stem cells, RegenD001, IW001, PBI-4050 and intravenous immunoglobulin. | safety and FVC (E1) | Uncertain | PMID 27890713; PMID 40036154; PMID 25614165; PMID 30578394; PMID 42164489 |
| M3.8 | Symptomatic and supportive interventions other than nalbuphine and rehabilitation are unresolved: low-dose morphine and thalidomide each rest on one very small short crossover trial in cough; supplemental oxygen shows acute exercise benefit without long-term IPF-specific evidence; palliative care, CPAP, neuromuscular electrical stimulation and inspiratory muscle training have small or indirect evidence. | symptoms (E8, E9), functional capacity (E5), HRQoL (E6) | Uncertain | PMID 38237620; PMID 22986377; PMID 32367694; PMID 34003726; PMID 25028171; PMID 34083348; PMID 39129185 |
| M3.9 | Seven named traditional-medicine interventions have randomised IPF-only trials that pass the prespecified screen (Jinbei oral liquid, Kangxian Huanji Granule, Qizhukangxian granules, Feiwei granules, umbilical moxibustion, Pulmonary Daoyin, Baduanjin exercise), and pooled syntheses of Chinese herbal medicine report benefit. Every such row is capped at Uncertain because risk of bias was only assessable from abstracts, samples are small, follow-up is short, and Chinese-language databases were not searched. Feiwei granules is author-reported null. | lung function, symptoms, exercise capacity - varies by trial | Uncertain | PMID 39849152; PMID 37993378; PMID 32744035; PMID 28459237; PMID 30942008; PMID 33164264; PMID 41184899; PMID 37235494 |
| M3.10 | Sildenafil is the one intervention in this record whose randomised IPF-only evidence points in two directions, with one positive and one null trial and no basis in the record for preferring either. | exercise capacity, symptoms | Uncertain | PMID 35452834 |
| M3.11 | Every 'works' verdict for a disease-directed drug in this record rests on FVC or a categorical FVC-based composite. Whether a treatment-induced change in FVC decline translates into longer survival is unresolved, and the record forbids grading a lung-function result on the survival dimension. | see conflicts register | Uncertain | Phase 1 ceiling table; PMID 34217681; PMID 28232409 |
| M3.12 | Whether corticosteroids increase mortality in IPF, and by how much, cannot be settled from the available evidence class: the excess-mortality signal comes from pooled predominantly observational data where confounding by indication cannot be excluded, and no randomised monotherapy trial exists. | see conflicts register | Uncertain | PMID 40277510; PMID 22607134 |
| M3.13 | Whether a genotype- or telomere-defined subgroup responds differently to N-acetylcysteine is unresolved. The PANTHER monotherapy arm was null overall; the subgroup findings are post hoc and do not lift that verdict. | see conflicts register | Hypothesis | PMID 24836309; PMID 30566847; NCT04300920 |
| M3.14 | Whether co-trimoxazole has any effect in a treatment-adherent subgroup is unresolved: the trial's per-protocol analysis disagreed with its null intention-to-treat result. | see conflicts register | Uncertain | see key_result_pmid 23143842 and conflict_note |

---

## 4. S4 — What we know about the disease

| ID | Statement | Outcome dimension | Tier | Source |
|---|---|---|---|---|
| M4.1 | IPF is a progressive fibrosing interstitial pneumonia of unknown cause, defined by a usual interstitial pneumonia pattern. | not applicable | Established | 2022 ATS/ERS/JRS/ALAT guideline, PMID 35486072 |
| M4.2 | Pooled global incidence is 5.8 per 100,000 (95% CI 4.8-6.8) and prevalence 17.7 per 100,000 (95% CI 14.0-21.5), with regional variation (North America 27.2, Europe 14.6, Asia 14.8). | not applicable | Established | PMID 40775309 |
| M4.3 | Registry cumulative mortality is 5%, 24%, 37% and 44% at years 1-4, and GAP stage III carries a hazard ratio of 4.64 versus stage I. | survival (E11) | Established | AIPFR, PMID 28232409 |
| M4.4 | Trial populations are not the disease population: 1- and 2-year mortality in modern trial cohorts (6.6%, 13.7%) is far below registry mortality (5%, 24%), which is why mortality endpoints are hard to power and why the randomised evidence base is concentrated in mild-to-moderate physiologic impairment. | survival (E11) | Established | PMID 24476390; PMID 28232409 |
| M4.5 | The frequently quoted median survival of about four years predates antifibrotic therapy (1998 data) and must not be presented as current prognosis. | survival (E11) | Established | PMID 9713446 |
| M4.6 | Acute exacerbation occurs in 18.6% of patients over three years and carries about 29.5% in-hospital mortality; no intervention in this record prevents or treats it with adequately powered randomised evidence. | acute exacerbation (E10) | Established | PMID 39256473; PMID 35614114 |
| M4.7 | Comorbidity drives outcome: pulmonary hypertension carries a mortality hazard ratio of 2.0 and lung cancer 2.6. | survival (E11) | Established | EMPIRE registry, PMID 30170904 |
| M4.8 | The best documented effect on the rate of FVC decline is a 130.1 mL 52-week between-group difference; the least-declining active arm in any IPF trial still declined (-21.5 mL over 26 weeks). No trial has documented recovery of lost lung function. | rate of FVC decline (E1), recovery (E15) | Established | ipf_phase1_ceiling.csv |
| M4.9 | Antifibrotic therapy is associated with a pooled acute-exacerbation risk ratio of 0.63 (95% CI 0.53-0.76, I2=0%), but the pooled sources are predominantly observational. | acute exacerbation (E10) | Uncertain | PMID 34217681 |
| M4.10 | Two interventions are conditionally recommended against for treating IPF by the current guideline: antacid medication and antireflux surgery. | disease course | Established | PMID 35486072 |

---

## 5. S5 — What we do not know

Twelve statements. Four of them (M5.7–M5.10) are facts about the completeness of this record rather
than about any intervention, and are kept in the map so that later phases cannot mistake a gap in
retrieval for a gap in biology.

| ID | Statement | Outcome dimension | Tier | Source |
|---|---|---|---|---|
| M5.1 | No intervention has been shown to recover lost lung function in IPF. | recovery (E15) | Unknown | ipf_phase1_ceiling.csv |
| M5.2 | Reversal of established fibrosis has never been demonstrated in IPF, and no human trial endpoint in this record measures it. | reversal (E15) | Unknown | ipf_phase1_ceiling.csv; ipf_phase1_endpoint_taxonomy.csv |
| M5.3 | No drug has randomised evidence of prolonging survival in IPF. The only survival evidence in this record is observational, for lung transplantation. | survival (E11) | Unknown | ipf_phase1_ceiling.csv; ipf_phase2_landscape.csv |
| M5.4 | Durability of antifibrotic effect beyond 52 weeks has never been established randomly; open-label extensions are not randomised comparisons. | durability (E12) | Unknown | ipf_phase1_ceiling.csv |
| M5.5 | No validated predictive biomarker identifies which patient benefits from which treatment in IPF; treatment-response heterogeneity is unexplained. | treatment-response heterogeneity | Unknown | ipf_phase2_conflicts_register.csv X7; ipf_phase1_unmet_needs.csv UN11 |
| M5.6 | Whether slowing FVC decline changes survival is unknown. This unresolved surrogacy question sits underneath every positive verdict in the record. | rate of FVC decline (E1) vs survival (E11) | Unknown | ipf_phase2_conflicts_register.csv X5 |
| M5.7 | Results of a large fraction of completed IPF trials cannot be found: of 149 completed interventional trials, 110 have no retrievable results and 97 of those are beyond the 12-month reporting window. This is a gap in the record, not evidence about the interventions. | not applicable | Established | ipf_phase1_retrievability_register.csv |
| M5.8 | 48 development programmes stopped before establishing a result, and for 10 of them no reason is stated anywhere in the retrieved record. | not applicable | Established | ipf_phase2_negative_results_register.csv |
| M5.9 | The Phase 2 per-entity search under-retrieves for agents whose registry label is a code name or a two-drug string: six of seventeen phase-3-labelled entities initially graded 'Poorly studied' in fact had published primary reports (corrections entry C11). The 208 remaining 'Poorly studied' rows are therefore an upper bound on genuine absence of evidence, not a count of it. | not applicable | Established | corrections_log.csv C11; ipf_phase3_retrieval_check.json |
| M5.10 | Chinese-language databases (CNKI, VIP, Wanfang, SinoMed) and Embase, CENTRAL, EU-CTR, jRCT and CTRI were not searched. Traditional-medicine and non-English evidence in this record is a floor, not a complete accounting. | not applicable | Unknown | ipf_phase2_search.json; ipf_phase2_conflicts_register.csv X8 |
| M5.11 | No adequately powered randomised evidence exists for preventing or treating acute exacerbation of IPF; the two randomised attempts in this record (thrombomodulin alfa, cyclophosphamide plus glucocorticoids) were null and harmful respectively. | acute exacerbation (E10) | Unknown | ipf_phase2_landscape.csv |
| M5.12 | Non-pharmacological and supportive-care evidence is largely ILD-wide rather than IPF-exclusive, so what works specifically in IPF is partly unknown. | functional capacity (E5), HRQoL (E6) | Unknown | ipf_phase1_standard_of_care.csv; ipf_phase2_landscape.csv |

---

## 6. S6 — What might be worth studying

Twelve candidate questions derived from S1–S5. **These are candidates, not Research Leads.** They
enter Phase 4 as the screening pool and most of them are expected not to survive.

| ID | Statement | Outcome dimension | Tier | Source |
|---|---|---|---|---|
| M6.1 | Interventions whose IPF trial stopped for recruitment, funding or operational reasons rather than for a result: azithromycin (recruitment targets not met), losartan (funding withdrawn), cromolyn sodium (recruitment and pandemic), continuous positive airway pressure (enrolment). The question these trials asked was never answered. | varies | Uncertain | ipf_phase2_landscape.csv (abandoned_reason in recruitment_or_operational, regulatory_or_commercial) |
| M6.2 | Underpowered nulls never retested at adequate size: GLPG1205, etanercept, imatinib, inhaled carbon monoxide, macitentan. Whether these represent absence of effect or absence of power is unresolved. | varies | Uncertain | ipf_phase2_landscape.csv (verdict_sublabel='null result that size or phase cannot make decisive') |
| M6.3 | Whether an N-acetylcysteine benefit exists in a genotype- or telomere-defined subgroup is a pre-existing hypothesis with existing datasets (PANTHER-IPF, PRECISIONS/NCT04300920) that could answer it without a new trial. | varies | Hypothesis | ipf_phase2_conflicts_register.csv X7; PMID 24836309; PMID 30566847; NCT04300920 |
| M6.4 | Whether the null co-trimoxazole result masks an adherence-dependent effect could be examined in the existing trial data (per-protocol vs intention-to-treat disagreement in EME-TIPAC; CleanUP-IPF individual data). | varies | Uncertain | ipf_phase2_conflicts_register.csv X1; PMID 23143842; PMID 33974018 |
| M6.5 | The sildenafil disagreement is the record's only unresolved within-intervention conflict in randomised IPF-only evidence, and is a candidate for individual-participant re-analysis rather than a new trial. | varies | Uncertain | ipf_phase2_conflicts_register.csv X4 |
| M6.6 | Whether treatment-induced change in FVC decline predicts survival is answerable by trial-level or individual-participant meta-analysis of existing IPF trials, and would change how every positive verdict in this record should be read. | varies | Unknown | ipf_phase2_conflicts_register.csv X5 |
| M6.7 | Retrieving the 110 completed IPF trials whose results are not retrievable, 97 of them past the reporting window, is the largest single addition available to this record. It is a retrieval task and carries no implication that the unretrieved results are positive. | varies | Established | ipf_phase1_retrievability_register.csv |
| M6.8 | For traditional-medicine interventions the smallest useful next step is closing the database gap (CNKI, VIP, Wanfang, SinoMed) and obtaining full texts for risk-of-bias assessment, before any question of efficacy is entertained. | varies | Uncertain | ipf_phase2_traditional_medicine_screen.csv; ipf_phase2_conflicts_register.csv X8 |
| M6.9 | Whether the short-term functional and quality-of-life gains from rehabilitation persist beyond about six months is unresolved and is a question about an intervention already in standard use. | varies | Uncertain | ipf_phase2_landscape.csv; ipf_phase1_standard_of_care.csv |
| M6.10 | The magnitude of corticosteroid-associated mortality in IPF, and whether it survives adjustment for confounding by indication, is examinable in existing registry cohorts. | varies | Uncertain | ipf_phase2_conflicts_register.csv X6; PMID 40277510 |
| M6.11 | Single positive small randomised signals with no adequately sized follow-up in this record: BMS-986020, GSK3008348, omipalisib, TRK-250, salbutamol, omeprazole, sirolimus and valganciclovir. Some were stopped for reasons other than efficacy (GSK3008348: 'sufficient information gathered'; bexotegrast: DSMB recommendation, a stop whose basis the record cannot determine). | varies | Uncertain | ipf_phase2_landscape.csv (positive randomised signal below phase 3) |
| M6.12 | No intervention in this record targets recovery of lost lung function or reversal of established fibrosis, and no trial endpoint measures them. Whether such an endpoint can be defined and measured is a prior question to any therapeutic candidate. | varies | Unknown | ipf_phase1_endpoint_taxonomy.csv; ipf_phase1_ceiling.csv |

---

## 7. Preserved distinctions

- **Outcome dimensions are not interchangeable.** Every S1–S3 statement names its dimension. The
  record contains no statement of the form "X treats IPF".
- **Evidence tiers are inherited, not recomputed.** A tier in the map equals the tier of the Phase 2
  row or Phase 1 fact it derives from.
- **Negative results are kept as results.** Failed, harm and stopped-without-result are three
  different things and occupy three different statement types.
- **Conflicts stay conflicts.** X1, X4, X5, X6, X7 and X8 are all in the map as unresolved.
- **Retrievability limits are in the map, not in a footnote** (M5.7–M5.10).
- **Indirect evidence is labelled.** PPF-wide and ILD-wide evidence enters only as indirect
  (M3.3, M5.12, and the nerandomilast label note in M1.3).

## 8. Limitations of this phase

The map contains no evidence that was not already in the Phase 0–2 record, except the six
reclassifications and the cough-ceiling update described in §0, all graded from abstracts with full
texts not read. Statements were assembled by hand from the Phase 2 tables; the per-intervention
spine was generated programmatically, and a coverage audit confirms every one of the 73 graded
interventions appears in at least one map statement. The 208 "Poorly studied" interventions are
represented collectively by M5.9 rather than individually.

## 9. Files produced by this phase

- `ipf_phase3_treatment_map.csv` — 75 statements across six sections
- `ipf_phase3_map_spine.csv` — 73 graded interventions mapped to statement IDs
- `ipf_phase3_retrieval_check.json` — searches and outcomes of the C11 retrieval-artefact check
- `fig5_ipf_phase3_map.png` — statements by section and evidence tier
- re-issued: `ipf_phase2_landscape.csv`, `ipf_phase2_negative_results_register.csv`,
  `ipf_phase1_ceiling.csv`, `corrections_log.csv` (through C11)
