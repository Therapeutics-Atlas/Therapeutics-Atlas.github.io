# IPF Phase 2 Brief — prespecified rules, fixed before any treatment effect was read

**Status: PRESPECIFIED.** Written 2026-09-02, before any Phase 2 retrieval of treatment effects.
Linked from `IPF_SCOPE.md` Part C, which deferred six criteria to this brief. Entered in
`corrections_log.csv` (C4) so a reader can verify the rules were set before results were seen, not
after.

This brief fixes only what Part C deferred. It does not modify L1–L6 and does not restate them.

**What had been read when this brief was written:** Phase 0, Phase 1 and their tables (endpoint
taxonomy E1–E15, ceiling, standard of care, retrievability register, unmet needs UN1–UN12,
corrections log), plus `IPF_SCOPE.md`. **Not** read: any Phase 2 intervention-level result, any TCM
trial result, any registry pull beyond the Phase 0/1 files.

---

## §1 Curated-intervention inclusion (Part C item 4)

The registry pull contains ~488 distinct intervention strings. Nothing is discarded. Every
intervention entity is placed in one of four **inclusion tiers**, and the tier is a column in
`ipf_phase2_landscape.csv`:

| Tier | Definition | Treatment in the landscape |
|---|---|---|
| **I1** | Any IPF-specific human trial at phase 2 or above, **or** an IPF-specific randomised publication of any phase | Fully graded row: verdict class, key result verbatim, identifier, endpoint E-code, duration, placebo-arm change where reported |
| **I2** | IPF-specific human evidence below that bar — phase 1, single small randomised trial without phase label, non-randomised human study, or an observational analysis naming the intervention | Row with verdict class restricted to `Uncertain`, `Poorly studied`, `Failed`, `Harm outweighs benefit` or `Conflicting`; `Works` is not available at this tier |
| **I3** | Registry-only: an intervention appears in a registered IPF trial but no human outcome evidence could be retrieved | Row graded `Poorly studied`, with the retrieval attempt recorded; if the trial is completed, the study also enters the retrievability register (L5) |
| **I4** | Named in the IPF literature with **no** IPF-specific human study retrieved — preclinical only, or extrapolated from PPF/ILD | Recorded in the landscape file with `Poorly studied` and an `indirect_evidence_only` flag; never graded on efficacy (L2) |

Rationale for tiers rather than a cutoff: a rank cutoff on 488 strings would silently delete the
"poorly studied" category, which the method treats as a distinct verdict from "failed"
(non-negotiable 8). Tiering keeps the whole set countable and lets a reader see exactly where the
evidence thins.

**Entity resolution rule.** Registry strings are collapsed to intervention entities by active
agent, not by trade name, arm label or formulation; formulation differences that plausibly change
delivery (e.g. inhaled versus oral) are kept as separate entities and the reason is recorded.
Placebo, standard-of-care comparator, "no intervention", diagnostic-only and device-measurement
arms are not intervention entities and are counted separately. Combination arms are recorded as
their own entity **and** cross-referenced to each component.

## §2 The bar for grading a row on survival (Part C item 5)

Phase 1 established that no trial-level surrogacy of lung function for mortality was retrieved. It
follows:

1. **No FVC, DLCO, HRCT or composite-progression result may be graded on the survival dimension**,
   in any tier, however large. Such a result is graded on its own E-code only.
2A row may carry a survival grade only from (a) randomised evidence with all-cause mortality as a
   prespecified primary or key secondary endpoint, or (b) an explicit mortality analysis in a
   human cohort that states its adjustment or causal-inference method.
3. Evidence of type (b) alone caps the survival statement at `Probable` at best, and at `Uncertain`
   where confounding by indication is unaddressed. `Established` on survival requires type (a).
4. A pooled estimate is quoted with its heterogeneity and with the design mix of its inputs; a
   pooled estimate whose inputs are predominantly observational is labelled as such in the row.

## §3 Admissibility of cross-trial FVC comparison (Part C item 6)

Phase 1 found placebo-arm FVC decline differing about three-fold across pivotal trials.

- **Quantitative cross-trial comparison of FVC effect magnitudes is not admissible** in this record.
  No ranking, no arithmetic difference and no pooling across trials of mL or %pred effects.
- Admissible: the **within-trial between-group difference**, quoted in the source's own metric with
  its duration and, where reported, the placebo-arm change. `ipf_phase2_landscape.csv` therefore
  carries `metric`, `duration_weeks` and `comparator_arm_change` columns; a row missing them cannot
  be used in any comparative statement.
- Ordering interventions by effect size is permitted **only** within a set matched on metric
  variant, duration and population, and any such set states its members explicitly.
