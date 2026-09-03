> **Archived phase report — a dated record of what was believed at the time, not the current state of the project.**
> Statements superseded by later verification are listed in `data/corrections_log.csv`. Check that log before citing anything in this file.
> Current lead status is in `data/research_leads_status.csv`.

# Open Therapeutics #001 — Rheumatoid Arthritis
## Phase 2: Comprehensive Treatment Landscape

**Date:** 2026-08-31
**Scope:** All treatment traditions — modern, experimental, repurposed, historical, natural
products, Traditional Chinese Medicine, acupuncture and other non-herbal TCM, lifestyle.
**Deliberately excluded from this document:** any Research Lead, ranking, recommendation, or
conclusion about what should be pursued. Phase 2 maps the terrain; it does not choose a route.

---

## 0. What this document is, and how it was built

This is a landscape survey of 67 interventions with a documented human evidence base in RA,
drawn from a structured PubMed sweep across thirteen intervention domains. Each intervention is
placed in one of seven verdict classes and linked to the specific unmet need from Phase 1 that
it would address if it worked.

**Retrieval.** Queries were issued in two-part keys (domain × concept) so that the provenance of
every record survived into analysis. Records were scored by study design inferred from title,
abstract and MeSH terms, by journal tier and by recency, with a penalty applied to animal-only
and in-vitro work; the best-designed records per query key were retained so that thin domains
(devices, helminths, faecal transplant) were not crowded out by dense ones (biologics). Two
further rounds targeted named interventions rather than concepts, to close gaps the concept
sweep left open.

**Extraction.** Structured fields — intervention, comparator, population, design, sample size,
the single most important numeric result copied verbatim, direction, outcome, author-stated
certainty and the author-stated main caveat — were extracted on a fixed schema and then checked
mechanically by searching each verbatim numeric result back in its source abstract. The
remainder were read directly from source abstracts.

**Important limitation stated up front:** this review is abstract-level. Full texts were not
retrieved. Numbers quoted here are as reported in abstracts and should be re-verified against
full texts before any of them is used to support a decision.

### Verdict classes used

| Class | Meaning |
|---|---|
| **Works** | Replicated benefit in humans, currently used or currently supported |
| **Works — abandoned anyway** | Positive human evidence exists, but the intervention left practice for reasons other than lack of effect (toxicity, cost, displacement, commercial decision) |
| **Conflicting** | Credible sources disagree; the disagreement is preserved rather than resolved |
| **Uncertain** | Positive signal, but the evidence base cannot bear the weight (small trials, no control, no blinding, surrogate outcome, or author-declared low certainty) |
| **Failed** | Adequately tested against a fair comparator and did not show benefit |
| **Harm outweighs benefit** | Effect is real but the safety record makes it indefensible |
| **Poorly studied** | Plausible and unevaluated — the absence of evidence is not evidence of absence |

### Phase 1 unmet-need codes

| Code | Unmet need |
|---|---|
| UN1 | Achieving remission beyond first-line therapy / refractory inflammatory disease |
| UN2 | Pain, fatigue and residual symptoms despite controlled inflammation |
| UN3 | Sustained drug-free remission |
| UN4 | Predicting which patient responds to which drug |
| UN5 | Prevention in at-risk individuals |
| UN6 | Reducing treatment toxicity and comorbidity burden |
| UN7 | ACPA-negative and other subgroup-specific disease |
| UN8 | Repair of existing structural damage |

---

## 1. The landscape at a glance

!Phase 2 treatment landscape: verdict composition by domain, and coverage of Phase 1 unmet needs

Three observations follow directly from the figure and are the organising facts of this phase.

**Uncertain is the largest class, not Works.** Of 67 interventions, 21 sit in *Uncertain* and
only 14 in *Works*. A further 8 are in *Works — abandoned anyway*: interventions with positive
human data that left practice for reasons other than failure.

**Effort is concentrated on one unmet need.** 41 of the 67 interventions address UN1 —
getting more patients into remission with anti-inflammatory therapy. Everything else is thin.

**One unmet need has no candidate at all.** UN4 — predicting which patient will respond to
which drug — has zero entries in every tradition surveyed, modern included. This is the single
most striking structural gap in the landscape: it is not that the candidates are weak, it is
that there are none. Phase 1 identified this as an open question; Phase 2 shows it is also an
empty intervention space. (This is a finding about the retrieved corpus, not proof that no work
exists; predictive-biomarker research is a research activity rather than an intervention, and
was not the target of this intervention-focused sweep.)

---

## 2. Modern medicine — the established core

The anchor drugs are the only part of the landscape where several interventions have
replicated, adequately controlled benefit.

