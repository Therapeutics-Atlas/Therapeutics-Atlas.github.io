# IPF Phase 2 — Treatment Landscape

Open Therapeutics / Open Evidence Record. Disease: idiopathic pulmonary fibrosis (IPF).
Search and grading date: 2026-09-02. Bound by `IPF_SCOPE.md` limits L1–L6 and by the prespecified
rules in `IPF_PHASE2_BRIEF.md`. **No Research Leads are generated or ranked in this phase.**

---

## 1. What was prespecified before any treatment effect was read

`IPF_SCOPE.md` Part C left six criteria unfixed. All six were written into `IPF_PHASE2_BRIEF.md`
before the first effect estimate was retrieved, and the fact that the rules preceded the results is
recorded as corrections entry C4:

1. **Inclusion (I1–I4)** — tiered inclusion over the whole registry intervention universe instead of a
   rank cutoff, so nothing is dropped for being obscure; entities with no retrieved human outcome
   evidence are graded `Poorly studied` rather than deleted.
2. **Survival rule** — no lung-function, imaging or composite result may be graded on the survival
   dimension. This is why no drug in this landscape carries a survival claim.
3. **Cross-trial comparison of FVC** — inadmissible as a quantitative comparison between programmes.
4. **Traditional-medicine eligibility and tiering (T1–T5)** — evidence tiers, not a numerical threshold,
   because no single cutoff was methodologically justifiable from Phase 0 or Phase 1.
5. **Risk of bias caps a verdict; it never gates inclusion.** A high-risk randomised trial stays in the
   record at a lower tier.
6. **Corpus distribution is described before grading** — the step a threshold would have skipped.

## 2. Corpus and search accounting

| item | count |
|---|---|
| intervention entities after normalisation and merging | 281 |
| entities with at least one registry trial | 265 |
| per-entity PubMed searches run | 311 |
| structured extractions from abstracts | 365 |
| traditional-medicine screen records | 107 |
| landscape rows carrying an explicit curation note | 25 |

Databases searched: PubMed/MEDLINE and the ClinicalTrials.gov API v2. **Not searched:** CNKI, VIP,
Wanfang, SinoMed, Embase, CENTRAL, EU-CTR, jRCT, CTRI, ChiCTR directly. Every count below is therefore
a floor, not a complete account — most consequentially for the traditional-medicine domain (see §6).

## 3. The landscape

![Landscape by verdict and evidence tier]({/Users/wangxiaowen/.claude-science/orgs/5d2b56b1-a3ac-45a3-bad2-5aa0b8b074d5/artifacts/proj_06ead86ec16d/69fd14a8-95d2-441e-8715-9094d449601f/ve1abb3ce_fig3_ipf_phase2_landscape.png})

| verdict | n | evidence tier |
|---|---|---|
| Works | 6 | Probable |
| Conflicting | 1 | Uncertain |
| Uncertain | 43 | Uncertain |
| Failed | 8 | Probable |
| Harm outweighs benefit | 8 | 7 Probable, 1 Uncertain |
| Poorly studied | 215 | Unknown |

**215 of 281 entities are `Poorly studied`** — registry arms or literature mentions for which no
IPF-specific human outcome result was retrievable. That is the dominant feature of the IPF treatment
landscape, and it is a statement about the evidence, not about the interventions.

### 3.1 Works (6) — each on a named dimension only

| intervention | dimension graded | key result source |
|---|---|---|
| pirfenidone | prevention of categorical progression (E3), FVC decline (E1) | PMID 24836312 (ASCEND) |
| nintedanib | annual rate of FVC decline (E1) | PMID 24836310 (INPULSIS) |
| nerandomilast | FVC change at 52 weeks (E1) | PMID 40387033 |
| inhaled treprostinil | FVC change at 52 weeks (E1) | PMID 41812190 (TETON-1) |
| pulmonary rehabilitation / exercise training | functional capacity (E5), HRQoL (E6) | PMID 33164264 |
| lung transplantation | survival (E11) | PMID 37625610 (registry) |

