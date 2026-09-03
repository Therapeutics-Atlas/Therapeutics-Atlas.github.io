# Schema extension note — IPF public data payload

**Payload:** `ipf_record.json` (`meta.schema_version = "ipf-public-1.1"`) · **Reference model:**
the rheumatoid-arthritis public data model (`ra_record.json`, `SCHEMA.md`)

The first record in this series established the public data model. This note records where the IPF
payload follows it, where it extends it, and why each extension was necessary rather than
cosmetic. The rule applied throughout: **structural uniformity gives way to scientific fidelity.**
An extension was added only where the IPF research record holds a state that the reference model
has no field for, and where dropping that state into an existing field would have published a
claim the record does not make.

## 1. What is unchanged

- **The registers are canonical; the payload is derived.** `ipf_record.json` is rebuilt from the
  Phase 0–6 CSV/JSON registers by `build_ipf_public_data.py`. The payload is a view, not a source.
  `meta.canonical_files` lists the registers it was built from.
- **Row-order identifiers are a published interface.** `TM-###`, `IV-###`, `NEG-###`, `CF-###`,
  `CAND-###`, `ACT-###`, `COR-###` are assigned by register row order and are stable across
  rebuilds as long as the registers are append-only.
- **Grades travel with statements.** No statement is published without its evidence tier; no
  intervention row without its verdict class and the sublabel stating what the verdict rests on.
- **Verbatim source text and derived text are separate fields.** `sources_verbatim`,
  `key_result_verbatim` and `safety` carry extracted source text; everything else is curated.
- **Corrections supersede.** `corrections` is append-only, and a corrected row carries the
  correction id (`superseded_by`, or the correction id inside `curation_note`).
- **No heuristic citations.** The reference builder produced token-matched "possible sources"
  alongside verified ones. That mechanism is deliberately not carried over: the IPF payload
  publishes a citation only where the research record states one. `references` therefore has no
  candidate/suggested tier, and 24 of 153 references carry `title: null` with
  `title_source: null`, because the record does not contain their titles. Nothing was fetched or
  inferred to fill them.
- **Display obligations inherited unchanged:** every statement shows its grade; caveats always
  show; superseded content is badged and linked to its correction; no symptom-lookup flow and no
  "top treatments" ranking is built from this data.

## 2. Extensions, and the record state each one exists to carry

### 2.1 `interventions[].evidence_access` — new closed vocabulary (required extension)

The IPF record distinguishes three access states that the reference model collapses into "graded /
not graded". Publishing them as one state would have made registry-only evidence indistinguishable
from peer-reviewed evidence, and would have made "no result was ever retrieved" look like "the
result was weighed".

| value | n | meaning |
|---|---|---|
| `published result` | 101 | graded on a located publication |
| `registry posting only, or posted result that cannot be graded` | 23 | outcome tables exist on the registry; some have no between-arm analysis at all |
| `no IPF-specific human result retrieved` | 155 | nothing to grade was found |

This field is required on every intervention row, and QA check D6 enforces it.

### 2.2 `interventions[].is_duplicate` / `duplicate_of` (required extension)

Phase 6 identified four landscape rows as duplicates of another row. The registers are
append-only, so the rows were not deleted. The payload publishes all 283 rows, flags 4, and
reports both `interventions_published` (283) and `interventions_distinct` (279). Every derived
count and every figure uses the distinct set. A display should exclude flagged rows from counts
and lists.

### 2.3 `map[].caveat_status` (required extension)

Three treatment-map statements (`TM-076`–`TM-078`) carry no separate caveat field in the research
record. The display obligation is that caveats always show, so a null caveat cannot be published
silently. `caveat_status` states either `stated in the record` or `absent in the record — the
statement's own qualifications are the only ones recorded`. Nothing was written into the empty
caveats. QA notes this as G2b.

### 2.4 `therapeutic_ceiling` — new section (required extension)

Twelve therapeutic dimensions, each with the best documented result, its evidence tier, and what
remains unachieved. This is the section that keeps *slowing decline* separate from *preserving
function*, *recovering lost function*, *reversing fibrosis*, *survival* and *cure*. The reference
model has no slot for it, and without it the IPF record's central finding — that the ceiling sits
at slowing decline — is not representable.

### 2.5 `endpoint_taxonomy` and `measurement_gaps` — new sections (required extension)

`endpoint_taxonomy` (15 rows) carries, per endpoint, what it licenses and, in a separate field,
what it explicitly **does not** license (`does_not_license`), plus its prognostic anchor. This is
where the prognostic-association / treatment-effect-surrogacy distinction lives as data rather
than prose. `measurement_gaps` (5 rows) holds candidate endpoints for dimensions that currently
have no validated measure, each with its smallest validation step. Both are needed because two of
the twelve unmet needs cannot be tested at all until an endpoint exists.

### 2.6 Retrieval and access registers — new sections (required extension)

