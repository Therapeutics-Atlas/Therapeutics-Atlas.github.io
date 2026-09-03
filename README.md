# Open Therapeutics #001 — Rheumatoid Arthritis

An open, checkable record of what is known, disputed, and untested about treating rheumatoid
arthritis — including the interventions that do **not** work, and the questions nobody has asked
in a form that could answer them.

This is not a review article and not medical advice. It contains no treatment recommendation and
no claim that any intervention works. It is a **map with its sources attached**, built so that
someone else can check it, disagree with a specific row on stated grounds, or continue it.

**Status:** phases 1–6 complete. Two research leads remain open; both are blocked on discretionary
access to data held by other groups, not on further literature work. Nothing here has been peer
reviewed.

---

## Start here

| If you want to | Read |
|---|---|
| A three-page overview | `SUMMARY.md` |
| The map itself, as data | `data/treatment_map.csv` |
| What has been shown *not* to work | `data/negative_results_register.csv` |
| Where credible sources disagree | `data/conflicts_register.csv` |
| The two open leads and their current footing | `data/research_leads_status.csv` |
| What this project got wrong and corrected | `data/corrections_log.csv` |
| How evidence was graded | `docs/evidence_grading.md` |
| What happens next, and who it depends on | `docs/next_steps_and_dependencies.md` |
| The full reasoning trail, dated | `phases/` |
| To read the record from code or a website | `data/ra_record.json` + `data/SCHEMA.md` |
| To browse it in a browser | `site/` — serve the folder, no build step |

## What is in here, in numbers

- **67 interventions** across 12 domains (modern, historical, repurposed, supplements, TCM herbal
  and non-herbal, acupuncture, mind–body, lifestyle) with a verdict class, the strongest available
  evidence design, a verbatim key result, and PMID/DOI — `data/intervention_register.csv`
- **115 mapped statements** in six sections: what works (17), what does not work (19), what is
  uncertain (22), what we know about the disease (22), what we do not know (13), and what might be
  worth studying (22) — `data/treatment_map.csv`
- **17 preserved negative results** — `data/negative_results_register.csv`
- **9 preserved conflicts**, kept unresolved where the evidence does not resolve them —
  `data/conflicts_register.csv`
- **9 documented corrections** to this project's own earlier statements — `data/corrections_log.csv`
- **77 references** with identifiers — `data/references.csv`
- **10 open questions** carried from the baseline review — `data/open_questions.csv`

## How it was built

Six sequential phases, each written before the next began, and each preserved unedited in
`phases/`:

1. **Evidence baseline** — what RA is, how it is treated, and where current treatment reaches its
   ceiling.
2. **Treatment landscape** — 67 interventions from all traditions, graded on the same scale, with
   negative results and conflicts recorded rather than dropped.
3. **Open treatment map** — the landscape reorganised into what we know, what we do not, and what
   might be worth studying.
4. **Research leads** — 22 candidate signals triaged; six promoted, sixteen rejected with reasons
   recorded.
5. **Deep investigation, then targeted verification against primary full texts** — three leads
   survived stage one; verification then reframed one, narrowed one, and downgraded one.
6. **Next steps** — the smallest analysis that could resolve each remaining lead, and a
   public-record check establishing whether it can be executed without contacting the original
   teams. It cannot.

Retrieval and drafting were AI-assisted under human direction. Every load-bearing claim was traced
to a primary record and carries a PMID, DOI, or registry identifier. Secondary summaries were not
treated as evidence. Where full text was read, statements are quoted rather than paraphrased.

## Working rules this record follows

1. Do not assume the answer. TCM is not assumed to work; modern medicine is not assumed superior.
2. AI does not declare that a treatment works. Efficacy requires clinical validation.
3. **Negative results are results.** They are collected deliberately, not as a by-product.
4. Levels of evidence are kept separate: human RCT, observational, case report, animal, in vitro,
   mechanistic, traditional record, hypothesis.
5. Traditional medicine is a source of hypotheses, not assumed truth. No claim depends on qi,
   meridians, or yin–yang being biologically real.
6. Phenomenon first, mechanism later — but absence of a mechanism is not evidence of an effect.
7. Uncertainty is stated. Where studies disagree, both are shown; where evidence is insufficient,
   the record says so.
8. Corrections are made in public. Nothing is silently revised.

## What is deliberately not here

- Any recommendation, dosing guidance, or claim of efficacy.
- Unsent correspondence with other research groups.
- Anything that would identify a patient or research participant. The record contains no
  individual-level data of any kind.
- A ranking of the open leads. They address different populations with different evidence types;
  ordering them would imply a comparison the evidence does not support.

## Known limitations

- **Retrieval is the main failure mode.** Three of the nine corrections in this record are cases
  where an apparent research gap turned out to be a gap in the search strategy. Others almost
  certainly remain. If you find one, it is a genuine contribution.
- Coverage of non-English and pre-1980 literature is thin, which matters most for historical and
  traditional interventions.
- No meta-analysis was performed. Effect sizes are reported as their sources reported them, which
  is why `data/intervention_register.csv` carries a `caveat` column.
- Verdict classes are judgements about evidence, not about biology, and are open to dispute. The
  grading scheme is written out in `docs/evidence_grading.md` so a disagreement can be located.

## Figures

`figures/` — treatment ceiling of current therapy; landscape by domain and by unmet need; reported
effect size against evidence quality; the open map; lead triage; evidence chains per lead; the
verification result per claim; and the proposed next steps.

## Continuing this work

The most useful contributions, in order: a missed primary record that changes a row; a negative
result not yet in the register; a correction to a verdict with a stated reason; an answer to either
open lead's blocking question. Each is a change to a specific line of a specific file.

## Reuse

Licence: *to be chosen by the author before publication.* CC BY 4.0 for text and data is the
conventional choice for a record intended to be reused and corrected.

Cite as a dated snapshot; the corrections log is the reason the date matters.