Constraints attached to these rows in the table itself: nerandomilast's mortality and exacerbation
endpoints were not significant; the rehabilitation row claims nothing about lung-function decline,
exacerbation, survival, or durability beyond the trial periods, and its strongest randomised source is
a TCM breathing-exercise trial that also appears in the traditional-medicine screen; the
transplantation row rests on registry-era comparisons, not randomised evidence, so it is capped by the
brief's survival rule. **No pharmacological intervention in this landscape is graded as improving
survival, preserving lung function in absolute terms, reversing fibrosis, or curing IPF.**

### 3.2 Failed (8) — null on the trial's own primary endpoint

interferon gamma-1b, bosentan, co-trimoxazole, simtuzumab, SAR156597, zinpentraxin alfa,
pamrevlumab, N-acetylcysteine (monotherapy).

`pamrevlumab` is recorded as *resolved by supersession*: phase 2 positive, adequately sized phase 3
null on the same endpoint. The disagreement is preserved in the conflicts register rather than in the
verdict. `n-acetylcysteine` is null in the overall PANTHER-IPF arm (n=264); the post hoc telomere and
TOLLIP genotype analyses are recorded as an open question (UN11), not as a positive result.

### 3.3 Harm outweighs benefit (8)

warfarin, ambrisentan, riociguat, carlumab, BG00011, cyclophosphamide, triple therapy
(prednisone + azathioprine + NAC), corticosteroid monotherapy.

The corticosteroid row keeps its harm verdict but sits at tier `Uncertain`: the pooled sources are
predominantly observational and steroid monotherapy has never been randomised in IPF, while steroids
remain in use for acute exacerbation, where nothing has randomised support.

### 3.4 Conflicting (1)

`sildenafil` — randomised IPF evidence points both ways and is left as a preserved disagreement.

## 4. Negative-results register

65 rows, separated by failure domain rather than lumped as "failed":

| failure domain | n |
|---|---|
| no benefit on the trial's own primary endpoint | 8 |
| harm exceeded benefit | 8 |
| development stopped before a result was established | 49 |

The third group is the largest. Termination reasons were classified from registry text into futility,
safety, recruitment or operational failure, sponsor or business decision, and unknown; where the
registry gives no reason, the row says `unknown` rather than guessing. Two termination reasons the
keyword classifier had misassigned were corrected to futility by hand.

## 5. Conflicts register

8 entries. Four are per-intervention (sildenafil, co-trimoxazole, pamrevlumab, N-acetylcysteine) and
four are record-level:

- **FVC as a surrogate for mortality (unresolved).** Every `Works` drug verdict here rests on FVC or an
  FVC-based composite. Phase 1 retrieved no source establishing trial-level surrogacy for mortality,
  and none refuting it. Antifibrotic survival evidence is pooled observational, not randomised.
- **Corticosteroids** — evidence-class split between observational harm signals and continued use in
  acute exacerbation.
- **N-acetylcysteine** — post hoc subgroup signals against an overall null.
- **Traditional Chinese medicine** — database-coverage-limited evidence (§6).

## 6. Traditional-medicine screen

![Traditional-medicine screen by tier and design]({/Users/wangxiaowen/.claude-science/orgs/5d2b56b1-a3ac-45a3-bad2-5aa0b8b074d5/artifacts/proj_06ead86ec16d/362ca766-8631-498b-ace5-e7ceb1b7eb7d/vf5351ca2_fig4_ipf_phase2_tm_screen.png})

107 records screened into the prespecified tiers. Nothing was deleted; records failing the main
threshold sit in a lower tier with a stated reason.

| tier | n | meaning |
|---|---|---|
| T1 | 3 | randomised, IPF-only, eligible outcome, registration stated |
| T2 | 12 | randomised or pooled; registration or allocation concealment not documented |
| T3 | 15 | non-randomised human, mixed-population, or outcome-limited |
| T4 | 74 | non-human or non-primary evidence; never graded on efficacy |
| T5 | 3 | protocol or no retrievable result (enters the L5 retrievability register) |

