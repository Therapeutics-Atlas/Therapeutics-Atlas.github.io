# IPF public data — QA report

**Date:** 2026-09-03 · **Payload:** `ipf_record.json` · **Automated checks:** 85 (note 4, pass 81) · **Manual checks:** 5

Every automated check re-runs with `IPF_DATA=research_record/registers python qa_ipf_public_data.py ipf_record.json OVERVIEW.md`. Checks that cannot be automated are listed as manual with their result. A `note` is a disclosed property of the data, not a defect.

## row fidelity

| id | check | result | detail |
|---|---|---|---|
| F1 | map: published rows == source rows (ipf_phase3_treatment_map.csv) | pass | source 89, published 89 |
| F2 | interventions: published rows == source rows (ipf_phase2_landscape.csv) | pass | source 283, published 283 |
| F3 | negatives: published rows == source rows (ipf_phase2_negative_results_register.csv) | pass | source 77, published 77 |
| F4 | conflicts: published rows == source rows (ipf_phase2_conflicts_register.csv) | pass | source 12, published 12 |
| F5 | candidates: published rows == source rows (ipf_phase4_candidate_register.csv) | pass | source 41, published 41 |
| F6 | corrections: published rows == source rows (corrections_log.csv) | pass | source 38, published 38 |
| F7 | actions: published rows == source rows (ipf_phase4_actions.csv) | pass | source 12, published 12 |
| F8 | limitations: published rows == source rows (ipf_phase4_limitations.csv) | pass | source 7, published 7 |
| F9 | unmet_needs: published rows == source rows (ipf_phase1_unmet_needs.csv) | pass | source 12, published 12 |
| F10 | open_questions: published rows == source rows (ipf_phase0_open_questions.csv) | pass | source 10, published 10 |
| F11 | therapeutic_ceiling: published rows == source rows (ipf_phase1_ceiling.csv) | pass | source 12, published 12 |
| F12 | endpoint_taxonomy: published rows == source rows (ipf_phase1_endpoint_taxonomy.csv) | pass | source 15, published 15 |
| F13 | retrievability: published rows == source rows (ipf_phase1_retrievability_register.csv) | pass | source 149, published 149 |
| F14 | registry_results_sweep: published rows == source rows (ipf_phase6_registry_results_sweep.csv) | pass | source 116, published 116 |
| F15 | located_publications: published rows == source rows (ipf_phase6_missing_results_retrieval.csv) | pass | source 8, published 8 |
| F16 | measurement_gaps: published rows == source rows (ipf_phase6_recovery_endpoints.csv) | pass | source 5, published 5 |
| F17 | coverage_gaps: published rows == source rows (ipf_phase6_chinese_language_coverage.csv) | pass | source 6, published 6 |

## identifiers

| id | check | result | detail |
|---|---|---|---|
| ID-TM | map: ids unique and prefixed TM- | pass | 89 unique of 89 |
| ID-IV | interventions: ids unique and prefixed IV- | pass | 283 unique of 283 |
| ID-NEG | negatives: ids unique and prefixed NEG- | pass | 77 unique of 77 |
| ID-CF | conflicts: ids unique and prefixed CF- | pass | 12 unique of 12 |
| ID-INT | internal treatment-map ids: collisions disclosed in meta.normalisations | pass | collided internal ids: ['M2.13', 'M2.14', 'M2.15', 'M2.16', 'M2.17', 'M2.18'] |

## grading