| Intervention | Evidence | Key result | Verdict |
|---|---|---|---|
| Methotrexate monotherapy | Cochrane, 7 RCTs, 732 pts | ACR50 RR 3.0 (1.5–6.0) at 52 wk | Works |
| Sulfasalazine | Cochrane, 6 RCTs, 468 pts | SMD −0.49 joints, −0.42 pain; ESR −17.6 mm; withdrawals for adverse reactions OR 3.0 | Works |
| Hydroxychloroquine | Cochrane, 4 RCTs, 300 pts | SMDs −0.33 to −0.52 | Works (weakly) |
| Triple therapy vs MTX+etanercept | RCT (RACAT/TEAR) | 78% vs 63% still on assigned therapy at 1 yr | Works |
| Switching after b/tsDMARD failure | Cochrane living NMA, 19 RCTs, 4779 pts | Untried TNFi ACR50 OR 6.04 (2.49–16.3); moderate-to-high certainty also for IL-6 inhibitors, abatacept, rituximab, JAK inhibitors | Works |
| Low-dose prednisolone 5 mg, 2 yr (GLORIA) | RCT, 451 pts aged 65+ | DAS28 0.37 lower (p<0.0001) and damage 1.7 points lower (p=0.003); **and** harm 60% vs 49%, adjusted RR 1.24 (p=0.02) | Benefit and harm both real |

Two points deserve emphasis because they are easy to lose.

**GLORIA is not a positive trial or a negative trial.** It met both a benefit endpoint and a
harm endpoint. The largest harm contrast was in mostly non-severe infections. It is a
quantified trade-off, and reporting it as either "steroids work" or "steroids are harmful"
misrepresents it.

**The Cochrane network meta-analysis establishes that switching works on average and gives no
rule for choosing.** It confirms that after a biologic fails, several different next options all
beat placebo — which is precisely why UN4 matters. The evidence supports *a* switch; it does not
support *which* switch.

---

## 3. Modern medicine — failed, stalled, or abandoned

This section is preserved in full because negative and abandoned results are the part of the
landscape most often deleted from reviews.

**Anakinra (IL-1 receptor antagonist)** — Cochrane, 5 RCTs, 2876 patients: ACR20 38% vs 23%
(15 percentage points absolute), ACR50 18% vs 7%, ACR70 7% vs 2%. Injection-site reactions 71%
vs 28%; serious infections 1.8% vs 0.6% (not statistically different). The drug works. It was
displaced because it works less well than TNF inhibitors, not because IL-1 is irrelevant in RA.

**IL-17 inhibitors** — pooled ACR20 RR 1.67 (1.40–2.00) in TNF-inadequate responders across 10
studies; a separate pooling gives ACR20 OR 2.47 (1.29–4.72). The class is established in
psoriatic arthritis and axial spondyloarthritis but did not enter RA practice. *Our search did
not retrieve a source documenting why*, so the reason is not established here. This is recorded
as a conflict between the pooled efficacy literature and clinical reality, not as a resolved
story.

**Sirukumab (anti-IL-6)** — ACR20 40% vs 24% placebo in one phase 3 trial, 53.5% and 54.8% vs
placebo in another. Positive phase 3 efficacy; not licensed. Again, the regulatory reasoning was
not retrieved.

**Ocrelizumab (anti-CD20)** — DAS28 response RR 3.77 (2.47–5.74) across 4 RCTs, 2230+ patients.
Development in RA stopped; the same molecule later succeeded in multiple sclerosis. Abandonment
here reflects risk-benefit context, not target invalidity.

**p38 MAPK inhibitors** — early ACR20 signal that did not sustain across outcomes; no drug
emerged. A reference case for mechanism-to-drug attrition in RA.

**Fostamatinib (Syk inhibitor)** — borderline ACR20, clearer ACR50/ACR70, halted on the
efficacy-versus-toxicity balance.

**Denosumab** — erosion healing 20% vs 6% at 24 months (p=0.045) with no effect on inflammation.
It is the only intervention in the whole survey that addresses UN8 (damage repair) directly, and
it is not a DMARD substitute.

The pattern across this section: **positive efficacy data are not sufficient for an intervention
to survive.** At least four agents here have credible positive human trials and are not
available for RA. Any Phase 3 search for overlooked treatments should treat "abandoned" as an
independent variable from "ineffective".

---

## 4. Modern medicine — experimental and emerging

**Vagus nerve neuromodulation** is the most developed experimental line and the only one with a
pivotal sham-controlled trial. RESET-RA randomised 242 patients with inadequate response or
intolerance to b/tsDMARDs: ACR20 at 3 months 35.2% (active) vs 24.2% (sham), P=0.0209; open-label
response 50.0% at 6 months and 52.8% at 12 months; related serious adverse events 1.6%, all
perioperative and resolved. The effect size against sham is 11 percentage points — real, and
modest. The open-label figures are not controlled comparisons and should not be read as the
treatment effect.

