"""Build the IPF public-site payload (ipf_record.json) from the corrected research record.

Design rules, carried from the rheumatoid-arthritis implementation and extended where the
IPF record holds a state that model cannot express:

  - the CSV registers stay canonical; this file only derives a view of them
  - every published row gets a stable id assigned by row order, so a URL can deep-link
  - free-text identifier strings are parsed into resolvable {type, id, url} objects
  - no heuristic source guessing: a citation is published only where the record states it
  - corrections are linked to what they correct, so a UI can badge superseded rows
  - vocabularies carry counts, so facets need no client-side scan
  - nothing is invented: a field that cannot be derived is omitted, not guessed
  - grade-bearing fields (verdict, tier, dimension, caveat) travel with every statement

Publication-stage normalisations are listed in `meta.normalisations` as PUB-01, PUB-02 and
PUB-03. No research file is rewritten by this script.

Usage (from the archive root):
    IPF_DATA=research_record/registers IPF_OUT=data/ipf_record.json python data/build_ipf_public_data.py
"""
import os, re, json, datetime
import pandas as pd

DATA = os.environ.get("IPF_DATA", ".")
GEN = datetime.date.today().isoformat()

ID_PATTERNS = [
    ("pmid", r"PMID[s]?[:\s]*((?:\d{7,8}[,;\s]*)+)", "https://pubmed.ncbi.nlm.nih.gov/{}/"),
    ("doi", r"(10\.\d{4,9}/[^\s;,)\]]+)", "https://doi.org/{}"),
    ("nct", r"(NCT\d{8})", "https://clinicaltrials.gov/study/{}"),
    ("isrctn", r"(ISRCTN\d{6,8})", "https://www.isrctn.com/{}"),
    ("euctr", r"(\d{4}-\d{6}-\d{2})", "https://www.clinicaltrialsregister.eu/ctr-search/search?query={}"),
    ("chictr", r"(ChiCTR[A-Za-z0-9-]+)", ""),
    ("jprn", r"(JPRN-[A-Za-z0-9]+)", ""),
]
BARE_PMID = re.compile(r"^[\d\.,;\s]+$")  # a bare digit list is a PMID list in this record


CANONICAL_FILES = []


def load(name):
    """Read a canonical register and record that the build consumed it."""
    CANONICAL_FILES.append(name)
    return pd.read_csv(os.path.join(DATA, name))


def clean(v):
    """NaN, empty and placeholder strings become None; numeric strings keep their text."""
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return None
    if isinstance(v, float) and v.is_integer():
        return int(v)
    s = str(v).strip()
    if s == "" or s.lower() in {"nan", "none", "n/a", "na", "-", "—"}:
        return None
    return s


def parse_ids(*texts):
    """Extract resolvable identifiers from free-text source strings."""
    out, seen = [], set()
    for text in texts:
        s = clean(text)
        if s is None:
            continue
        s = str(s)
        if BARE_PMID.match(s):
            s = "PMID " + s.replace(".0", "")
        for kind, pat, url in ID_PATTERNS:
            for m in re.findall(pat, s, flags=re.I):
                vals = re.split(r"[,;\s]+", m.strip()) if kind == "pmid" else [m]
                for v in vals:
                    v = v.strip().rstrip(".")
                    if v.endswith(".0"):
                        v = v[:-2]
                    if not v or (kind, v.lower()) in seen:
                        continue
                    seen.add((kind, v.lower()))
                    out.append({"type": kind, "id": v, "url": url.format(v) if url else None})
    return out


def codes(text, pat):
    return sorted(set(re.findall(pat, clean(text) or "")))


def truthy(v):
    return str(clean(v)).lower() in {"yes", "true", "y", "1"}


def rows(df, prefix, cols=None, id_col=None, start=1):
    """Emit records with a stable public id assigned by row order."""
    out = []
    for i, r in enumerate(df.to_dict("records"), start=start):
        rec = {"id": r[id_col] if id_col else f"{prefix}-{i:03d}"}
        for k, v in r.items():
            if cols and k not in cols:
                continue
            rec[k] = clean(v)
        out.append(rec)
    return out


