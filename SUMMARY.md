# Open Therapeutics #001 — Rheumatoid Arthritis
## Three-page summary

This is a dated snapshot of an open record. It makes no treatment recommendation and asserts no
efficacy. Every number below is traceable to a primary source through `data/references.csv` and the
per-row identifiers in `data/intervention_register.csv`. Nothing here has been peer reviewed.

---

### 1. Where treatment stands

Modern RA treatment is effective and has a ceiling that is visible in its own trials.

- The best first-line arm in a head-to-head strategy trial reached CDAI remission in **59%** of
  patients at 48 weeks. Roughly two in five did not reach remission on the best available start.
- **Drug-free remission is real but unevenly distributed.** At five years it was reached by about
  22% of autoantibody-positive patients, 38% of autoantibody-negative patients, and 56% of
  undifferentiated arthritis. The clinical rule that patients "cannot stop" is partly an artefact of
  which patients were studied.
- Withdrawal usually fails when attempted in the wrong population: **63%** flared within 12 months
  on taper-to-withdrawal versus **5%** on a stable TNF inhibitor.
- Refractory disease is uncommon but not rare: **11.7%** meet the EULAR difficult-to-treat
  definition, **4.3%** have failed three or more b/tsDMARDs, **1.6%** four or more.
- Prevention can delay onset but is not established. In the two interception trials, the
  intervention-versus-placebo gap at the end of follow-up was large in one subgroup
  (9% vs 32% progression) and near-absent in another (58% vs 65%) — see lead RL-01 below, because
  that contrast is the single most consequential unreplicated finding in this record.

### 2. What the landscape looks like when everything is graded on one scale

67 interventions across 12 domains were graded on identical criteria — modern, historical,
repurposed, supplements, TCM herbal and non-herbal, acupuncture, mind–body, lifestyle.

**Only 14 of 67 have replicated human benefit and are still in use.** The remainder split into
positive evidence that left practice anyway (8), conflicting evidence (10), evidence too weak to
bear the weight placed on it (21), adequate testing with no benefit (5), real effect with
unacceptable harm (4), and plausible-but-unevaluated (5).

Two structural findings are more informative than any individual row.

**One unmet need has no candidate intervention in any tradition.** Mapping every intervention onto
the eight unmet needs from the baseline review, *predicting which treatment will work for an
individual* attracts no intervention of any kind — not modern, not historical, not traditional. It
is not a crowded field with poor results; it is empty. By contrast, refractory inflammatory disease
attracts 41 of the 67.

**Reported effect sizes run largest where the evidence is weakest.** Plotting effect size against
evidence quality produces a clean inverse relationship: the largest reported standardised mean
differences (statin add-on at −2.00, electroacupuncture at −1.42) come with I² = 97% or with a
control-validity problem, while Cochrane-grade moderate-certainty findings cluster between −0.2 and
−0.5. This is a property of the literature, not of the treatments.

**On traditional medicine specifically**, following the evidence produced a mixed result that
neither confirms nor dismisses the tradition. *Tripterygium wilfordii* added to methotrexate
improved ACR20/50/70 (RR 1.44, 1.88, 2.12; moderate-to-low certainty), but as monotherapy it was
not superior to methotrexate (ACR20 RR 1.06, 95% CI 0.90–1.26), and its safety verdict is recorded
as **conflicting** — trial-level adverse events were not significantly raised, against forty years
of reproductive toxicology. Acupuncture versus sham showed no significant difference on any
measured outcome, while network meta-analyses against conventional therapy and non-acupoint sham
report large effects; the disagreement is about what the control is, and it is preserved unresolved.

### 3. The negative results

Seventeen interventions were tested adequately enough to record a negative result, and they are
kept as a register rather than discarded: acupuncture versus sham, vitamin E, balneotherapy
mudpacks, low-dose naltrexone (with increased adverse events), elemental diets, food-allergen
elimination on average, smoking-cessation interventions, intravenous doxycycline, blood-flow-
restricted resistance training, iguratimod monotherapy versus methotrexate, TwHF monotherapy versus
methotrexate, p38 MAPK inhibition, total lymphoid irradiation (net harm at ten years), the
Mediterranean diet, and omega-3 on disease-activity endpoints.

