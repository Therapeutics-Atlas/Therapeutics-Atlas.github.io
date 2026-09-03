# Phase 4 — Research Lead Identification: Idiopathic Pulmonary Fibrosis

Open Therapeutics / Open Evidence Record. Date: 2026-09-03. Scope: `IPF_SCOPE.md` (locked, unchanged).
Prespecified method: `IPF_PHASE4_BRIEF.md` (written before any screening).
Input: the Phase 3 Open Treatment Map (75 statements at input, 78 after Phase 4 additions).

## Headline result

**No research lead survived Phase 4.** All 33 candidates decomposed from the map's
12 "what might be worth studying" statements were rejected or held. Two are held at
verification and explicitly not promoted. Nine actions — retrieval, re-analysis and
measurement — are carried to Phase 6 as record work, not as therapeutic hypotheses.

Twelve corrections (C12–C23) were required to the Phase 2 landscape and the Phase 3 map.
Eleven of them are retrieval artefacts of the Phase 2 search strategy rather than changes
of judgement about the same evidence. Phase 4 therefore changed the record more by
correcting it than by extending it.

The single most consequential finding of Phase 4 is not a lead but a harm: bexotegrast,
which the record had carried as a small positive signal, was tested in an adequately sized
randomised phase 2b that was terminated on Data Safety Monitoring Board recommendation with
**more disease progression and more deaths on active treatment** (C23). That result existed
only as a ClinicalTrials.gov results posting and was invisible to a PubMed-only search.

## Method as prespecified

The pool was fixed before screening: every intervention and question named in map section S6
was decomposed into one candidate per intervention or per distinct question, giving 33 candidates.
No candidate was admitted from outside the map. Each was screened against six disqualifiers:

| Screen | Disqualifier |
|---|---|
| S1 | retrieval artefact — the question already had an answer the earlier record missed |
| S2 | superseded — a later or larger result, or the programme's own posted result, replaces the signal |
| S3 | already being answered — a registered ongoing trial addresses the same question |
| S4 | no testable signal — no controlled human signal, a non-clinical primary endpoint, or an effect not separable from an already-graded intervention |
| S5 | verification incomplete — the key result could not be checked against primary full text |
| S6 | not a therapeutic lead — a record, analysis or measurement action rather than an intervention hypothesis |

Hard stops that were honoured: no efficacy grading was performed in Phase 4; no Phase 2 verdict
was revised because a candidate looked appealing, only because a source was found or read; no
estimates were pooled; no gap in the record was converted into a therapeutic hypothesis; and a
candidate whose key result could not be verified against primary full text was recorded as
verification-incomplete and **not** promoted (S5, two candidates).

![Phase 4 screening outcome: none of the 33 candidates survived, and 17 of them failed because no controlled human signal remained to test]({{artifact:18f55e5f-5789-42d8-8f21-0f66d917248c}})

## Screening result

