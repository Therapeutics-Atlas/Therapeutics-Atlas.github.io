# What happens next, and what it depends on

Both open leads need an **analysis of data that already exists**. Neither justifies a new clinical
trial at this stage, and the record states that explicitly rather than defaulting to "further
research is needed". Both are blocked on discretionary access held by other groups. That is an
access problem, not a scientific one, and it is the reason this record is published in its current
state rather than held until the questions are closed.

Structured detail, including the strengthen/falsify criteria and the known barriers for each step,
is in `data/next_steps_specification.csv`. The result of checking whether each step can be executed
from public information alone is in `data/public_record_check.csv`.

---

## RL-01 — is MRI inflammatory burden predictive or prognostic?

**The step.** Apply the published MRI treatment-response definition to the **placebo arm** of the
interception trial, and test the treatment-by-baseline-burden interaction in the randomised
population. The published analysis used the treated arm only, which cannot separate a differential
drug effect from regression to the mean or from spontaneous resolution of subclinical inflammation.

**Why this is the smallest sufficient step.** The trial contains its own comparator and no other
dataset does. Three summary numbers would materially change the lead's status; the full
participant-level dataset is not required for the first pass.

**Specification.** `docs/analysis_spec_placebo_comparator.md`, written to be executable by the
original team without data transfer, and published before any data were requested so that the
hypothesis and the falsification criterion are on the record in advance.

**Access.** The publications document a discretionary, case-by-case route through the corresponding
author, described in the data-sharing statements of the primary and long-term follow-up papers. The
trial protocol's own data-availability clause is narrower and names no third-party route. **No
repository deposit exists**, so there is no route that does not depend on the original team's
consent. The public-record check confirmed this; the access route was not exercised as part of
building this record.

**What would change the lead's status.** An interaction clearly present, with a placebo-arm positive
predictive value substantially below the published 77–79%, would strengthen it and make an
imaging-selected interception trial a defensible question. Similar predictive values in both arms
with an interaction centred on the null would show the marker is prognostic for MRI improvement
generally, and the lead should then be closed. With 13 events in the index stratum, an
uninformatively wide interval is a realistic third outcome, and the placebo-arm proportions remain
interpretable in that case.

**Constraints on the analysis, recorded in advance.** The analysis must be preregistered because the
original signal was post-hoc; risk category and MRI burden are collinear, so the model must use
continuous burden; and power is limited by event count, not by sample size.

---

## RL-02 — two separable questions

**Step A: a records question.** Did the planned single-arm efficacy stage of the CDK-inhibitor
phase 1b trial ever enrol participants or produce results? The registry shows the trial closed with
15 enrolled against a target of 39, an overall end date of 31 December 2023, and links only the
phase 1b paper — which itself described the efficacy evaluation as ongoing. The funder record is
closed and lists only the phase 1b, protocol and analysis-plan papers. The European register does
not display the trial, and the exemption that explains its absence is documented. The health
authority summary is an application-stage record with no outcome section.

**Every public source that could answer this has been checked and none does.** Whether the stage
enrolled is not recoverable from the public record; only the trial team can answer it. A factual
records enquiry is the only remaining route, and an answer of "the stage never enrolled a
participant" would be as useful as any other, because at present the direction can be misread
either as untested or as failed when neither may be true.

**Step B: a validation question.** Define a drug-agnostic stromal score in one existing synovial
biopsy cohort and apply it unchanged to the other. If it predicts non-response across two or more
distinct drug classes, "stromal-high" is a transferable endpoint; if the association is confined to
one drug or fails to transfer, it is a restatement of "B-cell-poor" and the lead narrows to the
point of collapse.

**Access and its limits.** Both cohorts come from one research group, so cross-cohort transfer is
only partial independence — a caveat that cannot be removed with these datasets. One cohort exposes
an interactive interface with raw data by request; the other's raw data sit in a non-public
repository. **What those interfaces actually expose has not been verified**, and it should not be
assumed; establishing it may require a separate enquiry to that group. Per-drug arms in both cohorts
are small, which leaves little power for a multidrug-resistant subset.

---

## For anyone continuing this work

The two enquiries above are the whole of the immediate critical path, and neither requires
specialist resources — only a reply. If you are in a position to answer either question directly,
that is worth more to this record than any additional literature search.

Beyond that, the highest-value contributions are a missed primary record that changes a row, a
negative result absent from the register, or a verdict you can show to be wrong with a stated
reason. The corrections log exists to be added to.
