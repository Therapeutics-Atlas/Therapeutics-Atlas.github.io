# IPF_SCOPE.md — fixed disease-specific scope for the IPF Open Evidence Record

**Status: FIXED for Phases 1–6.** Adopted 2026-09-02, immediately after the Phase 0 verdict
`GO WITH SCOPE LIMITS` ([IPF_phase0_disease_selection.md](IPF_phase0_disease_selection.md)) and an
audit of the four proposed limits against that report. Machine-readable form:
`scope_limits.csv`.

This file is the Phase 1 gate required by the Open Therapeutics workflow. Every later phase opens
by reading it and closes by stating which limits bound its output. A limit that cannot be enforced
structurally must be reported as a live risk, not dropped. Changes to this file after adoption go
through `corrections_log.csv`; the limits are not revised silently.

Scope limits restrict what the *record* may contain and claim. They are not statements about
biology, and they are not clinical guidance.

---

## Part A — Audit of the four Phase 0 limits

No new literature or registry retrieval was performed for this audit. Sources are the Phase 0
report and its saved tables only (`ipf_phase0_pivotal_trials.csv`, `ipf_phase0_stopped_trials.csv`,
`ipf_phase0_open_questions.csv`, `ipf_phase0_registry_summary.json`, `ipf_ctg_raw.csv`).

| Limit | Supported by Phase 0? | Audit finding | Action |
|---|---|---|---|
| **L1** Disease boundary | Yes — §8 risk 1 (centre of gravity moving to PPF; the December 2025 approval is PPF-wide), §2 (three approvals, one of them PPF-labelled) | Sound, but incomplete in one respect: the diagnostic definition cited (2022 ATS/ERS/JRS/ALAT) postdates most of the evidence base. Phase 0's own register contains trials from 2000–2014 (IFIGENIA PMID 16306520, INSPIRE PMID 19570573, PANTHER PMID 22607134) that used earlier diagnostic criteria. As written, L1 either silently excludes them or silently re-labels them. | **Revised** — added a diagnostic-vintage rule |
| **L2** Evidence-type gate | Yes — §8 risk 2 (most of 18,308 records are mechanistic), §2 finding 3 (reversal exists only as a preclinical hypothesis) | Supported but **unnecessarily restrictive as worded**. "Admitted only where cited to explain a specific human observation" would exclude the disease-biology statements the Open Map's "what we know / what we do not know about the disease" sections require, and would exclude the preclinical reversal claim that Phase 0 itself records and that open question Q1 is built on — that claim explains no human observation. The intent (no efficacy claim resting on preclinical work) is preserved by a verdict-class bar rather than by an admission bar. | **Revised** — loosened, with the efficacy bar made explicit |
| **L3** Outcome-dimension separation | Yes — §2 (four incompatible FVC metrics in the pivotal trials), §5.4 (≈3-fold placebo-arm drift), §8 risk 5, and the stated biggest risk (the record becoming a record of a surrogate) | Sound and load-bearing. One addition follows directly from Phase 0 §2 finding 5: in TETON-1/TETON-2 the acute-exacerbation results were not "negative", they were **hierarchy-stopped** after the FVC endpoint (PMID 42149993, 41812190). A schema that records only significance would misreport those rows as tested-and-null. | **Revised** — added an endpoint-status field |
| **L4** Traditional-medicine handling | Yes — §3 (323 clinical studies, 295 RCTs, uniformly low quality, PMID 39805768), §8 risk 3 (CNKI/VIP/Wanfang/SinoMed not searched), §5.9 (volume without resolvable signal) | The *requirement* is supported. Two of its criteria are **not yet justified and must not be fixed here**: the numeric thresholds ("minimum duration, minimum sample size") cannot be set without the corpus's own distribution, which Phase 0 did not retrieve. Separately, restricting eligibility to "objective FVC or DLCO endpoint" is **unnecessarily restrictive and internally inconsistent with L3**: it would pre-decide that only surrogate endpoints count, in a record whose central risk is surrogate dependence. | **Revised** — thresholds deferred to a prespecified Phase 2 brief; endpoint criterion broadened |

### Missing limits

Phase 0 mandates two things in its verdict and risk sections that the four proposed limits do not
carry, so the scope would have been unenforceable as delivered:

1. **Retrievability.** Phase 0 §4 (of 239 completed interventional trials, 90 have posted results;
   129 completed since 2010 have none), §5.1 (PRECISIONS NCT04300920 completed, no results posted,
   no primary publication indexed), §7 ("missing results at scale"), and verdict §4, which names a
   **retrievability register** as one of Phase 1's first two deliverables — "a register the RA
   record did not need and this one does". A deliverable named in the verdict but absent from the
   limits is not binding on later phases. → **L5**, which also carries the registry-coverage
   declaration that Phase 0's limitations section shows is needed (ClinicalTrials.gov only; EU CTR,
   jRCT, ISRCTN and Chinese registries unsearched, so all trial counts are a lower bound).