The mechanistic predecessor (implanted VNS, open-label) showed inhibition of whole-blood TNF
production for up to 84 days with significant clinical improvement. A **transcutaneous**
(non-invasive) pilot in 16 high-activity patients showed DAS28-CRP 4.1→3.8 (p=0.02) over four
days, with no effect in a low-activity cohort — an open-label study far too small to interpret,
and a route to the same mechanism that has never been sham-tested in RA.

**Immune reset approaches.** A CD19×CD3 bispecific T-cell engager given on compassionate use to
6 patients with multidrug-resistant RA produced rapid decline in disease activity in all six,
with activated memory B cells replaced by IgD+ naive B cells and no clinically relevant
cytokine-release syndrome. n=6, uncontrolled.

**Autologous HSCT** achieved ≥ACR50 at some point in 49/76 (67%) patients with severe refractory
RA. It was largely abandoned in RA when biologics arrived, without a head-to-head comparison.

**Mesenchymal stem cells** — 64 patients, uncontrolled, DAS28 and HAQ lower at 1 and 3 years
versus pretreatment. There is no control group, patients remained on DMARDs, and pooled MSC
safety across autoimmune indications gives an adverse-event RR of 2.35 (0.58–9.58). The claim
that cannot be made from this design is a causal one.

**Regulatory T-cell therapy and low-dose IL-2** — reviews only. No controlled RA efficacy trial
was retrieved. These are the approaches most directly aimed at UN3 (drug-free remission) and
they have the thinnest RA clinical evidence base of any modern strategy in this survey.

---

## 5. Historical and abandoned treatments

Several older treatments have positive controlled evidence and were abandoned for reasons that
are documented and defensible — but the reasons vary, and the distinction matters.

**Abandoned because superseded:** auranofin (tender joints SMD −0.39, −0.54 to −0.25) is
genuinely active but slower and weaker than methotrexate.

**Abandoned because of toxicity:** D-penicillamine (SMD −0.51, −0.88 to −0.14) for proteinuria,
cytopenias and drug-induced autoimmunity; oral cyclophosphamide (SMD −0.57 and −0.59) for
malignancy and gonadal toxicity; ciclosporin constrained by a mean blood-pressure rise of
5 mmHg even at 1–4 mg/kg/day.

**Abandoned despite a positive sham-controlled result:** the Prosorba staphylococcal protein A
immunoadsorption column randomised 99 patients with mean 15.4 years' disease and more than five
prior DMARDs, and produced ACR responses in 28.9% versus 10.6% on sham (p=0.005; 41.7% vs 15.6%
among completers). This is a sham-controlled positive result in a refractory population, and the
column left practice on grounds of cost and practicality as biologics arrived. It is the
clearest "abandoned despite positive evidence" case found in this survey.

**Abandoned correctly, and only visible on long follow-up:** total lymphoid irradiation looked
symptomatically effective in short trials. At 10 years, 7 of 10 irradiated patients had died
versus 2 of 9 controls, and 3 developed B-cell malignancies. The lesson is about follow-up
duration.

**Contested:** radiation synovectomy. A meta-analysis of 21 studies gives OR 4 (1.2–14) for knee
response at 6 months; a 97-patient RCT found 48% response in *both* arms; an earlier review
found neither included yttrium study favoured treatment. Pooled observational optimism
contradicted by randomisation.

**Never followed up:** the 1991 Lancet trial of a 7–10 day subtotal fast followed by a
gluten-free vegan diet and then lactovegetarian diet (27 vs 26 patients) reported significant
improvement across tender joints, Ritchie index, swollen joints, pain, morning stiffness, grip
strength, ESR, CRP, white cell count and HAQ, with benefits still present at one year, while
only pain improved in controls. It was single-blind with a residential intervention and an
unmatched control setting. It remains the strongest historical dietary result in RA and the
least adequately followed up.

---

## 6. Repurposed drugs

