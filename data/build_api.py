"""Build a single JSON payload from the open-record CSVs, for a site to read.

Design rules, which are the point of this file:
  - every row gets a stable id, so a URL can deep-link to one statement
  - free-text identifier strings are parsed into resolvable {type, id, url} objects
  - corrections are linked to what they correct, so a UI can badge superseded rows
  - vocabularies are emitted with counts, so facets need no client-side scan
  - nothing is invented: a field that cannot be derived is omitted, not guessed
"""
import os, re, json, datetime
import pandas as pd

DATA = "ra_open_record/data"

ID_PATTERNS = [
    ("pmid",    r"PMID[s]?[:\s]*((?:\d{7,8}[,;\s]*)+)", "https://pubmed.ncbi.nlm.nih.gov/{}/"),
    ("doi",     r"(10\.\d{4,9}/[^\s;,)\]]+)",           "https://doi.org/{}"),
    ("nct",     r"(NCT\d{8})",                          "https://clinicaltrials.gov/study/{}"),
    ("isrctn",  r"(ISRCTN\d{6,8})",                      "https://www.isrctn.com/{}"),
    ("euctr",   r"(\d{4}-\d{6}-\d{2})",                  "https://www.clinicaltrialsregister.eu/ctr-search/search?query={}"),
    ("ntr",     r"\b(NTR\d{3,5})\b",                     ""),
    ("eudract_other", r"\b(NL\d{4})\b",                  ""),
]


def parse_ids(text):
    """Extract resolvable identifiers from a free-text source string."""
    out, seen = [], set()
    s = "" if text is None else str(text)
    if not s or s.lower() == "nan":
        return out
    for kind, pat, url in ID_PATTERNS:
        for m in re.findall(pat, s, flags=re.I):
            vals = re.split(r"[,;\s]+", m.strip()) if kind == "pmid" else [m]
            for v in vals:
                v = v.strip().rstrip(".")
                if not v or (kind, v.lower()) in seen:
                    continue
                seen.add((kind, v.lower()))
                out.append({"type": kind, "id": v, "url": url.format(v) if url else None})
    return out


def split_codes(text, pat=r"UN\d+"):
    return re.findall(pat, "" if text is None else str(text))


def clean(v):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return None
    s = str(v).strip()
    return None if s.lower() in ("", "nan", "none", "—", "-", "n/a") else s


STOPWORDS = {
    "meta", "analysis", "meta-analysis", "cochrane", "review", "rct", "trial", "trials",
    "study", "consensus", "international", "nma", "network", "systematic", "post", "hoc",
    "data", "registry", "cohort", "reports", "report", "case", "series", "guideline",
    "with", "and", "the", "for", "vs", "versus", "added", "arm", "phase", "open", "label",
}


def label_tokens(text):
    """Distinctive tokens from a short human source label (drops method vocabulary)."""
    toks = re.split(r"[^A-Za-z0-9\-]+", "" if text is None else str(text))
    keep = lambda t: (len(t) >= 4 or (len(t) == 3 and t.isupper()))
    return [t for t in toks if keep(t) and t.lower() not in STOPWORDS]


def link_by_label(label, interventions, references):
    """Conservative candidate links for a map row whose source is a label, not an ID.

    Emitted as CANDIDATES, never as citations: a token match is not a verified
    attribution, and a UI must present it as 'possible source', not as a reference.
    """
    out = []
    for t in label_tokens(label):
        tl = t.lower()
        for d in interventions:
            if tl in (d.get("intervention") or "").lower():
                out.append({"kind": "intervention", "id": d["id"],
                            "label": d.get("intervention"), "matched_on": t})
        for d in references:
            if tl in (d.get("title") or "").lower() or tl in (d.get("key_finding") or "").lower():
                out.append({"kind": "reference", "id": d["id"], "label": d.get("title"),
                            "matched_on": t})
    seen, uniq = set(), []
    for d in out:
        k = (d["kind"], d["id"])
        if k not in seen:
            seen.add(k)
            uniq.append(d)
    return uniq[:6]


def rows(df, id_prefix=None, id_col=None):
    out = []
    for i, r in df.iterrows():
        d = {k: clean(v) for k, v in r.items()}
        if id_col:
            d["id"] = clean(r[id_col])
        elif id_prefix:
            d["id"] = f"{id_prefix}-{i + 1:03d}"
        out.append(d)
    return out