def counts(seq):
    c = {}
    for v in seq:
        if v is None:
            continue
        c[v] = c.get(v, 0) + 1
    return [{"value": k, "count": v} for k, v in sorted(c.items(), key=lambda kv: -kv[1])]


# ---------------------------------------------------------------- source tables
LAND = load("ipf_phase2_landscape.csv")
MAP = load("ipf_phase3_treatment_map.csv")
NEG = load("ipf_phase2_negative_results_register.csv")
CONF = load("ipf_phase2_conflicts_register.csv")
CAND = load("ipf_phase4_candidate_register.csv")
CORR = load("corrections_log.csv")
ACT = load("ipf_phase4_actions.csv")
LIM = load("ipf_phase4_limitations.csv")
UNMET = load("ipf_phase1_unmet_needs.csv")
OQ = load("ipf_phase0_open_questions.csv")
CEIL = load("ipf_phase1_ceiling.csv")
ETAX = load("ipf_phase1_endpoint_taxonomy.csv")
RETR = load("ipf_phase1_retrievability_register.csv")
SWEEP = load("ipf_phase6_registry_results_sweep.csv")
FOUND = load("ipf_phase6_missing_results_retrieval.csv")
MEAS = load("ipf_phase6_recovery_endpoints.csv")
COVG = load("ipf_phase6_chinese_language_coverage.csv")
# PUB-03: one coverage row states a present-tense claim against a superseded landscape size.
# C38 supersedes 281 rows / 278 distinct with 283 rows / 279 distinct. The claim is unchanged;
# only the denominator is republished. The source register is not altered.
NORMALISED_DENOMINATOR = []
for _c in COVG.columns:
    if COVG[_c].dtype == object:
        _hit = COVG[_c].astype(str).str.contains("281-row landscape", na=False)
        for _i in COVG.index[_hit]:
            NORMALISED_DENOMINATOR.append("%s row pmid %s, field %s" % (
                "ipf_phase6_chinese_language_coverage.csv", COVG.at[_i, "pmid"], _c))
        COVG.loc[_hit, _c] = COVG.loc[_hit, _c].astype(str).str.replace(
            "281-row landscape", "283-row landscape (279 distinct interventions, correction C38)",
            regex=False)
TMS = load("ipf_phase2_traditional_medicine_screen.csv")
CANONICAL_FILES.append("ipf_phase2_extractions.json")
EXTR = json.load(open(os.path.join(DATA, "ipf_phase2_extractions.json")))

# ------------------------------------------------------- titles known to the record
TITLES = {}
for e in EXTR:
    p = clean(e.get("pmid"))
    if p:
        TITLES[("pmid", str(p))] = {"title": clean(e.get("title")), "journal": clean(e.get("journal")), "year": clean(e.get("year"))}
for _, r in TMS.iterrows():
    p = clean(r.get("pmid"))
    if p:
        TITLES.setdefault(("pmid", str(p)), {"title": clean(r.get("title")), "journal": clean(r.get("journal")), "year": clean(r.get("year"))})
for _, r in COVG.iterrows():
    p = clean(r.get("pmid"))
    if p:
        TITLES.setdefault(("pmid", str(p)), {"title": clean(r.get("topic")), "journal": clean(r.get("journal")), "year": clean(r.get("year"))})
for _, r in FOUND.iterrows():
    p = clean(r.get("pmid"))
    if p:
        TITLES.setdefault(("pmid", str(p)), {"title": clean(r.get("pub_title")), "journal": clean(r.get("journal")), "year": clean(r.get("pub_year"))})
for src in (RETR, SWEEP):
    for _, r in src.iterrows():
        n = clean(r.get("nct"))
        if n:
            TITLES.setdefault(("nct", n), {"title": clean(r.get("title")), "journal": None, "year": None})

REF_INDEX = {}