| id | check | result | detail |
|---|---|---|---|
| G1 | every map statement carries an evidence tier | pass | [] |
| G2 | every map statement either carries a caveat or is flagged caveat-absent | pass | [] |
| G2b | map statements with no caveat field in the research record | note | 3 statements (['TM-076', 'TM-077', 'TM-078']) carry no separate caveat in the record; caveat_status marks them so a display cannot present them as caveat-free |
| G3 | every map statement carries an outcome dimension | pass | [] |
| G4 | map tiers come from the closed tier vocabulary | pass | [] |
| G5 | intervention verdicts come from the closed verdict vocabulary | pass | [] |
| G6 | intervention tiers come from the closed tier vocabulary (after PUB-01 normalisation) | pass | [] |
| G7 | every graded verdict carries a sublabel stating what it rests on | pass | [] |
| G8 | every Works verdict names the outcome dimension it was graded on | pass | [] |
| G9 | every Works verdict carries a verbatim key result | pass | [] |

## distinctions

| id | check | result | detail |
|---|---|---|---|
| D1 | no drug carries a survival claim; survival evidence is transplantation only and observational | pass | rows with survival wording: ['lung transplantation'] |
| D2 | the record states in 'what we do not know' that no drug has randomised survival evidence | pass | ['TM-054', 'TM-057', 'TM-085', 'TM-089'] |
| D3 | every 'what works' statement is caveated against preservation, recovery, reversal and cure | pass | [] |
| D4 | the unresolved FVC-to-survival surrogacy question is published as a statement | pass | ['TM-057'] |
| D5 | 'poorly studied' rows are never described as ineffective | pass | [] |
| D6 | registry-only and unretrieved evidence states are identifiable on the row | pass | 178 of 279 rows not published-result |
| D7 | no traditional-medicine intervention is graded Works | pass | [] |

## research leads

| id | check | result | detail |
|---|---|---|---|
| L1 | leads list is empty | pass | [] |
| L2 | counts.research_leads is 0 | pass |  |
| L3 | no candidate is marked promoted | pass | [] |
| L4 | held candidates are labelled held, not rejected and not promoted | pass | 4 held |
| L5 | every candidate carries a final screening status and a reason | pass | [] |
| L6 | every screen referenced by a candidate is defined | pass | [] |

## corrections

| id | check | result | detail |
|---|---|---|---|
| X1 | every correction id cited by a published row exists in the corrections log | pass | [] |
| X2 | publication-stage normalisations are disclosed in meta, use their own id series, and do not extend the research log | pass | ['PUB-01', 'PUB-02', 'PUB-03']; corrections log ends at C38 |
| X3 | interventions regraded by the Phase 6 registry sweep carry the corrected verdict | pass | [] |

## references

| id | check | result | detail |
|---|---|---|---|
| R1 | every inline citation appears in the reference index | pass | [] |
| R2 | every PubMed, registry and DOI reference resolves to a URL | pass | [] |
| R3 | identifier syntax is valid | pass | [] |
| R4 | no heuristically token-matched 'possible source' is published as a citation | pass | the IPF payload publishes only citations stated in the record |
| R5 | references without a title inside the record are marked, not invented | note | 24 of 153 references have no title in the record; title_source is null for those |

## counts

| id | check | result | detail |
|---|---|---|---|
| N1 | counts.interventions_distinct equals non-duplicate rows | pass | 279 vs 279 |
| N2 | counts.conflicts_unresolved equals unresolved conflict rows | pass |  |
| N3 | counts.references equals the reference index length | pass |  |
| N4 | retrievability summary matches the register | pass | unretrievable 110 vs 110; register 149 vs 149 |

## overview arithmetic

| id | check | result | detail |
|---|---|---|---|
| O1 | Overview figure matches the data ((\d+) interventions were graded) | pass | overview 279, data 279 |
| O2 | Overview figure matches the data (Only (\d+) of \d+ interventions have evidence of benefit) | pass | overview 7, data 7 |
| O3 | Overview figure matches the data (\*\*(\d+) are poorly studied) | pass | overview 195, data 195 |
| O4 | Overview figure matches the data ((\d+)\s+graded statements) | pass | overview 89, data 89 |
| O5 | Overview figure matches the data ((\d+)\s+corrections) | pass | overview 38, data 38 |
| O6 | Overview figure matches the data ((\d+) candidate signals) | pass | overview 41, data 41 |
| O9 | Overview figure matches the data (\*\*(\d+) are held at verification\*\*) | pass | overview 4, data 4 |
| O10 | Overview figure matches the data ((\d+) were rejected) | pass | overview 37, data 37 |
| O7 | Overview states zero research leads | pass |  |
| O8 | Overview carries the disclaimer | pass |  |