| Intervention | Evidence | Key result | Verdict |
|---|---|---|---|
| Metformin add-on | 4 RCTs, 350 pts | CRP MD −5.55 (−7.46 to −4.52); DAS-28 MD −0.8; HAQ-DI −0.12 | Uncertain (promising, thin) |
| Atorvastatin add-on | 15 RCTs; parallel review 9 RCTs | DAS28 SMD −2.00 (−3.19 to −0.81); parallel −2.46 with I²=97% | Conflicting / implausible |
| Tetracyclines | 10 RCTs | TJC SMD −0.39 (−0.74 to −0.05) | Uncertain |
| Low-dose sirolimus | 1 RCT, 62 pts | Significant DAS28, ESR, TJC reduction | Uncertain |
| Dapsone | 1980s–90s RCTs | Improvement in 5 of 7 clinical measures and ESR | Works — abandoned, never re-tested |
| Cannabis-based medicine (Sativex) | RCT, 58 pts, 5 wk | Significant improvement in pain on movement, pain at rest, sleep quality, DAS28; no effect on morning stiffness | Uncertain (single small trial) |
| Low-dose naltrexone | 7 RCTs (chronic pain) | d = −0.11 (−0.96 to 0.74), P=0.31; fibromyalgia subgroup d = −0.34 | Failed for pain overall |
| Opioids | Cochrane, 11 studies, 672 pts | Global impression RR 1.44 (1.03–2.03); adverse events OR 3.90 (2.31–6.56) | Weak benefit, clear harm |

**The atorvastatin estimate should not be accepted as reported.** An SMD of −2.0 on DAS28 is
larger than that of most biologics. With I²=97% in the parallel review, this is far more likely
to be a pooling artefact than a real effect of a lipid-lowering drug. The cardiovascular benefit
of statins in RA (a UN6 goal) is a separate and better-supported claim.

**The opioid entry is the largest evidence-to-practice gap in this table.** The entire Cochrane
evidence base is 11 short trials, and the only strong opioid studied was controlled-release
morphine in a single 20-patient study — against a real-world pattern of chronic opioid
prescribing in RA.

**Low-dose naltrexone is a documented negative for pain overall**, with adverse events IRR 1.4
(1.12–1.75) versus placebo. Its only positive subgroup was fibromyalgia (d = −0.34), which is
relevant because roughly one third of RA patients meet fibromyalgia criteria (34.2% of 187 in
one prospective cohort). There is no RA-specific LDN trial.

**Helminth therapy and faecal microbiota transplantation** returned no RA efficacy trial at all.
Both follow directly from the mucosal-origins hypothesis in Phase 1, and both are unevaluated in
RA. Microbiome-modulating interventions have RCT data only for inflammatory markers.

---

## 7. Supplements and natural products

**Vitamin D for prevention (VITAL, n=25,871).** Vitamin D 2000 IU/day gave HR 0.78 (0.61–0.99),
P=0.05 for all incident autoimmune disease; omega-3 gave HR 0.85 (0.67–1.08), P=0.19. In the
post-supplementation extension two years later, the vitamin D effect had disappeared (HR 0.98,
0.83–1.17) while omega-3 had become significant (HR 0.83, 0.70–0.99). Both endpoints are *all*
autoimmune disease, not RA alone. This reversal is shown in panel b of the figure below and is
one of the most instructive results in the whole survey.

**Vitamin D in established RA — direct conflict, preserved.** One meta-analysis of 11 studies
reports DAS-28 WMD −0.83 (−1.38 to −0.28), p<0.001, at self-declared moderate certainty. Another,
pooling 27 RCTs across autoimmune diseases, reports no significant effect on pain scores in RA.
These may be partly reconcilable — the positive review found benefit on DAS-28 and ESR but not
on HAQ or VAS-pain, so the disagreement may be outcome-specific rather than a true
contradiction. It is recorded as unresolved.

**Omega-3** reduces tender joint count (SMD −0.59, −0.79 to −0.39) without significantly
changing DAS28, ESR or CRP across 18 RCTs and 1018 patients. Symptom effect without inflammatory
effect points at UN2, not UN1.

**Curcumin** gives DAS28 MD −1.20 (−1.85 to −0.55) from 6 publications that the authors
themselves describe as low quality — an effect size comparable to a biologic from six small
trials, which is the classic signature of small-study bias.

**Probiotics** reduce IL-6 (pooled SMD −0.83), TNF-α (−0.41) and CRP (SMD −0.67, I²=80.8%).
No pooled effect on disease activity or joint counts was reported. Cytokine change is not a
clinical outcome.

**Selenium** gives VAS pain MD −12.68 mm (−19.08 to −6.28) from 7 small studies; selenium has a
narrow therapeutic window. **Vitamin E** is negative: sensitive joints MD −1.66 (−6.32 to 2.99),
I²=93%.

**Dietary polyphenols** across 47 RCTs and 3852 patients improved DAS28, CRP and ESR — but the
pooling combines 15 chemically unrelated compounds, which makes the summary estimate difficult
to interpret or act on.

---

## 8. Traditional Chinese Medicine — herbal

This is the best-evidenced non-Western domain in the survey, and its evidence base is larger
than most Western clinicians assume.