def refs(*texts, cited_by=None):
    """Resolve identifiers and register them in the reference index."""
    out = parse_ids(*texts)
    for r in out:
        key = (r["type"], r["id"])
        e = REF_INDEX.setdefault(key, {"type": r["type"], "id": r["id"], "url": r["url"],
                                       "title": None, "journal": None, "year": None,
                                       "title_source": None, "cited_by": []})
        meta = TITLES.get(key)
        if meta and meta.get("title") and not e["title"]:
            e.update(title=meta["title"], journal=meta.get("journal"), year=meta.get("year"),
                     title_source="within the research record")
        if cited_by and cited_by not in e["cited_by"]:
            e["cited_by"].append(cited_by)
    return out


# ---------------------------------------------------------------- treatment map
map_rows = []
for i, r in enumerate(MAP.to_dict("records"), 1):
    mid = f"TM-{i:03d}"
    map_rows.append({
        "id": mid,
        "internal_map_id": clean(r["map_id"]),
        "section": clean(r["section"]),
        "statement": clean(r["statement"]),
        "subject": clean(r["subject"]),
        "outcome_dimension": clean(r["outcome_dimension"]),
        "evidence_tier": clean(r["evidence_tier"]),
        "evidence_tier_sublabel": clean(r["evidence_tier_sublabel"]),
        "caveat": clean(r["caveat"]),
        # three statements carry no separate caveat field in the research record; the payload
        # discloses that rather than leaving a UI to render them as caveat-free
        "caveat_status": "stated in the record" if clean(r["caveat"])
        else "absent in the record - the statement's own qualifications are the only ones recorded",
        "sources_verbatim": clean(r["sources"]),
        "refs": refs(r["sources"], cited_by=mid),
        "maps_to_unmet_need": codes(r["maps_to_unmet_need"], r"UN\d+"),
        "provenance": clean(r["provenance"]),
        "phase4_status": clean(r["phase4_status"]),
        "phase6_status": clean(r["phase6_status"]),
        "superseded_by": codes(str(r["phase4_status"]) + " " + str(r["phase6_status"]) + " " + str(r["statement"]), r"\bC\d{1,2}\b"),
    })

# --------------------------------------------------------------- interventions
IV_COLS = ["intervention", "category", "verdict_class", "verdict_sublabel", "evidence_tier",
           "evidence_tier_sublabel", "endpoint_dimension", "strongest_design", "n_human_studies",
           "n_mono_randomised", "key_result_verbatim", "metric", "duration_weeks",
           "comparator_arm_change", "indirect_only", "conflict_present", "conflict_note", "safety",
           "abandoned_reason", "termination_reasons", "registry_trials", "max_phase", "statuses",
           "trials_with_posted_results", "why", "curation_note", "duplicate_of", "registry_only_result"]
iv_rows, NORMALISED_TIER = [], []
for i, r in enumerate(LAND.to_dict("records"), 1):
    iid = f"IV-{i:03d}"
    rec = {"id": iid}
    for c in IV_COLS:
        rec[c] = clean(r.get(c))
    rec["traditional"] = truthy(r.get("traditional"))
    rec["is_duplicate"] = bool(rec["duplicate_of"]) or str(rec["verdict_class"]).startswith("Duplicate")
    # publication-stage normalisation: two rows carried a verdict label in the tier column
    if rec["evidence_tier"] == "Poorly studied":
        NORMALISED_TIER.append(rec["intervention"])
        rec["evidence_tier"] = "Unknown"
        rec["evidence_tier_sublabel"] = rec["evidence_tier_sublabel"] or "normalised at publication (PUB-01)"
    if rec["registry_only_result"]:
        rec["evidence_access"] = "registry posting only, or posted result that cannot be graded"
    elif not clean(r.get("key_result_pmid")) and not rec["key_result_verbatim"]:
        rec["evidence_access"] = "no IPF-specific human result retrieved"
    else:
        rec["evidence_access"] = "published result"
    rec["refs"] = refs(r.get("key_result_pmid"), r.get("pooled_context_pmids"),
                       r.get("combination_evidence_pmids"), cited_by=iid)
    iv_rows.append(rec)

IVX = [r for r in iv_rows if not r["is_duplicate"]]