`retrievability` (149 completed trials), `registry_results_sweep` (116 trials with posted
results), `located_publications` (8 rows) and `coverage_gaps` (6 rows), plus a derived
`retrievability_summary`. The reference record had no comparable body of unreachable evidence.
These sections exist so that missing and inaccessible evidence is published as a measured gap. The
reading rules state that none of it counts in any direction.

### 2.7 `screens` + `candidates` in place of leads, and an explicit `leads_outcome`

The reference model publishes research leads with the candidates that failed screening as
supporting detail. The IPF record promoted **zero** leads, so an empty `leads: []` alone would
read as an unfinished record. The payload therefore publishes:

- `leads: []` and `counts.research_leads: 0`;
- `leads_outcome`, an object stating the zero-lead result in words, with the breakdown:
  41 screened, 4 held at verification, 37 rejected, of which 6 were rejected as leads with a
  retrieval, analysis or measurement action retained;
- `candidates[]` with `status` (`rejected` / `held at verification` / `rejected as a lead, action
  retained`, from the register's own outcome vocabulary), `screens_failed`, `reason`, `action_retained`, and `promoted_to_lead: false` on
  every row;
- `screens[]`, the six prespecified screen definitions, so a reader can see the bar that was
  applied.

`status: held at verification` is a verification state, not a positive finding. QA checks L1–L6
enforce the zero-lead outcome, the held/rejected labelling, and that every candidate carries a
final status and a reason.

### 2.8 `actions[].type` and `actions[].open`

Actions are typed `retrieval` / `analysis of existing data` / `measurement development`, and none is a
proposal for a new clinical trial. The typing is load-bearing: it is what keeps an unresolved
retrieval or measurement problem from being read as a therapeutic hypothesis.

### 2.9 `meta.reading_rules` and `meta.normalisations`

`reading_rules` publishes, inside the payload, the eight distinctions a display must not blur
(slowing ≠ preserving ≠ recovering ≠ reversing ≠ curing; lung-function effect ≠ survival benefit;
prognostic association ≠ treatment-effect surrogacy; poorly studied ≠ ineffective; missing or
inaccessible ≠ promising; registry-only stays identifiable; held stays held). A consumer of the
data receives the rules with the data.

`normalisations` records the three publication-stage changes, which are applied in the derived
payload only and did not touch any research file:

- **PUB-01** — two intervention rows carried the verdict label `Poorly studied` in the
  evidence-tier column; published as tier `Unknown`, the tier that verdict class uses throughout,
  with `evidence_tier_sublabel` marked `normalised at publication (PUB-01)`.
- **PUB-02** — six internal treatment-map identifiers (`M2.13`–`M2.18`) were each used by two
  rows, an artefact of statements added in later phases. The payload assigns stable `TM-###`
  identifiers by row order and preserves the original in `internal_map_id`.
- **PUB-03** — one Chinese-language coverage row made a present-tense claim against a superseded
  landscape size (`the 281-row landscape`, the count recorded in corrections C31 and C33). The
  denominator is republished as the final one established by C38 (283 rows, 279 distinct
  interventions); the claim itself — that the intervention is absent from the landscape — is
  unchanged. Phase-dated text that reports what a past action examined is left as written and is
  disclosed instead in `meta.historical_text_note`.

These are deliberately numbered in a separate `PUB-` series rather than continuing the research
corrections log (which ends at C38), so that publication-stage bookkeeping is never mistaken for a
correction to the research record.

### 2.10 `meta.canonical_files`, `meta.source_directory` and `meta.historical_text_note`

`canonical_files` is a list of the register filenames the build actually consumed, appended by the
loader itself rather than typed by hand, so it cannot drift from the build. `source_directory`
names the archive-relative register directory (`research_record/registers`), which is also the
default value of `IPF_DATA`. `historical_text_note` discloses that phase-dated text quotes the
landscape size as it stood in that phase (281 rows / 278 distinct in corrections C31 and C33 and
in two Phase 4 rows), superseded by C38 (283 / 279), so a display does not read a historical
account of past work as a current count. Schema version `1.1` marks these three fields: `1.0`
published `canonical_files` as a single sentence and had no source directory or historical note.

## 3. Sections carried over unchanged in shape

`map`, `interventions`, `negatives`, `conflicts`, `corrections`, `limitations`, `unmet_needs`,
`open_questions`, `vocab`, `counts`, `references`. Field names follow the reference model where a
matching field existed.

## 4. Rebuild and verification

```
IPF_DATA=<registers dir> IPF_OUT=ipf_record.json python build_ipf_public_data.py
IPF_DATA=<registers dir> python qa_ipf_public_data.py ipf_record.json OVERVIEW.md
```

The QA script runs 85 automated checks over the payload and the Overview and writes
`QA_PUBLIC_DATA.md` and `qa_findings.csv`. Checks that cannot be automated are listed as manual
checks with their result rather than reported as passing.