| cand_id | subject | shape | outcome | screen_failed |
|---|---|---|---|---|
| P1 | azithromycin | (d) abandoned rather than refuted | rejected | S1; S4 |
| P2 | losartan | (d) abandoned rather than refuted | rejected | S4 |
| P3 | cromolyn sodium (RVT-1601) | (d) abandoned rather than refuted | rejected | S2 |
| P4 | continuous positive airway pressure | (d) abandoned rather than refuted | rejected | S4 |
| P5 | GLPG1205 | (a) unreplicated null that size or phase cannot make decisive | rejected | S4 |
| P6 | etanercept | (a) unreplicated null that size or phase cannot make decisive | rejected | S4 |
| P7 | imatinib | (a) unreplicated null that size or phase cannot make decisive | rejected | S4 |
| P8 | inhaled carbon monoxide | (a) unreplicated null that size or phase cannot make decisive | rejected | S4 |
| P9 | macitentan | (a) unreplicated null that size or phase cannot make decisive | rejected | S4 |
| P10 | n-acetylcysteine in a TOLLIP- or telomere-defined subgroup | (c) subgroup that may respond differently | held at verification - not promoted | S5 |
| P11 | co-trimoxazole adherence-dependent effect | (b) analysis of existing trial data | rejected as a lead; analysis action retained | S2; S6 |
| P12 | sildenafil in right-heart dysfunction | (c) subgroup that may respond differently | rejected | S2; S1 |
| P13 | BMS-986020 / LPA1 pathway | (d) abandoned rather than refuted (toxicity) | rejected | S3 |
| P14 | FVC change as a surrogate for survival | (e) record-level analysis opportunity | rejected as a lead; analysis action retained | S6 |
| P15 | 110 completed trials with unretrievable results | (e) record-level retrieval opportunity | rejected as a lead; retrieval action retained | S6 |
| P16 | Jinbei oral liquid | (f) traditional-medicine signal | rejected | S4 |
| P17 | Kangxian Huanji granule | (f) traditional-medicine signal | held at verification - not promoted | S5 |
| P18 | Baduanjin exercise | (f) traditional-medicine signal | rejected | S4 |
| P19 | Chinese-language database gap | (e) record-level retrieval opportunity | rejected as a lead; retrieval action retained | S6 |
| P20 | corticosteroid harm magnitude | (e) record-level analysis opportunity | rejected as a lead; analysis action retained | S6 |
| P21 | recovery and reversal endpoints | (e) measurement gap | rejected as a lead; measurement action retained | S6 |
| P22 | pulmonary rehabilitation durability | (g) open question about an intervention that works | rejected | S1 |
| P23 | omeprazole | (a) small positive randomised signal | rejected | S4 |
| P24 | GSK3008348 | (a) small positive randomised signal | rejected | S4 |
| P25 | LTI-03 | (a) small positive randomised signal | rejected | S3; S4 |
| P26 | TRK-250 | (a) small positive randomised signal | rejected | S4 |
| P27 | bexotegrast (PLN-74809) | (a) small positive randomised signal | rejected | S2 |
| P28 | omipalisib | (a) small positive randomised signal | rejected | S4 |
| P29 | salbutamol | (a) small positive randomised signal | rejected | S4 |
| P30 | sirolimus | (a) small positive randomised signal | rejected | S4 |
| P31 | valganciclovir | (a) small positive randomised signal | rejected | S4 |
| P32 | palliative care | (a) small positive randomised signal | rejected | S4 |
| P33 | mesenchymal stem cells | (a) small positive randomised signal | rejected | S3; S4 |

Per-candidate reasoning is in `ipf_phase4_candidate_register.csv` (column `reason`), which also
carries the screen definitions for each row.

## Held at verification — not promoted

Two candidates are neither rejected nor promoted, because the Phase 4 brief forbids promoting a
key result that has not been read in primary full text:

- **P10 — N-acetylcysteine in a TOLLIP- or telomere-defined subgroup.** The motivating post hoc
  interaction analysis (PMID 26331942) is closed access and could not be obtained. Independently,
  the genotype-stratified phase 3 trial PRECISIONS (NCT04300920) has completed with no results
  posted. The question is already being answered; the smallest next step is retrieval.
- **P17 — Kangxian Huanji granule.** Abstract reports treatment failure at 4 weeks
  (RR 0.22, 95% CI 0.051–0.965, P=0.023) with no significant 16-week mortality difference, but the
  full text could not be obtained through any available route.

Neither is evidence of efficacy and neither is a lead. Both are retrieval actions.

## Corrections made in Phase 4