# ------------------------------------------------------------------- negatives
neg_rows = []
for i, r in enumerate(NEG.to_dict("records"), 1):
    nid = f"NEG-{i:03d}"
    rec = {"id": nid}
    for c in ["intervention", "verdict_class", "failure_domain", "abandoned_reason", "evidence_tier",
              "evidence_tier_sublabel", "max_phase", "registry_trials", "trials_with_posted_results",
              "key_result_verbatim", "metric", "duration_weeks", "endpoint_dimension",
              "termination_reasons", "conflict_note", "why", "curation_note"]:
        rec[c] = clean(r.get(c))
    rec["refs"] = refs(r.get("key_result_pmid"), cited_by=nid)
    neg_rows.append(rec)

# ------------------------------------------------------------------- conflicts
conf_rows = []
for i, r in enumerate(CONF.to_dict("records"), 1):
    cid = f"CF-{i:03d}"
    conf_rows.append({
        "id": cid, "internal_id": clean(r["id"]), "subject": clean(r["subject"]),
        "conflict_type": clean(r["conflict_type"]), "description": clean(r["description"]),
        "current_status": clean(r["current_status"]),
        "resolution_rule_applied": clean(r["resolution_rule_applied"]),
        "verdict_recorded": clean(r["verdict_recorded"]),
        "sources_verbatim": clean(r["sources"]), "refs": refs(r["sources"], cited_by=cid),
        "resolved": "unresolved" not in str(r["current_status"]).lower(),
    })

# ------------------------------------------------- candidates, screens, leads
SCREEN_TEXT = {}
for _, r in CAND.iterrows():
    sids = codes(r.get("screen_failed"), r"S\d")
    parts = [p.strip() for p in str(clean(r.get("screen_definitions")) or "").split("|") if p.strip()]
    if len(sids) == len(parts):  # unambiguous pairing only
        for sid, part in zip(sids, parts):
            SCREEN_TEXT.setdefault(sid, part)
screens = [{"id": k, "definition": v} for k, v in sorted(SCREEN_TEXT.items())]

cand_rows = []
for r in CAND.to_dict("records"):
    cand_rows.append({
        "id": clean(r["cand_id"]), "subject": clean(r["subject"]), "shape": clean(r["shape"]),
        "from_statement": clean(r["from_statement"]), "outcome": clean(r["outcome"]),
        "screens_failed": codes(r.get("screen_failed"), r"S\d"),
        "reason": clean(r["reason"]),
        "promoted_to_lead": truthy(r.get("promoted_to_lead")),
        "status": ("held at verification" if str(r["outcome"]).startswith("held")
                   else "rejected as a research lead"),
        "action_retained": clean(r["outcome"]).split("; ")[1] if "; " in str(r["outcome"]) else None,
    })

leads_outcome = {
    "leads": 0,
    "statement": ("Phase 4 promoted no research lead. Forty-one candidate signals were screened against "
                  "six prespecified screens; none met the promotion bar. Four are held at verification "
                  "because their key result could not be checked against primary full text, and are "
                  "neither promoted nor rejected. Phase 5 (deep investigation of surviving leads) was "
                  "therefore recorded as skipped because there was nothing to investigate, not as not done."),
    "candidates_screened": len(cand_rows),
    "held_at_verification": sum(1 for c in cand_rows if c["status"] == "held at verification"),
    "rejected": sum(1 for c in cand_rows if c["status"] == "rejected as a research lead"),
    "actions_retained": sum(1 for c in cand_rows if c["action_retained"]),
    "not_a_therapeutic_claim": ("A held candidate is a verification state, not a positive finding, and an "
                                "unretrieved or missing result is not evidence of promise."),
}

# ------------------------------------------------ corrections, actions, limits
corr_rows = [{"id": clean(r["id"]), "date": clean(r["date"]), "phase": clean(r["phase"]),
              "claim_corrected": clean(r["claim_corrected"]), "correction": clean(r["correction"]),
              "basis": clean(r["basis"]), "effect": clean(r["effect"])}
             for r in CORR.to_dict("records")]