2. **Currency and dating.** Phase 0 §8 risk 4 (three phase 3 readouts and one approval in
   2025–2026; "any statement must be dated") and §3 (the 2025–2026 readouts materially change the
   landscape relative to any review written before 2024). → **L6**.

### Nothing was found to be unsupported

No proposed limit lacked Phase 0 support, and none was removed. Two were loosened (L2, L4), two
were tightened in specificity without broadening their reach (L1, L3), and two were added (L5, L6).

### Deviation from the earlier machine-readable draft

`scope_limits.csv` as first written after Phase 0 had five rows and merged retrievability with
dating into a single L5. This audit separates them, because their enforcement mechanisms differ (a
register versus a per-row field plus a supersession rule) and a merged limit lets either half be
satisfied while the other is not. The CSV is reissued with six rows to match this file, which is
authoritative.

---

## Part B — The fixed limits

### L1 — Disease boundary

The record covers **IPF only**, as defined by a usual interstitial pneumonia (UIP) pattern with no
identified cause (2022 ATS/ERS/JRS/ALAT criteria, PMID 35486072).

- Evidence from **progressive pulmonary fibrosis (PPF), non-IPF ILD, or other fibrotic diseases**
  may enter only as explicitly labelled **indirect evidence**, with the studied population stated
  in the row itself. It may never be the sole support for a statement about IPF.
- **Diagnostic vintage.** Studies that predate the current criteria are included and graded on the
  criteria **in force at the time**, recorded per row (`diagnostic_criteria_vintage`). A study is
  not excluded for having used an earlier definition, and its result is not re-labelled as though
  it had used the current one.
- Mixed-population trials are included only where an IPF subgroup is reported, and the IPF-subgroup
  status is recorded per row.

*Enforced by:* mandatory `population` and `diagnostic_criteria_vintage` fields on every register
row; `evidence_direction = indirect` for non-IPF populations.

### L2 — Evidence-type gate (revised)

Human clinical evidence is the spine of the record.

- **No efficacy statement, and no verdict class other than `Poorly studied`, may rest on
  preclinical evidence.** Animal, in-vitro and mechanistic work never raises an intervention's
  verdict class or evidence tier.
- Preclinical and mechanistic evidence **is** admitted for: (i) disease-biology statements in the
  "what we know / do not know about the disease" sections; (ii) explaining a specific human
  observation; (iii) rows explicitly tiered `Hypothesis`. Where a therapeutic direction exists
  **only** preclinically, it is recorded as `Hypothesis` with no human evidence — which is a
  finding, not a gap to be filled with mechanism.
- Preclinical work is not systematically reviewed. It is retrieved only where one of the three
  admissions above applies, and the retrieval is stated.

*Enforced by:* `evidence_level` field with preclinical tiers barred from any verdict class above
`Poorly studied`; screening exclusion rule for unsolicited preclinical literature.

### L3 — Outcome-dimension separation (revised)

The following outcome dimensions are **separate schema fields** and are never combined into an
undifferentiated "works" statement: **rate of FVC decline · prevention of progression · recovery of
lost lung function · reversal of established fibrosis · acute exacerbation · symptoms (cough,
dyspnoea) · quality of life · functional capacity · all-cause mortality / survival · durability**.

- The **FVC metric** is recorded per row (`fvc_metric`: annual rate of decline / absolute change /
  median change / categorical threshold / other), because the pivotal trials use all four and they
  are not interconvertible.
- The **endpoint status** is recorded per row (`endpoint_status`: primary / prespecified secondary,
  tested / secondary, hierarchy-stopped and not formally tested / post-hoc / exploratory), so a
  hierarchy-stopped endpoint is never reported as a tested null.
- Comparator and background therapy are recorded per row (`comparator`, `background_therapy`),
  because placebo-arm decline varies ~3-fold and several modern trials run on antifibrotic
  background.
- Effect sizes are reported in the source's own metric. No conversion, no pooling across metrics.

*Enforced by:* one column per outcome dimension plus `fvc_metric`, `endpoint_status`, `comparator`,
`background_therapy`; a row with a value in only the FVC field may not be graded `Works`.

### L4 — Traditional, historical and non-English evidence (revised)

TCM and other traditional or historical interventions are **included as a domain**, and the
295-RCT base is handled as a prespecified **screening** task, not as a narrative.

- Screening criteria are **fixed in the Phase 2 TCM screening brief before any result is read**,
  and the brief is published with the record. The criteria themselves are deliberately **not fixed
  here** (see Part C).