This register is the part of the record most likely to save someone else's effort, and it is the
part a conventional review would compress into a sentence.

### 4. The conflicts left unresolved

Nine disagreements between credible sources are recorded without forcing a resolution. Three are
worth naming because they are instructive about method rather than about RA:

- **Vitamin D for prevention** — the same trial reads HR 0.78 on treatment at 5.3 years and HR 0.98
  two years after stopping. One trial, opposite readings, depending on when you look.
- **Radiation synovectomy** — a meta-analysis gives OR 4 (1.2–14); the randomised trial found a 48%
  response rate in *both* arms. Pooling and randomisation contradict each other.
- **Low-dose glucocorticoids** — benefit on disease activity and on damage, both p<0.005, alongside
  harm at 60% versus 49% (RR 1.24). Both endpoints were met in one trial; this is a trade-off, not
  an uncertainty.

### 5. What remains open

Twenty-two candidate signals were triaged; six became research leads; verification against primary
full texts then reduced these to **two open leads**, both of which need an analysis of data that
already exists rather than a new trial.

**RL-01 — imaging-burden-selected interception.** In a placebo-controlled interception trial,
methotrexate-based treatment was associated with reduced progression in a high-risk subgroup, and a
companion analysis identified baseline MRI inflammatory burden as the feature marking those who
responded (OR 1.4 per RAMRIS unit; positive predictive values 77% and 79%). Verification reframed
this lead substantially: the selection axis is imaging burden, **not** ACPA status; the subgroup
analysis was not in the published analysis plan; no interaction test and no multiplicity adjustment
are reported; and the four-year and five-year results are the same 66 participants with 13 events,
not independent replications. The open question is narrow and answerable: is baseline MRI burden
*predictive* (it modifies the treatment effect) or merely *prognostic* (it marks who improves
anyway)? The published analysis used the treated arm only, so the trial's own placebo arm settles
it. A one-page specification of that analysis is in `docs/`.

**RL-02 — stromal-signature selection.** Synovial pathotype predicts drug response in two
biopsy-driven cohorts, and no interventional RA trial has ever selected patients on a
stromal/fibroblast molecular signature. Verification corrected this project's original claim that
no stromal-directed agent had been tried at all — a phase 1b of a CDK inhibitor enrolled 15
patients and set a maximum tolerated dose — and narrowed the surviving claim to selection, not
agent. It also weakened the biological premise: pauci-immune patients failed rituximab but
responded normally to etanercept and tocilizumab, so the resistance is drug-specific, not general.
Two questions remain: did the planned efficacy stage of that phase 1b trial ever enrol or report
(absent from every public record checked), and is "stromal-high" a transferable endpoint or a
restatement of "B-cell-poor"?

**Neither lead justifies a new clinical trial at this stage**, and the record says so explicitly.
Both next steps are re-analyses of existing data, and both are blocked on discretionary access held
by the original groups — one dataset available only case-by-case from a corresponding author, the
other commercially restricted. That is the current state: not a scientific obstacle, an access one.

Four leads were closed: one because a randomised trial is already testing its question, one because
its question had been answered, one reclassified from a therapeutic direction to a methodological
caveat about sham controls, and one left explicitly unresolved on insufficient evidence.

### 6. How to check this record

`data/corrections_log.csv` lists nine statements this project made and then retracted, with the
cause of each. **Three of the nine were cases where an apparent research gap was a gap in our own
search strategy** — a base rate worth carrying into any reading of the remaining claims. The phase
reports in `phases/` are preserved unedited so that the reasoning can be audited rather than taken
on trust, each carrying a banner pointing at what was later superseded.

The most useful correction anyone could contribute is a primary record we missed.