act_rows = [{"id": clean(r["action_id"]), "type": clean(r["type"]), "subject": clean(r["subject"]),
             "detail": clean(r["detail"]), "from_candidate": clean(r["from_candidate"]),
             "phase6_outcome": clean(r["phase6_outcome"]), "phase6_detail": clean(r["phase6_detail"]),
             "open": str(clean(r["phase6_outcome"]) or "").startswith(("opened", "blocked", "partially", "not executable"))}
            for r in ACT.to_dict("records")]

# ------------------------------------------------------------------ retrieval
unretrievable = RETR[RETR.results_retrievable.astype(str).str.startswith("no results found")]
past_window = unretrievable[unretrievable.reporting_status.astype(str).str.startswith("beyond")]
retr_summary = {
    # the register holds the completed trials WITHOUT posted registry results; the Phase 1
    # denominator of all completed interventional IPF studies is 239, of which 90 posted results
    "completed_interventional_trials": 239,
    "with_results_posted_on_registry": 90,
    "register_rows_without_posted_results": int(len(RETR)),
    "no_retrievable_result": int(len(unretrievable)),
    "no_retrievable_result_past_reporting_window": int(len(past_window)),
    "publication_likely_primary_outcome_unverified": int((RETR.results_retrievable.astype(str).str.startswith("publication likely")).sum()),
    "registry_posted_results_read_in_sweep": int(len(SWEEP)),
    "publications_located_by_registry_id_search": int(FOUND.nct.nunique()),
    "publications_located_rows": int(len(FOUND)),
    "publications_reporting_the_missing_primary_outcome": 0,
    "note": ("Missing results are missing, not mis-indexed: a registry-identifier search of the "
             "unretrievable trials located publications for a small minority and none of them "
             "reported the trial's missing primary clinical outcome."),
}

