# Open Therapeutics #002 — Idiopathic Pulmonary Fibrosis: archive

This archive contains a complete open evidence record for idiopathic pulmonary fibrosis: the
research registers it was built from, the derived public data payload, the public summary, and the
QA report on both.

**This is a research record, not medical advice, and it has not been peer reviewed.** Nothing in
it establishes that a treatment is effective, safe or appropriate for any patient.

**The headline result:** 279 interventions graded on one scale; 7 have evidence of benefit, each
on one outcome dimension only; 195 are poorly studied, which is not the same as ineffective; no
drug has randomised survival evidence; and **no research lead was promoted.** Zero leads is the
outcome of the screening, not an unfinished step.

## Layout

```
publication/        the public-facing materials
  OVERVIEW.md            the summary of the record (start here)
  SCHEMA_EXTENSIONS.md   where the public data model extends the reference model, and why
  QA_PUBLIC_DATA.md      the QA report: 85 automated checks + 5 manual checks
data/               the machine-readable payload and the code that builds and checks it
  ipf_record.json        derived single-file payload (schema ipf-public-1.1)
  build_ipf_public_data.py
  qa_ipf_public_data.py
  qa_findings.csv        machine-readable QA results
  qa_counts.json         the automated/manual check split this run produced
research_record/    the canonical research record (source of truth)
  registers/             24 CSV/JSON registers, Phase 0-6
  reports/               8 phase reports
  figures/               9 figures + FIGURES_NOTE.md (phase provenance and superseded values)
```

## What is canonical and what is derived

`research_record/registers/` is the source of truth. `data/ipf_record.json` is a derived view of
those registers and can be rebuilt from them at any time:

```
IPF_DATA=research_record/registers IPF_OUT=data/ipf_record.json python data/build_ipf_public_data.py
IPF_DATA=research_record/registers python data/qa_ipf_public_data.py \
    data/ipf_record.json publication/OVERVIEW.md README.md publication/SCHEMA_EXTENSIONS.md
```

Run from the archive root; `research_record/registers` is also the default value of `IPF_DATA`.
Rebuilding reproduces the shipped payload key-for-key apart from `meta.generated`.

Requires Python 3 with pandas. The build is deterministic apart from the generation timestamp in
`meta.generated`.

The registers are append-only. Later corrections supersede earlier statements: `corrections_log.csv`
holds 38 research-phase corrections (C1–C38), each with what was claimed, what replaced it, the
basis and the effect. Three publication-stage normalisations (PUB-01, PUB-02, PUB-03) are applied in the
derived payload only and are disclosed in `meta.normalisations`; **no research file was rewritten
to suit the published view.**

The phase reports and figures are historical: correct as of the phase that produced them, and in
several cases superseded. `research_record/figures/FIGURES_NOTE.md` lists every superseded value
and where the current one lives. Quote current numbers from `publication/OVERVIEW.md` or
`data/ipf_record.json`, never from a phase figure.

## Publication QA corrections

<!-- qa:historical-start -->
Corrections made at publication stage after the website integration, all confined to publication
artifacts; registers and corrections C1–C38 are unchanged.

| # | what was wrong | what was done |
|---|---|---|
| 1 | this README and `SCHEMA_EXTENSIONS.md` stated 75 automated checks, and the QA report header reported one combined figure (81) mixing automated and manual checks | the report now states the automated and manual counts separately, writes them to `data/qa_counts.json`, and two new checks (H8, H9) fail the run if either document states a count this run did not produce |
| 2 | manual check M3 referred to corrections C39/C40, which never existed — the publication-stage changes are PUB-01/PUB-02 | M3 rewritten; check X2 now asserts the PUB series is self-consistent, disjoint from the corrections log, and that the log still ends at C38 |
| 3 | `meta.canonical_files` and the QA usage text named obsolete register directories (`research/data`, `record_data`) | `canonical_files` is now the list of register files the loader actually read, `meta.source_directory` names `research_record/registers` (also the new `IPF_DATA` default), and checks H1–H3, H9 fail the run on an obsolete path in the payload or the documents |
| 4 | one Chinese-language coverage row claimed, in the present tense, that a product is absent from "the 281-row landscape" — a denominator superseded by C38 (283 rows, 279 distinct interventions) | republished as PUB-03 with the final denominator and the claim unchanged; phase-dated text that reports what a past action examined is left as written and disclosed in `meta.historical_text_note`; checks H5–H6 hold that line |

<!-- qa:historical-end -->

## Reading rules

These are published inside the payload as `meta.reading_rules` because the distinctions are
load-bearing:

1. Slowing decline is not preserving function, is not recovering lost function, is not reversing
   fibrosis, and is not a cure.
2. A lung-function effect is not a demonstrated survival benefit.
3. A prognostic association is not evidence of treatment-effect surrogacy.
4. "Poorly studied" means the evidence needed to judge does not exist — not that the intervention
   was tested and failed.
5. Missing, unreported or inaccessible evidence counts in no direction, including as promise.
6. Registry-only evidence stays identifiable and is not mixed with published evidence.
7. A finding held at verification is a verification state, not a positive result.
8. Every verdict is specific to the outcome dimension named on its row.

A display built on this data must show each statement's evidence grade, must always show its
caveat, and must badge superseded content with a link to the correction. Three treatment-map
statements carry no separate caveat in the record; they are flagged `caveat_status: absent in the
record` so a display cannot present them as caveat-free.

## Scope

Idiopathic pulmonary fibrosis only. Evidence from other fibrotic lung diseases appears only where
it is labelled indirect. Interventions from modern biomedicine, repurposed drugs, abandoned
programmes, supportive care, procedures and traditional medical systems are graded on the same
scale; 14 traditional or historical interventions are in the landscape and none reaches a benefit
verdict — for most, the evidence could not be reached at all. Six English-indexed syntheses of
Chinese-language randomised trials were located and are published as a measured coverage gap
(`ipf_phase6_chinese_language_coverage.csv`): CNKI, Wanfang, VIP and SinoMed are subscription-gated
and the Chinese trial registry refused automated access, so that body of randomised evidence has
not been examined. It is credited with nothing in either direction.

## What would change this record

The release of a completed but unreported genotype-stratified trial; primary full texts for the
four findings held at verification; individual-participant re-analysis of existing trial data for
the FVC-to-survival surrogacy question; and an examination of the Chinese-language randomised
literature by someone with database access. Eight actions remain open and none of them is a
proposal for a new clinical trial.
