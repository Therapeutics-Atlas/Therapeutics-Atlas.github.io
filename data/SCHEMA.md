# `ra_record.json` — schema for site consumption

One file, ~270 KB, UTF-8. It is a **derived view** of the CSVs in this directory, built by
`build_api.py`; the CSVs and the phase reports remain canonical. If the two disagree, the CSVs win.
No backend is required — a static site can fetch this and do everything client-side.

## Top-level keys

| Key | Rows | Contents |
|---|---|---|
| `meta` | — | disease, generated date, schema version, disclaimer, licence, counts, `peer_reviewed: false` |
| `vocab` | — | facet values with counts: `sections`, `evidence_tiers`, `verdict_classes`, `domains`, `unmet_needs`, `evidence_levels` |
| `map` | 115 | the treatment map, one statement per row |
| `interventions` | 67 | the graded intervention register |
| `negatives` | 17 | negative-results register |
| `conflicts` | 9 | preserved conflicts (`side_a`, `side_b`, `status`) |
| `leads` | 6 | research leads, with `steps`, `verification_checks` and `corrections` nested |
| `corrections` | 9 | corrections log, linked to what it corrects |
| `triage` | 22 | all lead candidates and why each was rejected or promoted |
| `public_record_check` | 14 | per-source result of the access check on the two open leads |
| `open_questions` | 10 | baseline open questions |
| `references` | 77 | bibliography with resolved `url` |

## Identifiers

Stable and safe to use in URLs (`/statement/TM-042`): `TM-001…115` (map), `IV-001…067`
(interventions), `NEG-`, `CF-`, `PRC-`, `OQ-`, `REF-001…077`. Leads, corrections, steps and triage
rows keep their own project ids (`RL-01`, `C1`, `V6`, `RL-01-A`, and the triage `key`).

Ids are assigned by row order at build time. They are stable as long as the CSVs are appended to
rather than reordered — if you reorder a CSV, previously published deep links break. Treat that as
a release constraint.

## `refs` vs `ref_candidates` — do not merge these

- **`refs`** — identifiers extracted verbatim from the row's own source field, as
  `{type, id, url}` with `type` in `pmid`, `doi`, `nct`, `isrctn`, `euctr`, `ntr`. These are
  citations. 37 of 115 map rows and all 67 intervention rows have them.
- **`ref_candidates`** — present only where `refs` is empty. The map's `source` column holds short
  human labels ("TwHF meta-analysis", "Cochrane acupuncture"), so these are **token matches**
  against intervention names and reference titles, each carrying `matched_on`. They are
  *possible* sources, not verified attributions. 70 of 115 map rows have them.

A UI must render the two differently — `refs` as a citation link, `ref_candidates` as "possible
source" — because a token match can be wrong, and presenting one as a citation would put a claim
next to a source that does not support it. 8 map rows have neither and must show their raw `source`
label as-is.

## Display obligations

These are not styling preferences; they are what keeps the site an evidence record.

1. **Never show a statement without its `evidence_tier`** (map) or `verdict_class` (interventions).
   A bare claim stripped of its grade is a misrepresentation of this dataset.
2. **Show `caveat` wherever it is non-null.** It exists because the effect as reported is not
   credible, and it is the row's most important field when present.
3. **Badge superseded content.** Every `corrections` row carries `corrects_lead` and
   `corrects_phase`; the archived phase reports in `phases/` contain statements this project has
   retracted. Any view that surfaces phase-report text must link the corrections log.
4. **Surface `meta.disclaimer` on every page**, not only a landing page — deep links mean any page
   can be someone's first.
5. **Do not build symptom-to-treatment lookup, ranking, or "what should I take" flows.** The
   dataset does not support them and the framing converts a record into advice.
6. `evidence_tier` may carry a parenthetical sub-label (`Uncertain (same trial, opposite
   readings)`). Facet on the part before the bracket; display the whole string.

## Rebuilding

`python build_api.py` → `build(outfile="ra_record.json")`. The builder omits fields it cannot
derive rather than guessing, and normalises `—`/`n/a` placeholders to `null`.
