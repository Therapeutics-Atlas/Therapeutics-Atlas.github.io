# Figures — phase provenance and superseded values

These figures belong to the research record. Each one is correct **as of the phase that produced
it**, and several were superseded by later corrections. They are kept because the record is
append-only and its working state is part of what is being published.

**Only `ipf_phase6_summary.png` reflects the final counts.** For any current figure quoted in
public materials, the authoritative values are in `publication/OVERVIEW.md` and
`data/ipf_record.json`. Do not publish a figure below without the badge in the last column.

| figure | phase | superseded value shown | current value | where the current value lives |
|---|---|---|---|---|
| `fig1_ipf_therapeutic_ceiling.png` | 0 | trial-level FVC differences as of Phase 0 | unchanged in direction; the ceiling table is the authoritative version | `ipf_phase1_ceiling.csv` |
| `fig2_ipf_stopped_trials.png` | 0 | termination-reason counts for the Phase 0 registry pull | unchanged | `ipf_phase0_stopped_trials.csv` |
| `fig1_ipf_phase1_ceiling.png` | 1 | best cough result "−39.4% at day 14, n=44" | 60.2% highest documented placebo-adjusted reduction in objective cough frequency | `ipf_phase1_ceiling.csv` |
| `fig2_ipf_phase1_retrievability.png` | 1 | 110 of 239 completed trials with no retrievable result | unchanged (239 completed, 90 posted, 149 register rows, 110 unretrievable, 97 past window) | `retrievability_summary` in `ipf_record.json` |
| `fig3_ipf_phase2_landscape.png` | 2 | 281 entities; Works 6, Conflicting 1, Uncertain 43, Failed 8, Harm 8, Poorly studied 215 | 279 distinct interventions; Works 7, Uncertain 51, Failed 17, Harm outweighs benefit 9, Poorly studied 195. The "Conflicting" verdict class was retired; conflicts are carried in the conflicts register instead | `ipf_phase2_landscape.csv`, `vocab.verdict_classes` |
| `fig4_ipf_phase2_tm_screen.png` | 2 | 107 traditional-medicine records by prespecified tier | unchanged; the Phase 6 coverage register adds what could not be reached | `ipf_phase2_traditional_medicine_screen.csv`, `ipf_phase6_chinese_language_coverage.csv` |
| `fig5_ipf_phase3_map.png` | 3 | 75 map statements (S1 7, S2 20, S3 14, S4 10, S5 12, S6 12) | 89 statements (S1 7, S2 26, S3 18, S4 10, S5 16, S6 12) | `ipf_phase3_treatment_map.csv` |
| `fig6_ipf_phase4_screening.png` | 4 | 33 candidates screened, 2 held at verification, 9 actions carried | 41 candidates screened, 4 held at verification, 12 actions of which 8 open | `ipf_phase4_candidate_register.csv`, `leads_outcome` in `ipf_record.json` |
| `ipf_phase6_summary.png` | 6 | — | current | `ipf_record.json` |

The Phase 6 corrections that moved these numbers are C24–C38 in `corrections_log.csv`, each with
the claim corrected, what replaced it, the basis and the effect.