| id | claim_corrected | correction | basis | effect |
|---|---|---|---|---|
| C12 | Phase 2 and map statement M6.9 held that no randomised trial had tested whether pulmonary rehabilitation gains persist beyond 3-6 months, and rated durability an open question. | A 52-week randomised trial of exercise training on background antifibrotic therapy (PMID 37012071) exists and was missed. It is null on 6MWD ('mean difference, 21 m (95% CI -25 to 66), p=0.38') and favours training on endurance time ('mean difference, 187 s (95% CI 34 to 153), p=0.019'). The untested horizon is now beyond 12 months, not beyond 6 months. | Phase 4 screen-1 search (rehabilitation synonyms) 2026-09-03; abstract read. The endurance-time interval as printed does not contain its own point estimate; reproduced verbatim and flagged as an apparent source typographical error - full text not obtained. | Landscape curation note and M1.6 amended; candidate P22 (durability) rejected as already answered. |
| C13 | Phase 2 held a smaller co-trimoxazole trial as the key result and carried an unresolved intention-to-treat versus per-protocol conflict (X1). | The adequately powered EME-TIPAC trial (n=342, PMID 33289822) was missed. Its primary time-to-event composite is null ('hazard ratio of 1.2 ([95% CI, 0.9-1.6]; P = .32)'). X1 is resolved by supersession; the adherence question survives only as a re-analysis action. | Phase 4 screen-1 search (co-trimoxazole/trimethoprim synonyms) 2026-09-03; abstract read. | Landscape key result, negative-results register and M2.3 updated; X1 status changed; candidate P11 rejected as superseded, re-analysis carried to Phase 6. |
| C14 | Phase 2 and Phase 3 recorded sildenafil as the record's only genuinely conflicting intervention (X4) and listed a right-heart-dysfunction subgroup as an open question (M6.5). | Two randomised sources were missed: a phase 2b trial adding sildenafil to pirfenidone in advanced IPF at risk of group 3 pulmonary hypertension, null on its primary endpoint ('between-group difference 3·06% [95% CI -11·30 to 17·97]; p=0·65'), and a prespecified INSTAGE subgroup analysis ('There was no heterogeneity between subgroups by presence of RHD in the effect of nintedanib plus sildenafil versus nintedanib alone on change in SGRQ total score at Week 12 (P = 0.74) or Week 24 (P = 0.90), or change in FVC at Week 12 (P = 0.58) or Week 24 (P = 0.55)'). Sildenafil is reclassified Failed in the overall population and the subgroup hypothesis is recorded as tested and not supported. The trialists' own residual sentence ('further research is required to establish if specific subgroups of patients with IPF might benefit from sildenafil') is preserved as an open statement not backed by a positive subgroup result. | Phase 4 screen-1 search (sildenafil synonyms) 2026-09-03; both abstracts read. | Landscape verdict changed Conflicting->Failed; X4 resolved; new map statement M2.13; M3.10 and M6.5 superseded; candidate P12 rejected. |
| C15 | Phase 2 graded cromolyn sodium (RVT-1601) as a programme stopped before a result and listed it as abandoned rather than refuted (M6.1, M3.5). | A phase 2a trial of the same inhaled formulation was positive on cough (PMID 28923239) and a larger phase 2b dose-ranging trial was null ('did not provide benefit over placebo for the treatment of chronic cough in patients with IPF'). The programme was superseded by its own null result, not abandoned before one. | Phase 4 screen-2 search (cromolyn/RVT-1601 synonyms) 2026-09-03; abstracts read. | Landscape verdict changed to Failed; negative-results register row reclassified; new map statement M2.14; removed from M3.5 and M6.1; candidate P3 rejected as superseded. |
| C16 | Phase 2 labelled ten interventions 'positive randomised signal below phase 3', and M6.11 listed them as positive signals awaiting adequately sized follow-up. | For GSK3008348, LTI-03, TRK-250, bexotegrast, omipalisib, salbutamol, sirolimus, valganciclovir, palliative care and mesenchymal stem cells the trial's own primary endpoint was safety, tolerability, pharmacokinetics, lung deposition, feasibility or a mechanistic marker, not a clinical outcome. Sub-labels rewritten; M6.11 rewritten to state that only BMS-986020 has a positive clinical-endpoint result among these. | Audit of each row against its own recorded primary-endpoint field, Phase 4 2026-09-03; for sirolimus the abstract states 'Lung function was unaffected by either treatment'. | Ten landscape sub-labels corrected; M6.11 and M3.6 rewritten; candidates P24-P33 rejected for absence of a clinical signal to test. |
| C17 | Phase 2 recorded omeprazole as a positive randomised signal below phase 3 on cough. | Full text verified: primary objectives were feasibility and acceptability with no formal sample-size calculation; the adjusted cough-frequency difference was 39.1% lower (95% CI 66.0% lower to 9.3% higher), i.e. including no effect; and in the same trial FEV1 -0.12 L (95% CI -0.25 to -0.002), -7.4% predicted (-14.6 to -0.2) and FVC -0.11 L (-0.21 to -0.02) favoured placebo, with lower respiratory tract infection in 6 of 23 versus 3 of 22. | Full text of the pilot trial (doi 10.1136/thoraxjnl-2018-212102) obtained and read, Phase 4 2026-09-03. | Landscape sub-label and tier corrected; M3.6 and M6.11 amended; candidate P23 rejected - verification weakened rather than supported it. |
| C18 | Phase 2 recorded BMS-986020's abandonment reason as not_applicable. | The trial was terminated for drug-related hepatobiliary toxicity: 'The study was terminated early because of three cases of cholecystitis that were determined to be related to BMS-986020'. Reason changed to safety_or_toxicity and a harm-domain row added to the negative-results register. | Abstract of the phase 2 trial (PMID 30201408) read in Phase 4 2026-09-03. | Landscape and negative-results register updated; M6.11 rewritten; candidate P13 rejected as already being answered by the phase 3 successor programme in the same pathway. |
| C19 | Conflicts register X7 cited PMID 30566847 (telomere length and immunosuppression) as the source of the N-acetylcysteine subgroup hypothesis. | The primary source is the TOLLIP rs3750920 x N-acetylcysteine interaction analysis of PANTHER-IPF (PMID 26331942): 'NAC therapy was associated with a significant reduction in composite endpoint risk (hazard ratio, 0.14; 95% confidence interval, 0.02-0.83; P = 0.03) in those with a TT genotype'. Both papers are retained as distinct subgroup hypotheses. | Targeted search and record check, Phase 4 2026-09-03. The full text of PMID 26331942 could not be obtained (abstract-level only). | X7 provenance corrected; candidate P10 held at verification and not promoted. |
| C20 | Phase 2 recorded the Jinbei oral liquid trial as a randomised trial with a positive effect on total lung capacity. | Full text verified: 'No primary endpoint was predefined in the clinical trial.' The only significant endpoint among many was total lung capacity, multiplicity uncontrolled, while FVC % predicted, DLco % predicted, 6MWD, SGRQ and PaO2 were not significant. | Full text (doi 10.1038/s41598-025-87474-x) obtained and read, Phase 4 2026-09-03. | Traditional-medicine screen annotated with full-text verification; candidate rejected - no predefined primary endpoint and no accepted IPF efficacy endpoint met. |
| C21 | Phase 2 recorded the Baduanjin trial's design as narrative_review_or_mechanistic with n=28 and duration unstated. | Full text verified: it is a randomised trial, n=28, 8 weeks, unblinded, allocation by opened envelopes, control group received no training, powered only for the 6MWT and described by the authors as exploratory. | Full text (doi 10.1186/s13030-025-00346-8) obtained and read, Phase 4 2026-09-03. | Design, sample-size and duration fields corrected; candidate rejected - the no-exercise comparator cannot separate a Baduanjin-specific effect from the generic effect of exercise training already graded at Probable. |
| C22 | Phase 2 recorded azithromycin's abandonment reason as recruitment_or_operational alongside a null cough result, and M6.1 listed it as abandoned rather than refuted. | The two facts belong to different trials: the null cough result is a completed double-blind randomised crossover trial (NCT02173145, PMID 34015241, 'This randomized controlled trial does not support the use of low-dose azithromycin for chronic cough in patients with IPF'), while the terminated trial was a combination-therapy study (NCT01432080, n=12). The cough question has a randomised answer. | Registry rows for NCT02173145, NCT01432080 and NCT05842681 read from the Phase 0 registry extract, Phase 4 2026-09-03. | Landscape curation note and M6.1 amended; candidate P1 rejected - the abandoned trial is not the source of the signal, and the ongoing large trial NCT05842681 addresses acute exacerbation, a different question. |
| C23 | Phase 2 graded bexotegrast as a positive randomised signal below phase 3 (later corrected in C16 to a non-clinical primary endpoint) and Phase 3 listed it among small programmes awaiting adequately sized follow-up (M6.11). | Bexotegrast is reclassified as 'Harm outweighs benefit'. In BEACON-IPF (NCT06097260, n=319 randomised), terminated on DSMB recommendation, registry-posted results show more disease-progression events on bexotegrast than placebo: 5 of 106 (placebo), 16 of 105 (160 mg) and 25 of 108 (320 mg); Cox hazard ratios versus placebo 3.31 (95% CI 1.21-9.05, p=0.0194) and 5.36 (95% CI 2.05-13.99, p=0.0006). A >=10% absolute FVC decline was also more frequent (odds ratio 3.33, 95% CI 1.03-10.81, p=0.0449 for 160 mg; 3.01, 95% CI 0.91-9.91, p=0.07 for 320 mg). Deaths: 0 of 106, 6 of 105 and 4 of 108; serious adverse events 6, 17 and 21. The week-52 FVC primary endpoint is uninformative because only 1, 1 and 2 participants reached week 52 after early termination. | ClinicalTrials.gov results section for NCT06097260, retrieved 2026-09-03. The Phase 2 search used PubMed only and no peer-reviewed publication of these results was identified, so a registry-results check was required to find them. | Landscape verdict changed Uncertain->Harm outweighs benefit; negative-results register row reclassified to the harm domain; new map statement M2.15; bexotegrast removed from M6.11; candidate P27 rejected as superseded by its own trial. Adds a methodological limitation to Phase 2: PubMed-only searching misses registry-posted results. |