- Eligibility requires **at least one prespecified objective or validated patient-reported outcome
  mapping onto an L3 dimension** — not FVC or DLCO specifically. A trial reporting only a validated
  symptom or quality-of-life instrument is eligible, with its dimension recorded per L3; a trial
  reporting only TCM syndrome-score change is not.
- Risk of bias is assessed with a named published tool and reported per included study.
- The **Chinese-language database coverage actually achieved** (CNKI, VIP, Wanfang, SinoMed) is
  declared explicitly, including "not searched" where that is the truth, as the RA record did for
  its gap.
- No claim may depend on a traditional theoretical entity being biologically real.

*Enforced by:* the prespecified Phase 2 screening brief; a coverage-declaration section in the
Phase 2 report; `risk_of_bias_tool` and `outcome_dimension` fields per included study.

### L5 — Retrievability (added)

Completed-but-unreadable studies get **their own register**
(`ipf_phase1_retrievability_register.csv`), built in Phase 1 and maintained thereafter — not a
footnote.

- Every completed interventional trial with no posted results and no indexed primary publication is
  a register row, with NCT, phase, enrolment, intervention, sponsor, completion date, and what was
  searched.
- A missing result is recorded as **unretrievable**, never as evidence of absence, and never
  inferred from the trial's design, sponsor or termination status.
- **Registry and database coverage is declared** wherever a count is reported: Phase 0 searched
  ClinicalTrials.gov and PubMed only, so all trial counts are a lower bound until EU CTR, jRCT,
  ISRCTN and Chinese registries are searched or the gap is declared.
- Where an unretrievable result bears on an open question, the retrieval attempt is documented so a
  reader can repeat or extend it.

*Enforced by:* the retrievability register; `results_retrievable` and `retrieval_attempted` fields;
a coverage statement accompanying every reported count.

### L6 — Currency and dating (added)

- Every register row and every conclusion carries a **retrieval date** (`retrieval_date`).
- Reviews, guidelines and meta-analyses whose search predates a subsequent readout are marked
  **superseded on this point**, with the superseding source named. As of adoption this applies to
  any synthesis whose search closed before the 2025–2026 readouts (nerandomilast, treprostinil,
  deupirfenidone) and the December 2025 approval.
- Approval and label status is recorded with its date and jurisdiction, never as a timeless fact.
- A statement whose truth depends on the assessment date says so in the row.

*Enforced by:* `retrieval_date` field on every register row; `superseded_by` field on synthesis
rows; dated snapshot citation for the bundle.

---

## Part C — Criteria deliberately NOT fixed here

These require information the record does not yet have. Fixing them now would be a guess presented
as a rule. Each must be **prespecified in the brief of the phase that needs it, before results are
read**, and published with that phase.

| Item | Why it cannot be fixed now | Where it gets fixed |
|---|---|---|
| TCM screening thresholds: minimum treatment duration, minimum sample size, minimum follow-up | Phase 0 did not retrieve the corpus; the distribution of durations and sample sizes in the 295 RCTs is unknown, so any threshold now is arbitrary and could be tuned after seeing results | Phase 2 TCM screening brief, prespecified |
| Whether a formal risk-of-bias tool result gates inclusion or is only reported | Depends on how the corpus scores; a gate set blind could empty the domain | Phase 2 TCM screening brief |
| Which non-English databases are searched versus declared as a gap | Depends on access at the time of Phase 2 | Phase 2, declared either way |
| Curated-intervention inclusion threshold (how far down the 488 registry intervention strings the treatment landscape goes) | Requires the Phase 2 pull to see where the evidence becomes uninformative | Phase 2 brief |
| The evidence bar for grading a row on survival rather than FVC | Phase 1 must first establish the endpoint taxonomy and what the field's mortality evidence actually supports | End of Phase 1, then applied in Phase 2 |
| Whether a quantitative cross-trial comparison of FVC effects is admissible at all, given ~3-fold placebo drift | Requires the Phase 1 endpoint taxonomy | End of Phase 1 |

Anything fixed later under this section is recorded in the phase brief and in
`corrections_log.csv`, so a reader can see it was set before results were read rather than after.

**Status update, 2026-09-02.** All six deferred items are now fixed, before any Phase 2 treatment
effect was read, in `IPF_PHASE2_BRIEF.md`: §1 curated-intervention inclusion tiers I1–I4 (item 4),
§2 the survival-grading bar (item 5), §3 cross-trial FVC admissibility (item 6), §4 the L4
traditional-medicine screening rules — eligibility, tiers T1–T5 in place of numeric thresholds,
risk of bias reported rather than gating, corpus description before grading, and the database
coverage declaration (items 1–3). Entered as C4 in `corrections_log.csv`.