Seven named traditional interventions entered the landscape as curated rows: Jinbei oral liquid,
Kangxian Huanji Granule, Qizhukangxian granules, Feiwei granules, umbilical moxibustion, Pulmonary
Daoyin, and Baduanjin exercise; plus one aggregate row for the pooled Chinese-herbal-medicine
syntheses. **Every one is capped at `Uncertain`** by the brief's risk-of-bias rule: risk of bias could
only be judged from abstracts, samples are small (n = 80–120 where an n was extractable from the
abstract; the Baduanjin trial reports 28 in its methods text) and follow-up short (4 weeks – 48 weeks
where a duration was stated), author-reported directions are mixed, and no result was independently replicated
outside its originating research setting. Feiwei granules is author-reported null and also appears in
the negative-results register.

The classifier that produced these tiers was rewritten once (C8): a first pass keyed on abstract wording
misclassified a large block of narrative reviews and mechanistic papers as non-randomised human
evidence. Four borderline records were then corrected by hand with reasons recorded in the table —
an open-label single-arm pilot demoted from T1, a registered randomised exercise trial promoted into
it, an unregistered randomised trial placed one tier down, and a randomised safety-and-feasibility
study kept but explicitly barred from supporting an efficacy statement.

## 7. Method and its limits

Grading is a documented rule engine plus manual curation, not model judgement (C7). Every verdict is
reproducible from the recorded columns; 25 rows carry a
`curation_note` stating what was overridden and why.

Three attribution repairs were needed and are logged (C5, C6). Evidence is now attached to an
intervention from each extraction's own intervention list, with comparator-only mentions excluded, and
each source is classified as monotherapy, combination or head-to-head, or pooled many-agent — the last
kept as context but excluded from direction counting, which is what had let network meta-analyses
spread one direction across every agent they name.

Known limitations, none of them resolved in this phase:

- Grading is from **abstracts**, not full texts. Formal risk-of-bias assessment would require full text.
- Chinese-language databases were not searched, so the traditional-medicine counts and directions may
  be biased in unknown magnitude and direction.
- The `Poorly studied` bucket is heterogeneous: it mixes genuinely unstudied agents with agents whose
  results exist but were not retrievable here (L5).
- Registry phase labels overstate two very small, very short crossover studies; those rows were
  downgraded by hand and say so.

## 8. What Phase 3 needs from this phase

The Open Treatment Map should consume `ipf_phase2_landscape.csv` as its intervention spine, keyed by
verdict × evidence tier × outcome dimension, and must carry forward, unmerged: the negative-results
register, the conflicts register, the L5 retrievability problem for the 49 stopped-without-result
programmes, and the corrections log C1–C9.

## 8b. Correction applied after first release of this report

Corrections entry **C10**: this report and nine rows of `ipf_phase2_landscape.csv` carried
mis-mapped E-codes against `ipf_phase1_endpoint_taxonomy.csv` (categorical progression was written
E7 instead of E3; functional capacity E13 instead of E5; HRQoL/SGRQ E11 instead of E6; survival E15
instead of E11; cough E10 instead of E9; acute exacerbation E9 instead of E10). The dimension
*names* and the underlying results were correct throughout; only the codes were wrong. Both files
are corrected and re-issued; no verdict, tier or effect estimate changed.

## 9. Files

- `ipf_phase2_landscape.csv` — 281 intervention entities, graded
- `ipf_phase2_traditional_medicine_screen.csv` — 107 records, tiered
- `ipf_phase2_negative_results_register.csv` — 65 rows
- `ipf_phase2_conflicts_register.csv` — 8 preserved disagreements
- `ipf_phase2_search.json`, `ipf_phase2_entity_hits.json`, `ipf_phase2_extractions.json` — search strategies and extracted records
- `corrections_log.csv` — C1–C9
- `fig3_ipf_phase2_landscape.png`, `fig4_ipf_phase2_tm_screen.png`