## Effect on the landscape

Verdict distribution before Phase 4 → after:
Works 7 → 7, Failed 11 → 13,
Harm outweighs benefit 8 → 9,
Uncertain 46 → 44,
Poorly studied 208 → 208. The one intervention Phase 3 graded 'Conflicting' (sildenafil) is reclassified, so the record now holds no intervention in that class.

Two statements were added to the map's "what does not work" section (M2.13 sildenafil, M2.14
cromolyn sodium) and one to the harm evidence within it (M2.15 bexotegrast). Fourteen existing
statements carry a `phase4_status` field recording amendment, supersession, resolution or answer.
The conflicts register drops from 3 unresolved within-intervention conflicts to 1 unresolved
(X1 and X4 resolved); the sildenafil disagreement that Phase 3 called the record's only
unresolved within-intervention conflict is closed.

## Actions carried to Phase 6 (not executed here)

| action_id | type | subject | detail | from_candidate |
|---|---|---|---|---|
| A1 | retrieval | PRECISIONS (NCT04300920) | Genotype-stratified phase 3 of N-acetylcysteine in TOLLIP rs3750920 TT patients; primary completion 2026-03-02, no results posted at 2026-09-03. Request or await results; this is the direct test of the record's only surviving subgroup hypothesis. | P10 |
| A2 | retrieval | closed-access key results | Full text of PMID 26331942 (TOLLIP x N-acetylcysteine interaction) and of the Kangxian Huanji granule trial (PMID 37993378) could not be obtained. Both are marked verification-incomplete and neither can be promoted until read. | P10; P17 |
| A3 | retrieval | 110 completed trials without retrievable results | 97 of them past the reporting window. Largest single addition available to this record. Not evidence of promise. | P15 |
| A4 | retrieval | Chinese-language databases | CNKI, VIP, Wanfang and SinoMed were not searchable from this environment; the traditional-medicine screen therefore rests on English-indexed records only. | P19 |
| A5 | retrieval | registry-results sweep of the full landscape | NEW Phase 4 finding: the Phase 2 search used PubMed only, and the bexotegrast harm result (C23) existed solely as a ClinicalTrials.gov results posting. A results-section check was run in Phase 4 for the 22 candidate subjects only; the remaining landscape entities have not been checked for posted-but-unpublished results. | C23 |
| A6 | analysis of existing data | co-trimoxazole adherence | Adherence-stratified re-analysis of EME-TIPAC, acknowledging confounding by health status in open-label per-protocol comparisons. | P11 |
| A7 | analysis of existing data | corticosteroid harm magnitude | Quantify mortality association in existing cohorts with explicit handling of confounding by indication. | P20 |
| A8 | analysis of existing data | FVC-to-survival surrogacy | Trial-level or individual-participant meta-analysis; begin with a check of whether published meta-analyses already answer it. | P14 |
| A9 | measurement development | recovery and reversal endpoints | No endpoint in the record measures recovery of lost lung function or reversal of established fibrosis. | P21 |