## public language

| id | check | result | detail |
|---|---|---|---|
| P1 | no unqualified efficacy, cure or recommendation language in the Overview | pass | [] |
| P2 | no promotional language in the payload outside quoted source text | pass | [] |
| P2b | promotional wording inside verbatim quoted source text | note | 1 occurrence(s) inside quoted fields, which a display must render as quotation: ['safety: The PD programme is safe and effective as a rehabilitation intervention'] |
| P3 | payload carries a disclaimer and reading rules | pass |  |
| P4 | payload states that the record is not peer reviewed | pass |  |

## coverage

| id | check | result | detail |
|---|---|---|---|
| C1 | every unmet-need code cited by a map statement is defined | pass | [] |
| C2 | unmet needs with no map statement are reported, not hidden | note | unlinked: [] |
| C3 | every limitation carries scope and detail | pass |  |
| C4 | open actions are published with their Phase 6 outcome | pass | open: ['A1', 'A2', 'A4', 'A6', 'A8', 'A10', 'A11', 'A12'] |

## publication hygiene

| id | check | result | detail |
|---|---|---|---|
| H1 | payload carries no obsolete register path | pass | none |
| H2 | meta.canonical_files lists real register files the build read | pass | 19 entries, missing [] |
| H3 | meta.source_directory names the archive register directory | pass | research_record/registers (archive layout); set IPF_DATA to override |
| H4 | publication-stage normalisations use the PUB series and are all recorded | pass | ['PUB-01', 'PUB-02', 'PUB-03'] |
| H5 | superseded landscape denominator survives only in phase-dated historical text | pass | none outside corrections/actions/limitations; disclosed in meta.historical_text_note |
| H6 | meta.historical_text_note discloses the phase-dated count difference | pass | Phase-dated text quotes the landscape size as it stood in that phase. Corrections C31 and C33 and two Phase 4 rows (an a |
| H7 | schema_version is set and matches the documented value | pass | ipf-public-1.1 (extends the rheumatoid-arthritis public model) |

## documents

| id | check | result | detail |
|---|---|---|---|
| H8 | README and schema note state this run's automated and manual check counts | pass | 2 documents checked against 85 automated + 5 manual |
| H9 | documents carry no obsolete register path outside passages that document the correction | pass | 2 documents clean |

## manual

| id | check | result | detail |
|---|---|---|---|
| M1 | Overview section structure follows the rheumatoid-arthritis Overview (same sections, same depth), with IPF-specific sections added where the record holds a state the RA model has no slot for | pass | pass - RA SUMMARY.md read and mirrored; added sections: therapeutic ceiling by dimension, evidence that exists but cannot be graded, evidence coverage limits |
| M2 | no new research was performed for publication: no new literature search, no new candidate, no new lead | pass | pass - all published values are derived from the Phase 0-6 registers; the builder reads CSVs only |
| M3 | no historical research file was rewritten to suit the public materials | pass | pass - the three publication-stage normalisations (PUB-01, PUB-02, PUB-03) are recorded in meta.normalisations and applied in the derived payload only; the research corrections log still ends at C38 and no register file was edited |
| M4 | held findings are presented as held, and no unresolved retrieval or measurement issue is presented as a therapeutic hypothesis | pass | pass - candidates carry status and screens_failed; actions carry type retrieval/analysis/measurement |
| M5 | Traditional Chinese Medicine coverage is presented as a coverage limit, not as a verdict on efficacy | pass | pass - coverage_gaps and limitation L7 published; no traditional intervention graded Works |