**Tripterygium wilfordii Hook F (TwHF), monotherapy versus methotrexate.** An international
consensus applying GRADE to 19 RCTs and 1795 participants reports ACR20 RR 1.06 (0.90–1.26) at
moderate certainty, ACR50 RR 1.03 (0.80–1.34) at moderate certainty, and ACR70 RR 1.12
(0.69–1.79) at low certainty. This is *non-inferiority to the anchor drug of RA therapy*, not
superiority.

**TwHF added to methotrexate.** ACR20 RR 1.44 (1.28–1.62), ACR50 RR 1.88 (1.56–2.28), ACR70 RR
2.12 (1.40–3.19). An independent meta-analysis of 14 RCTs and 1446 patients gives a remission
rate RR 1.31 (1.11–1.55) and an overall effective rate RR 1.15 (1.10–1.21).

**The critical caveat is inside the same meta-analysis.** Efficacy correlated *positively* with
TwHF dose — biologically coherent — and *negatively* with methotrexate dose and *negatively*
with methodological quality. The last correlation means part of the pooled effect is bias, and
the analysis itself says so. Trials are almost entirely Chinese, mostly open-label, and TwHF
preparations are not standardised between trials.

**TwHF safety is unresolved and this is the central problem.** Trial-level pooling is
reassuring: infection RR 1.37 (0.84–2.23), liver dysfunction RR 1.14 (0.71–1.85), renal damage
RR 2.20 (0.50–9.72) — none significant. But 40 years of toxicology document oligospermia,
reduced sperm motility, testicular atrophy and infertility in males, and menstrual disorder,
amenorrhoea and infertility in females. Short trials in mostly older cohorts cannot detect
gonadal toxicity. The reassuring trial safety data and the concerning toxicology data are not
in contradiction; they are measuring different things over different timescales.

**Total glucosides of paeony (TGP)** — 8 RCTs, 1209 patients: added to csDMARDs, improved
ACR20/50/70 *and reduced adverse effects*, at limited methodological quality. The
adverse-effect reduction (a possible methotrexate-tolerability effect, i.e. UN6) is the less
studied and arguably more interesting of the two claims.

**Sinomenine versus NSAIDs** — 10 trials, 1185 patients: more improved patients and more RF
disappearance (P<0.00001; P=0.008), better morning stiffness, painful joints and ESR; no
difference in swollen joints, grip strength or CRP; fewer digestive but more dermatomucosal
adverse events. NSAIDs are the wrong comparator for a disease-modifying claim, and "RF
disappearance" is an unusual endpoint that needs checking in the primary trials.

**Iguratimod** sits at the boundary of this domain — a synthetic small molecule licensed in
Japan and China, essentially unknown in Western practice. Added to methotrexate across 31 RCTs
and 2776 patients: ACR20 RR 1.55 (1.14–2.13), ACR50 RR 2.04 (1.57–2.65), ACR70 RR 2.19
(1.44–3.34), DAS28 WMD −1.65, with adverse events no different from methotrexate alone, and
GRADE high certainty for ACR70. As *monotherapy* it is not superior to methotrexate (ACR20 OR
1.04, 0.79–1.36 across 12 trials). It has the largest RCT base of any agent in the non-Western
part of this survey.

---

## 9. TCM — acupuncture, moxibustion, and mind-body

This domain contains the clearest unresolved conflict in the entire landscape, and it is
preserved rather than settled.

**Against sham, acupuncture has not shown benefit.** The Cochrane review (2 RCTs, 84 patients)
found no statistically significant difference on ESR, CRP, VAS global, swollen or tender joint
counts, GHQ or DAS. A systematic review of complementary therapies found no significant
difference in pain reduction across three sham-controlled acupuncture trials and concluded there
was no good evidence of efficacy.

**Against conventional therapy and non-acupoint sham, it shows large benefit.** A 2025 network
meta-analysis of 10 RCTs and 704 participants gives electroacupuncture SMD −1.42 (−1.87 to
−0.98) and conventional acupuncture SMD −1.11 (−1.49 to −0.73) for pain, with electroacupuncture
SUCRA 97.7%. A separate network meta-analysis of 32 RCTs and 2115 patients found
electroacupuncture + DMARDs best for DAS28 and fire needle + DMARDs best for VAS, CRP and ESR —
while finding that *no* acupuncture-related therapy beat DMARDs alone for morning stiffness.

**The disagreement is about what counts as a placebo, not about the data.** The network
meta-analysis authors argue explicitly that same-acupoint sham underestimates the true effect
and that non-acupoint sham should be used as the control. If they are right, the older
sham-controlled nulls are uninformative. If they are wrong, the effect sizes above are inflated
by unblinded expectancy. Nothing in the retrieved evidence resolves this, and the negative
morning-stiffness result inside the positive network analysis is a useful internal check that
the effects are not uniform.