## Limitations of Phase 4

| limitation_id | scope | detail |
|---|---|---|
| L1 | Phase 2 search strategy | PubMed-only searching missed a randomised trial (C12), an adequately powered trial (C13), two sildenafil sources (C14), a phase 2b null (C15) and a registry-only harm result (C23). Eleven of the twelve Phase 4 corrections are retrieval artefacts of the Phase 2 search, not changes of judgement about the same evidence. |
| L2 | Phase 4 screening | The registry-results check was run for the 22 candidate subjects, not for all 281 landscape entities (action A5). |
| L3 | full-text verification | Two candidate key results could not be verified against primary full text (P10, P17) and are recorded as held, not rejected and not promoted. |
| L4 | quantitative synthesis | No pooling or re-estimation was performed in Phase 4; all figures are quoted from their source reports. |
| L5 | one source with an internal inconsistency | The endurance-time interval in PMID 37012071 as printed does not contain its own point estimate; reproduced verbatim and flagged, full text not obtained. |

## Interpretation

A completed screen with zero surviving leads is the outcome the brief anticipated as acceptable.
It is worth stating what it does and does not mean.

It does not mean that IPF has no unexplored therapeutic space. It means that the space this record
had labelled "might be worth studying" turned out, on inspection, to consist mostly of questions
that already have answers (17 candidates had no controlled human signal to test; 4 were superseded;
3 are under test in registered trials; 2 had answers the earlier search missed) and of record work
that no amount of reasoning can substitute for: results that were never reported, full texts that
cannot be read, and databases that could not be searched.