- The effect-size-versus-evidence-quality relation the method asks to plot early is plotted with
  **one point per study**, axis labelled as within-trial effect, and no cross-trial magnitude claim
  is drawn from it.

## §4 TCM and traditional-medicine screening rules (L4 prespecification)

Applies to all traditional, historical, herbal and natural-product interventions, of any tradition.

### §4.1 Eligibility

- **Population:** IPF only (L1). Mixed IPF/other-ILD populations are eligible but flagged
  `indirect`, with the population stated on the row; they may never be sole support for a statement.
- **Intervention:** any traditional-system, herbal, formula, natural-product or historical
  intervention, single or compound, any route.
- **Outcome:** at least one **objective measure or validated patient-reported instrument mapping
  onto an L3 outcome dimension** (an E-code in `ipf_phase1_endpoint_taxonomy.csv`). A trial whose
  only outcome is a traditional syndrome score, a non-validated composite "total effective rate",
  or a laboratory marker with no E-code mapping is **outcome-ineligible**.
- **Design:** no design is excluded at the eligibility step. Design determines tier (§4.2).

### §4.2 Evidence tiers, in place of numeric thresholds

No minimum sample size, treatment duration or follow-up is set as a gate. Part C deferred those
thresholds precisely because the corpus distribution was unknown, and a number chosen now — or
chosen after seeing which trials it admits — would be untraceable. Instead, tiers are defined by
**design and reporting features that are visible before any effect is read**, and sample size and
duration are *reported* on every row as descriptors and used to caveat, never to exclude:

| Tier | Definition |
|---|---|
| **T1** | Randomised, IPF-only population, ≥1 eligible outcome, prospectively registered, and full text retrievable |
| **T2** | Randomised, IPF-only, ≥1 eligible outcome, but not prospectively registered, or retrievable only as an abstract, or with no description of allocation concealment |
| **T3** | Non-randomised human evidence (cohort, before–after, case series), or a randomised trial in a mixed population (`indirect` per L1) |
| **T4** | Outcome-ineligible per §4.1 (syndrome score or non-validated composite only), or non-human evidence only. **Preserved with its identifier and the reason for placement; never graded on efficacy.** |
| **T5** | Identified but the result could not be obtained (no full text, no abstract data, registered-only). Enters the retrievability register (L5) rather than being dropped. |

No study identified by the screen is deleted. A study that fails the T1 bar moves down a tier and
keeps its row, its identifier and a stated reason.

### §4.3 Risk of bias — reported, not a gate

Risk of bias is assessed with **Cochrane RoB 2** domains, recorded per included study in a
`risk_of_bias_tool` and `risk_of_bias_judgement` field. It does **not** gate inclusion: a gate set
before seeing how the corpus scores could empty the domain, which is a conclusion disguised as a
method. It **caps the verdict** instead — a T1 study judged high risk of bias, or with concerns in
the randomisation domain, cannot lift its intervention above `Uncertain`.

### §4.4 Corpus description before grading

The screen first reports the corpus's own distribution — number of studies, sample sizes,
durations, outcome types, publication venues, registration status — and that description is
published whether or not any study reaches T1. This is the step that would have been needed to
justify a threshold; it is reported instead of being converted into one.

### §4.5 Database coverage declaration

The coverage actually achieved is declared per L4, including "not searched" where true. Chinese
biomedical databases (CNKI, VIP, Wanfang, SinoMed) are not reachable from this environment; if that
remains true at execution, the screen declares them **not searched**, and every TCM count in the
record is stated as a lower bound restricted to PubMed-indexed literature.

### §4.6 Interpretation limits

- No claim may depend on a traditional theoretical entity (syndrome type, qi, meridian) being
  biologically real. Such entities may be described as trial eligibility criteria, which is a
  factual statement about the trial.
- Absent T1 evidence with low risk of bias, the maximum verdict available to the traditional-medicine
  domain as a whole is `Poorly studied` or `Uncertain`; a domain-level `Works` is not reachable
  under these rules and would require evidence this brief has prespecified as absent.
- Herbal-product safety findings are graded on the safety dimension independently of any efficacy
  tier, and a safety signal is never downgraded because the efficacy evidence is weak.

## §5 What this brief does not decide

It does not decide any verdict, does not name a candidate intervention, and does not rank anything.
Verdict classes and evidence tiers remain those of the method (`Works`, `Works — abandoned anyway`,
`Conflicting`, `Uncertain`, `Failed`, `Harm outweighs benefit`, `Poorly studied`; `Established`,
`Probable`, `Uncertain`, `Hypothesis`, `Unknown`), applied per row with a stated sub-label.