def counts(seq):
    c = {}
    for v in seq:
        for x in (v if isinstance(v, list) else [v]):
            if x:
                c[x] = c.get(x, 0) + 1
    return dict(sorted(c.items(), key=lambda kv: -kv[1]))


def build(outfile="ra_record.json"):
    T = {f[:-4]: pd.read_csv(os.path.join(DATA, f))
         for f in os.listdir(DATA) if f.endswith(".csv")}

    mp = rows(T["treatment_map"], "TM")
    for d in mp:
        d["refs"] = parse_ids(d.get("source"))
        d["unmet_need_codes"] = split_codes(d.get("unmet_need"))
        d.pop("evidence_tier_ord", None)

    iv = rows(T["intervention_register"], "IV")
    for d in iv:
        d["refs"] = parse_ids(" ".join(filter(None, [d.get("pmid"), d.get("doi")])))
        d["unmet_need_codes"] = split_codes(d.get("unmet_need"))

    corr = rows(T["corrections_log"], id_col="id")
    for d in corr:
        d["refs"] = parse_ids(d.get("key_ids"))
        tgt = d.get("corrects") or ""
        d["corrects_lead"] = (re.findall(r"RL-\d+", tgt) or [None])[0]
        d["corrects_phase"] = (re.findall(r"Phase \d+|External public record", tgt) or [None])[0]

    leads = rows(T["research_leads_status"], id_col="lead")
    steps = rows(T["next_steps_specification"], id_col="step_id")
    checks = rows(T["verification_checks"], "VC")
    for d in checks:
        d["refs"] = parse_ids(d.get("primary_source"))
    for L in leads:
        L["steps"] = [s for s in steps if s.get("lead") == L["id"]]
        L["verification_checks"] = [c for c in checks if c.get("lead") == L["id"]]
        L["corrections"] = [c["id"] for c in corr if c.get("corrects_lead") == L["id"]]

    refs = rows(T["references"], "REF")
    for d in refs:
        d["pmid"] = None if d.get("pmid") is None else str(d["pmid"]).split(".")[0]
    for d in refs:
        d["url"] = (f"https://doi.org/{d['doi']}" if d.get("doi")
                    else (f"https://pubmed.ncbi.nlm.nih.gov/{d['pmid'].split('.')[0]}/" if d.get("pmid") else None))

    for d in mp:
        d["ref_candidates"] = [] if d["refs"] else link_by_label(d.get("source"), iv, refs)

    payload = {
        "meta": {
            "project": "Open Therapeutics #001",
            "disease": "Rheumatoid arthritis",
            "generated": datetime.date.today().isoformat(),
            "schema_version": "1.0",
            "disclaimer": ("Not medical advice. Contains no treatment recommendation and no claim "
                           "that any intervention works. Evidence grades describe the state of the "
                           "evidence, not the biology."),
            "licence": "Creative Commons Attribution 4.0 International (CC BY 4.0)",
            "canonical_source": "ra_open_record bundle (README.md, SUMMARY.md, phases/)",
            "peer_reviewed": False,
            "counts": {k: len(v) for k, v in
                       [("map", mp), ("interventions", iv), ("negatives", T["negative_results_register"]),
                        ("conflicts", T["conflicts_register"]), ("corrections", corr),
                        ("leads", leads), ("open_leads", [L for L in leads if (L.get("current_status") or "").upper().startswith("OPEN")]),
                        ("references", refs), ("open_questions", T["open_questions"])]},
        },
        "vocab": {
            "sections": counts([d["section"] for d in mp]),
            "evidence_tiers": counts([(d.get("evidence_tier") or "").split(" (")[0] for d in mp]),
            "verdict_classes": counts([d.get("verdict_class") for d in iv]),
            "domains": counts([d.get("domain") for d in iv]),
            "unmet_needs": counts([d["unmet_need_codes"] for d in iv]),
            "evidence_levels": counts([d.get("evidence_level") for d in refs]),
        },
        "map": mp,
        "interventions": iv,
        "negatives": rows(T["negative_results_register"], "NEG"),
        "conflicts": rows(T["conflicts_register"], "CF"),
        "leads": leads,
        "corrections": corr,
        "triage": rows(T["lead_candidate_triage"], id_col="key"),
        "public_record_check": rows(T["public_record_check"], "PRC"),
        "open_questions": rows(T["open_questions"], "OQ"),
        "references": refs,
    }
    with open(outfile, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
    return payload, outfile