**Tai chi** — Cochrane, 7 trials, 345 participants: pain MD −2.15 (−3.19 to −1.11), a 22%
absolute improvement, but from 2 studies and 81 participants at very low quality, downgraded for
imprecision, blinding and attrition. Disease activity was inconclusive (DAS-28-ESR reduction
0.40, −1.10 to 0.30, from 1 study of 43 patients). The majority of trials were at high risk of
performance and detection bias, and roughly 75% did not report random sequence generation.

**Balneotherapy / spa therapy** — Cochrane 2015, 9 studies, 579 patients: mudpacks versus
placebo gave pain MD 0.50 (−0.84 to 1.84) — no benefit — at a very low level of evidence.
Earlier reviews had described most trials as positive with weak scientific support; the later
placebo comparison did not confirm it.

---

## 10. Lifestyle interventions

**Exercise has the most consistent evidence in this domain, and it is not anti-inflammatory.**
Resistance training improves isokinetic strength by 23.7% and isometric strength by 35.8%
(both P<0.001) across 10 RCTs and 547 patients. High-intensity weight-bearing exercise (RAPIT,
309 patients, 2 years) slowed hip bone loss (1.6% decrease in year 1 versus usual care) — notable
mainly because high-intensity exercise had long been avoided in RA on joint-damage grounds.
No effect on inflammation or radiographic progression has been shown.

**Physical activity is the best-evidenced intervention for fatigue, and the effect is small.**
Cochrane, 24 studies, 2882 patients: physical activity SMD −0.36 (−0.62 to −0.10), equal to 14.4
points on a 100-point fatigue scale, NNTB 7; psychosocial interventions SMD −0.24 (−0.40 to
−0.07), NNTB 10. No drug has been shown to relieve RA fatigue independently of inflammation.

**Diet is genuinely uncertain, and the uncertainty is not one-sided.** The Cochrane review of
15 trials gives fasting plus 13-month vegetarian diet pain MD −1.89 (−3.62 to −0.16) on a 0–10
scale and a 12-week Cretan Mediterranean diet pain MD −14.00 (−23.6 to −4.37) on a 0–100 scale,
with elemental diets showing no difference and vegan/elimination effects uncertain from
inadequate reporting. Against this, an overview of systematic reviews concludes the
Mediterranean diet may make little or no difference to pain or disease activity at low
certainty, while a pooled analysis of 7 anti-inflammatory-diet RCTs (326 patients) reports pain
−9.22 mm (−14.15 to −4.29) at very low certainty. Both cannot be strongly true.

**The most reliably measured dietary findings are the harms.** Dietary manipulation raised
drop-out by 10 percentage points (RD 0.10, 0.02–0.18) and produced 3.23 kg more weight loss
(WMD −4.79 to −1.67) than ordinary diets. Adherence, not efficacy, may be the binding
constraint.

**One trial in this domain was designed to find a subgroup rather than an average.** A
double-blind study of 94 seropositive patients over 12 weeks found only subjective improvement
overall and no difference between allergen-free and allergen-restricted diets — but 9 patients
improved and then flared markedly on rechallenge, with changes in objective activity measures.
The "food-intolerant RA" subgroup hypothesis has not been retested with modern tools in more
than 30 years.

**Periodontal treatment** reduced disease activity with SMD −0.88 (−1.38 to −0.38) across 9
studies and 388 patients, at low or very low GRADE certainty, with selection bias and unstable
RA medication named as heterogeneity sources. This is one of the few interventions that directly
tests the mucosal-origins hypothesis from Phase 1 by intervening on it.

**Smoking** shows the widest gap between risk-factor evidence and intervention evidence in the
survey. Risk of RA remains elevated 15 years after cessation (RR 1.99, 1.23–3.20) and even 1–7
cigarettes per day carries RR 2.31 (1.59–3.36) — while the Cochrane review of cessation
*interventions* in RA found 2 studies, 57 patients, and no evidence of benefit at very low
certainty.

**Mindfulness** shows its clearest effect on depressed mood (MBCT depression SMD −0.72, −1.22 to
−0.22) rather than on pain or disease activity. **Yoga** has positive pooled evidence that is
largely borrowed from non-RA conditions. **Sleep interventions** — 5 studies, 262 patients, no
consistent or conclusive evidence — despite sleep disturbance being near-universal in RA.

---

## 11. Conflicting and negative evidence, preserved

!Standardised effect sizes by evidence quality, and the VITAL prevention reversal