record = {
    "meta": {
        "project": "Open Therapeutics — Open Evidence Record",
        "record": "IPF Open Evidence Record",
        "disease": "Idiopathic pulmonary fibrosis (IPF)",
        "scope": ("IPF only. Evidence from other fibrotic diseases appears only where it is labelled "
                  "indirect evidence."),
        "generated": GEN,
        "schema_version": "ipf-public-1.1 (extends the rheumatoid-arthritis public model)",
        "source_of_truth": "the corrected Phase 0-6 research record; later corrections supersede earlier statements",
        "research_status": "research cycle complete through Phase 6; no research lead promoted",
        "peer_reviewed": False,
        "disclaimer": ("This is a research record, not medical advice. It grades published evidence and "
                       "names what is missing. Nothing here establishes that a treatment is effective, "
                       "safe or appropriate for any patient. Treatment decisions belong to a qualified "
                       "clinician with the full patient context."),
        "reading_rules": [
            "Slowing the rate of lung-function decline is not preserving lung function, not recovering lost function, not reversing fibrosis and not a cure.",
            "A lung-function effect is not a demonstrated survival benefit. No drug in this record has randomised evidence of prolonging survival.",
            "Patient-level prognostic association between lung-function decline and death does not establish that a treatment-induced change in decline predicts survival.",
            "Poorly studied is not ineffective: it means the evidence needed to judge the intervention does not exist.",
            "Missing, unretrieved or inaccessible evidence is not therapeutic promise.",
            "A registry posting without an analysable between-arm result is identifiable as such and is not graded as published evidence.",
            "A candidate held at verification is neither promoted nor rejected.",
            "Every verdict is graded on one named outcome dimension only and carries its caveat.",
        ],
        "normalisations": [
            {"id": "PUB-01", "what": "two intervention rows carried the verdict label 'Poorly studied' in the evidence-tier column; published as tier 'Unknown', which is the tier that verdict class uses throughout", "rows": NORMALISED_TIER},
            {"id": "PUB-02", "what": "six internal treatment-map identifiers (M2.13-M2.18) were each used by two rows; the published payload assigns stable TM-### identifiers by row order and preserves the internal identifier in internal_map_id"},
            {"id": "PUB-03", "what": "one Chinese-language coverage row stated a present-tense claim against a superseded landscape size ('the 281-row landscape'); the denominator is republished as the final one established by correction C38 (283 rows, 279 distinct interventions). The claim itself is unchanged: the intervention is still absent from the landscape", "rows": NORMALISED_DENOMINATOR},
        ],
        "canonical_files": sorted(CANONICAL_FILES),
        "source_directory": "research_record/registers (archive layout); set IPF_DATA to override",
        "historical_text_note": ("Phase-dated text quotes the landscape size as it stood in that phase. Corrections C31 and C33 "
                                 "and two Phase 4 rows (an action narrative and a limitation) say 281 rows / 278 distinct "
                                 "interventions; C38 supersedes both with 283 rows / 279 distinct. Past-tense accounts of work "
                                 "performed are left as written; only present-tense claims about the final record were "
                                 "renormalised (PUB-03)."),
    },
    "counts": {
        "map_statements": len(map_rows),
        "interventions_published": len(iv_rows),
        "interventions_distinct": len(IVX),
        "duplicate_rows_flagged": len(iv_rows) - len(IVX),
        "negative_results": len(neg_rows),
        "conflicts": len(conf_rows),
        "conflicts_unresolved": sum(1 for c in conf_rows if not c["resolved"]),
        "candidates_screened": len(cand_rows),
        "research_leads": 0,
        "corrections": len(corr_rows),
        "actions": len(act_rows),
        "actions_open": sum(1 for a in act_rows if a["open"]),
        "unmet_needs": len(UNMET),
        "open_questions": len(OQ),
        "limitations": len(LIM),
        "references": None,
    },
    "vocab": {
        "sections": counts(r["section"] for r in map_rows),
        "evidence_tiers": counts(r["evidence_tier"] for r in map_rows),
        "verdict_classes": counts(r["verdict_class"] for r in IVX),
        "intervention_categories": counts(r["category"] for r in IVX),
        "evidence_access": counts(r["evidence_access"] for r in IVX),
        "failure_domains": counts(r["failure_domain"] for r in neg_rows),
        "conflict_types": counts(r["conflict_type"] for r in conf_rows),
        "candidate_outcomes": counts(r["outcome"] for r in cand_rows),
        "action_types": counts(r["type"] for r in act_rows),
        "traditional_medicine_rows": [{"value": "traditional or historical intervention", "count": sum(1 for r in IVX if r["traditional"])}],
    },
    "map": map_rows,
    "interventions": iv_rows,
    "negatives": neg_rows,
    "conflicts": conf_rows,
    "leads": [],
    "leads_outcome": leads_outcome,
    "candidates": cand_rows,
    "screens": screens,
    "corrections": corr_rows,
    "actions": act_rows,
    "limitations": rows(LIM, "LIM", id_col="limitation_id"),
    "unmet_needs": rows(UNMET, "UN", id_col="code"),
    "open_questions": rows(OQ, "OQ", id_col="id"),
    "therapeutic_ceiling": rows(CEIL, "CEIL"),
    "endpoint_taxonomy": rows(ETAX, "E", id_col="id"),
    "retrievability_summary": retr_summary,
    "retrievability": rows(RETR, "RT", cols=["nct", "title", "phase", "enrollment", "interventions",
                                             "sponsor", "completion", "results_posted",
                                             "results_retrievable", "linked_pmids", "reporting_status"]),
    "registry_results_sweep": rows(SWEEP, "RS", cols=["nct", "title", "phase", "enroll", "status",
                                                      "completion", "n_primary", "n_analyses",
                                                      "iv_match", "sweep_outcome"]),
    "located_publications": rows(FOUND, "LP"),
    "measurement_gaps": rows(MEAS, "MG"),
    "coverage_gaps": rows(COVG, "CG"),
}

record["references"] = sorted(REF_INDEX.values(), key=lambda r: (r["type"], r["id"]))
record["counts"]["references"] = len(record["references"])
record["counts"]["references_with_title_in_record"] = sum(1 for r in record["references"] if r["title"])

if __name__ == "__main__":
    out = os.environ.get("IPF_OUT", "ipf_record.json")
    with open(out, "w") as fh:
        json.dump(record, fh, indent=1, ensure_ascii=False)
    print(out, os.path.getsize(out), "bytes")
    for k, v in record["counts"].items():
        print(f"  {k}: {v}")