The clearest signal from Phase 4 is methodological. A PubMed-only landscape search missed a
52-week randomised rehabilitation trial, an adequately powered antibiotic trial, two sildenafil
sources, a phase 2b cough trial, and a registry-only harm result in which patients on active
treatment progressed and died more often than patients on placebo. Before any future phase treats
this record as a map of what is known, the registry-results sweep in action A5 should be completed
across all landscape entities.

## Files

- `ipf_phase4_candidate_register.csv` — 33 candidates, shapes, outcomes, screens failed, per-candidate reasoning
- `ipf_phase4_actions.csv` — 9 actions carried to Phase 6
- `ipf_phase4_limitations.csv` — Phase 4 limitations
- `corrections_log.csv` — corrections C1–C23 (C12–C23 added in Phase 4)
- `ipf_phase2_landscape.csv` — landscape with Phase 4 corrections applied
- `ipf_phase2_negative_results_register.csv` — reclassified rows, bexotegrast harm row added
- `ipf_phase2_conflicts_register.csv` — X1 and X4 resolved, X7 provenance corrected
- `ipf_phase2_traditional_medicine_screen.csv` — full-text verification columns added
- `ipf_phase3_treatment_map.csv` — 3 statements added, 14 carrying `phase4_status`
- `fig6_ipf_phase4_screening.png` — screening outcome by disqualifier