Panel **a** places every intervention whose result was reported as a standardised mean
difference on one axis, coloured by the quality of the evidence behind it. The ordering is the
finding: the four largest reported effects in RA — atorvastatin, electroacupuncture,
conventional acupuncture, periodontal treatment — all come from evidence the authors themselves
grade as low or very low certainty, while every Cochrane-grade estimate sits between −0.24 and
−0.57. Effect size and methodological rigour run in opposite directions. This does not prove the
large estimates are wrong. It does mean that a large reported effect in this literature is
weak evidence of a large real effect, and that direct comparison of effect sizes across evidence
tiers is invalid.

Panel **b** shows the VITAL reversal in full: on treatment, vitamin D looked protective and
omega-3 did not; two years after stopping, the vitamin D effect was gone and the omega-3 effect
had appeared. A single trial supports opposite conclusions depending on when it is read.

### Register of preserved conflicts

| Conflict | Side A | Side B | Status |
|---|---|---|---|
| Acupuncture for RA pain | Cochrane and CAM review: no difference vs sham | Network meta-analyses: SMD −1.11 to −1.42 vs conventional therapy and non-acupoint sham | Unresolved; disagreement is about control validity |
| Vitamin D in established RA | DAS-28 WMD −0.83, moderate certainty | No significant effect on pain across 27 RCTs | Unresolved; may be outcome-specific |
| Vitamin D for prevention | HR 0.78 at 5.3 yr on treatment | HR 0.98 at 7.3 yr after stopping | Same trial, opposite readings |
| Mediterranean / anti-inflammatory diet | Pain −9.22 mm and −14.00/100 | "Little or no difference" in pain or activity | Unresolved |
| Radiation synovectomy | Meta-analysis OR 4 (1.2–14) | RCT: 48% response in both arms | Randomisation contradicts pooling |
| Statins in RA | DAS28 SMD −2.00 | I² = 97% in parallel review | Effect size not credible as stated |
| TwHF safety | Trial-level AEs not significantly raised | 40 years of reproductive toxicology | Different timescales, both real |
| Low-dose glucocorticoids | DAS28 and damage benefit, both p<0.005 | Harm 60% vs 49%, RR 1.24 | Both endpoints met in one trial |
| IL-17 inhibitors | ACR20 RR 1.67 in TNF-IR | Not used in RA | Reason not retrieved |

### Register of preserved negative results

- Acupuncture versus sham: no significant difference on any outcome (Cochrane; CAM review).
- Vitamin E: no benefit on sensitive or swollen joints.
- Balneotherapy mudpacks versus placebo: no pain benefit.
- Low-dose naltrexone: no pain benefit overall (d = −0.11, P=0.31), with increased adverse events.
- Elemental diets: no difference in pain, function or stiffness.
- Food-allergen elimination: negative on average (positive only in a rechallenge-defined subgroup).
- Smoking-cessation interventions in RA: no evidence of benefit.
- IV doxycycline (n=23): 1 responder versus 0 on placebo.
- Blood-flow-restricted low-intensity resistance training: SMD −0.01.
- Acupuncture-related therapies for morning stiffness: none beat DMARDs alone.
- Iguratimod monotherapy: not superior to methotrexate (ACR20 OR 1.04).
- TwHF monotherapy: not superior to methotrexate (ACR20 RR 1.06).
- p38 MAPK inhibition: signal did not sustain into a usable drug.
- Total lymphoid irradiation: net harm at 10 years.
- Mediterranean diet: may make little or no difference (low certainty).
- Omega-3: no significant effect on DAS28, ESR or CRP despite the tender-joint effect.
- Probiotics: no pooled disease-activity outcome reported.

---

## 12. Patient-generated research priorities (Phase 1 gap, now closed)

Phase 1 could not retrieve patient-set research agendas. This has now been closed.

**A James Lind Alliance Priority Setting Partnership for RA** generated 212 questions from three
focus groups, distilled them to 36 for survey, and collected 554 responses (mean age 58 [SD 13];
481 [87%] women; 449 [81%] people with RA, 105 [19%] healthcare professionals). Ranking produced
a shortlist of 26 and then a top 10. The top 10 priorities address **prevention, rapid diagnosis,
identifying effective treatments, reducing treatment side effects, and holistic management.**

Three things follow from this, and each is checkable against the map above.

**Prevention is a top patient priority and has 4 candidate interventions in the entire
landscape** (vitamin D, omega-3, periodontal treatment, smoking cessation) — of which the two
supplement entries are for all autoimmune disease rather than RA, and the smoking-cessation
intervention literature is empty.

**Reducing side effects is a top patient priority and maps to UN6, which has 10 entries** —
mostly incidental (a drug that happens to be better tolerated) rather than interventions
designed to reduce toxicity. TGP is one of the few entries where reduced adverse effects is
itself the reported outcome.

**"Holistic management" maps to UN2**, where the best-evidenced intervention is physical
activity at SMD −0.36.

Two further findings sharpen the patient-versus-clinician picture:

- A meta-epidemiological analysis of 73 double-blind RCTs (165 comparisons, 33,956 patients)
  found physician global assessment improved more than patient global assessment (SMD −0.60 vs
  −0.50; ΔSMD −0.09, −0.12 to −0.05), with the contrast driven by swollen joint count, and pain
  independently associated only with the patient assessment. **Treatments look better to
  physicians than to patients, and the gap is specifically about pain.**
- In an observational cohort of 210 patients with long-standing RA, EQ-5D 0.57 and HAQ 0.75 at
  baseline remained largely unchanged over 12 months of ongoing treatment; 61% reported
  difficulty with housework and 55% needed external support.
- Concomitant fibromyalgia was present in 34.2% of 187 patients with RA, independently
  associated with higher DAS28-CRP, driven predominantly by subjective components, and
  associated with more corticosteroid use despite less frequent DMARD use.

That last finding is a mechanism by which UN2 becomes a treatment-safety problem: symptom-driven
escalation of immunosuppression in patients whose symptoms are not being driven by inflammation.

---

## 13. Where the landscape is empty

Distinguishing *failed* from *unstudied* is the point of this section. The following are not
negative results; they are absences.

| Gap | What exists | What does not |
|---|---|---|
| **Predicting individual response (UN4)** | Evidence that switching works on average | Any intervention, in any tradition, that selects the drug for the patient |
| **Drug-free remission (UN3)** | 3 entries across 67 interventions | Any tolerance-restoring therapy with controlled RA data |
| **ACPA-negative / subgroup disease (UN7)** | 2 entries, both incidental | Any intervention developed or tested for a defined RA subgroup |
| **Structural repair (UN8)** | Denosumab, 1 trial | Anything else |
| **Non-invasive vagus stimulation** | 4-day open-label pilot, n=16 | Any sham-controlled trial, despite a positive pivotal trial of the implanted version |
| **Helminth therapy, faecal transplant** | Reviews and mechanism | Any RA efficacy trial |
| **Treg / low-dose IL-2** | Reviews | Any controlled RA trial |
| **Sleep** | 5 studies, no conclusion | Adequately powered trials of a near-universal symptom |
| **Dapsone** | Positive 1980s–90s RCTs | Any modern replication |
| **Food-intolerance subgroup** | 1992 rechallenge study | Any modern retest |
| **RA-specific cannabinoid data** | One 58-patient trial from 2006 | Anything since |
| **RA-specific LDN data** | None | Any RA trial, despite widespread off-label use |

---

## 14. Limitations of this survey

1. **Abstract-level only.** No full texts were retrieved. Reported numbers should be re-verified
   against full texts before use.
2. **English-language PubMed.** The TCM evidence base extends into Chinese-language databases
   (CNKI, Wanfang) that were not searched. TCM coverage here is therefore a lower bound, and is
   biased toward interventions with international publication.
3. **Retrieval failures.** Several over-conjoined Boolean queries returned zero hits and were
   re-issued in shortened form; a few named targets returned nothing and were left unretrieved
   rather than substituted. Absence from this map is weak evidence of absence in the literature.
4. **Domain tagging is imperfect.** Some records surfaced under domains they did not belong to,
   and a small number concerned other diseases entirely; these were excluded rather than
   silently carried, but the exclusion was manual.
5. **Verdict classes are judgements.** They are assigned from the retrieved evidence and are
   reproducible from the map file, but they are not computed and another reviewer could
   reasonably differ, particularly on the boundary between *Uncertain* and *Failed*.
6. **The 67 interventions are not the complete landscape.** They are the interventions with
   retrievable human evidence that survived design-based triage.
7. **No efficacy claim is made anywhere in this document.** Every statement above is an
   attribution to a specific cited source with its evidence tier and its stated caveats.

---

## 15. What this phase does not do

No Research Leads are proposed here. No intervention is recommended, ranked, or endorsed. The
conflicts in §11 are left open because the retrieved evidence does not close them, and closing
them prematurely would be the specific failure mode this project is designed to avoid.

**Companion files**
- `ra_phase2_treatment_map.csv` — 67 interventions with verdict class, evidence design, evidence
  base size, population, outcome, verbatim key result, direction, author-stated certainty,
  linked Phase 1 unmet need, main caveat, PMID and DOI.
- `ra_phase2_landscape.png` — verdict composition by domain and unmet-need coverage matrix.
- `ra_phase2_effect_vs_rigour.png` — standardised effect sizes by evidence quality; VITAL
  prevention reversal.
- Phase 1: `RA_phase1_evidence_baseline.md`, `ra_phase1_references.csv`,
  `ra_phase1_open_questions.csv`, `ra_phase1_treatment_ceiling.png`.
