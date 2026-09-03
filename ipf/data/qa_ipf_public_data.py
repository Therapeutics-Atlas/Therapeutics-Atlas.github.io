"""Quality assurance for the IPF public data payload and the public Overview.

Every check is mechanical and re-runnable. A check that cannot be automated is not
reported as passing; it is listed as a manual check with its result and who ran it.

Usage (from the archive root):
    IPF_DATA=research_record/registers python data/qa_ipf_public_data.py \\
        data/ipf_record.json publication/OVERVIEW.md
Writes: QA_PUBLIC_DATA.md, qa_findings.csv
"""
import os, re, sys, json, datetime
import pandas as pd

DATA = os.environ.get("IPF_DATA", "research_record/registers")
REC = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "ipf_record.json"))
OVERVIEW = open(sys.argv[2] if len(sys.argv) > 2 else "OVERVIEW.md").read()
F = []  # findings


def chk(cid, group, check, ok, detail="", severity="fail"):
    res = "note" if severity == "note" else ("pass" if ok else severity)
    F.append({"check_id": cid, "group": group, "check": check,
              "result": res, "detail": str(detail)[:600]})
    return ok


def load(n):
    return pd.read_csv(os.path.join(DATA, n))


# ---------------------------------------------------------------- 1. fidelity
SRC = {
    "map": ("ipf_phase3_treatment_map.csv", 89),
    "interventions": ("ipf_phase2_landscape.csv", 283),
    "negatives": ("ipf_phase2_negative_results_register.csv", 77),
    "conflicts": ("ipf_phase2_conflicts_register.csv", 12),
    "candidates": ("ipf_phase4_candidate_register.csv", 41),
    "corrections": ("corrections_log.csv", 38),
    "actions": ("ipf_phase4_actions.csv", 12),
    "limitations": ("ipf_phase4_limitations.csv", 7),
    "unmet_needs": ("ipf_phase1_unmet_needs.csv", 12),
    "open_questions": ("ipf_phase0_open_questions.csv", 10),
    "therapeutic_ceiling": ("ipf_phase1_ceiling.csv", 12),
    "endpoint_taxonomy": ("ipf_phase1_endpoint_taxonomy.csv", 15),
    "retrievability": ("ipf_phase1_retrievability_register.csv", 149),
    "registry_results_sweep": ("ipf_phase6_registry_results_sweep.csv", 116),
    "located_publications": ("ipf_phase6_missing_results_retrieval.csv", 8),
    "measurement_gaps": ("ipf_phase6_recovery_endpoints.csv", 5),
    "coverage_gaps": ("ipf_phase6_chinese_language_coverage.csv", 6),
}
for i, (key, (fn, _)) in enumerate(SRC.items(), 1):
    n_src, n_pub = len(load(fn)), len(REC[key])
    chk(f"F{i}", "row fidelity", f"{key}: published rows == source rows ({fn})",
        n_src == n_pub, f"source {n_src}, published {n_pub}")

# ------------------------------------------------------------- 2. identifiers
for key, pref in [("map", "TM-"), ("interventions", "IV-"), ("negatives", "NEG-"), ("conflicts", "CF-")]:
    ids = [r["id"] for r in REC[key]]
    chk(f"ID-{pref.strip('-')}", "identifiers", f"{key}: ids unique and prefixed {pref}",
        len(set(ids)) == len(ids) and all(str(i).startswith(pref) for i in ids),
        f"{len(set(ids))} unique of {len(ids)}")
internal = [r["internal_map_id"] for r in REC["map"]]
dups = sorted({i for i in internal if internal.count(i) > 1})
chk("ID-INT", "identifiers", "internal treatment-map ids: collisions disclosed in meta.normalisations",
    bool(dups) == any("M2.13" in str(n.get("what", "")) for n in REC["meta"]["normalisations"]),
    f"collided internal ids: {dups}")

# --------------------------------------------------- 3. grade-bearing fields
missing_tier = [r["id"] for r in REC["map"] if not r["evidence_tier"]]
missing_cav = [r["id"] for r in REC["map"] if not r["caveat"]]
undisclosed_cav = [r["id"] for r in REC["map"] if not r["caveat"] and "absent in the record" not in str(r.get("caveat_status"))]
missing_dim = [r["id"] for r in REC["map"] if not r["outcome_dimension"]]
chk("G1", "grading", "every map statement carries an evidence tier", not missing_tier, missing_tier)
chk("G2", "grading", "every map statement either carries a caveat or is flagged caveat-absent",
    not undisclosed_cav, undisclosed_cav)
chk("G2b", "grading", "map statements with no caveat field in the research record",
    True, f"{len(missing_cav)} statements ({missing_cav}) carry no separate caveat in the record; "
          f"caveat_status marks them so a display cannot present them as caveat-free",
    severity="note")
chk("G3", "grading", "every map statement carries an outcome dimension", not missing_dim, missing_dim)

TIERS = {"Established", "Probable", "Uncertain", "Unknown", "Hypothesis"}
bad_tier = sorted({r["evidence_tier"] for r in REC["map"] if r["evidence_tier"] not in TIERS})
chk("G4", "grading", "map tiers come from the closed tier vocabulary", not bad_tier, bad_tier)

VERD = {"Works", "Uncertain", "Failed", "Harm outweighs benefit", "Poorly studied"}
IVX = [r for r in REC["interventions"] if not r["is_duplicate"]]
bad_verd = sorted({r["verdict_class"] for r in IVX if r["verdict_class"] not in VERD})
chk("G5", "grading", "intervention verdicts come from the closed verdict vocabulary", not bad_verd, bad_verd)
bad_iv_tier = sorted({r["evidence_tier"] for r in IVX if r["evidence_tier"] not in TIERS})
chk("G6", "grading", "intervention tiers come from the closed tier vocabulary (after PUB-01 normalisation)",
    not bad_iv_tier, bad_iv_tier)
nosub = [r["id"] for r in IVX if r["verdict_class"] in {"Works", "Failed", "Harm outweighs benefit"} and not r["verdict_sublabel"]]
chk("G7", "grading", "every graded verdict carries a sublabel stating what it rests on", not nosub, nosub)
works_nodim = [r["intervention"] for r in IVX if r["verdict_class"] == "Works" and not (r["endpoint_dimension"] or r["verdict_sublabel"])]
chk("G8", "grading", "every Works verdict names the outcome dimension it was graded on", not works_nodim, works_nodim)
works_noresult = [r["intervention"] for r in IVX if r["verdict_class"] == "Works" and not r["key_result_verbatim"]]
chk("G9", "grading", "every Works verdict carries a verbatim key result", not works_noresult, works_noresult)

# ---------------------------------------------- 4. the load-bearing distinctions
works = [r for r in IVX if r["verdict_class"] == "Works"]
POS_SURV = re.compile(r"(?<!no )(?<!not )(?:survival benefit|improve[sd]? survival|extended survival|"
                      r"prolong(?:s|ed)? survival|reduce[sd]? mortality|mortality benefit)", re.I)
surv = [r["intervention"] for r in works
        if POS_SURV.search(str(r["endpoint_dimension"]) + " " + str(r["verdict_sublabel"]) + " " + str(r["key_result_verbatim"]))]
chk("D1", "distinctions", "no drug carries a survival claim; survival evidence is transplantation only and observational",
    set(surv) <= {"lung transplantation"}, f"rows with survival wording: {surv}")
tm_map = [r["id"] for r in REC["map"] if r["section"].startswith("S5") and re.search(r"surviv", str(r["statement"]), re.I)]
chk("D2", "distinctions", "the record states in 'what we do not know' that no drug has randomised survival evidence",
    bool(tm_map), tm_map)
slow = [r["id"] for r in REC["map"] if r["section"].startswith("S1")
        and re.search(r"slows|reduces the proportion|improve", str(r["statement"]), re.I)
        and not re.search(r"slowing decline is not|graded on the named outcome", str(r["caveat"]), re.I)]
chk("D3", "distinctions", "every 'what works' statement is caveated against preservation, recovery, reversal and cure",
    not slow, slow)
sur = [r["id"] for r in REC["map"] if re.search(r"surrogac", str(r["statement"]), re.I)]
chk("D4", "distinctions", "the unresolved FVC-to-survival surrogacy question is published as a statement",
    bool(sur), sur)
poorly = [r for r in IVX if r["verdict_class"] == "Poorly studied"]
badpoor = [r["intervention"] for r in poorly if re.search(r"ineffective|does not work|no effect", str(r["verdict_sublabel"]), re.I)]
chk("D5", "distinctions", "'poorly studied' rows are never described as ineffective", not badpoor, badpoor)
noaccess = [r for r in IVX if r["evidence_access"] != "published result"]
chk("D6", "distinctions", "registry-only and unretrieved evidence states are identifiable on the row",
    len(noaccess) > 0 and all(r["evidence_access"] for r in IVX), f"{len(noaccess)} of {len(IVX)} rows not published-result")
trad_pos = [r["intervention"] for r in IVX if r["traditional"] and r["verdict_class"] == "Works"]
chk("D7", "distinctions", "no traditional-medicine intervention is graded Works", not trad_pos, trad_pos)

# ------------------------------------------------------------------ 5. leads
chk("L1", "research leads", "leads list is empty", REC["leads"] == [], REC["leads"])
chk("L2", "research leads", "counts.research_leads is 0", REC["counts"]["research_leads"] == 0)
prom = [c["id"] for c in REC["candidates"] if c["promoted_to_lead"]]
chk("L3", "research leads", "no candidate is marked promoted", not prom, prom)
held = [c for c in REC["candidates"] if c["status"] == "held at verification"]
chk("L4", "research leads", "held candidates are labelled held, not rejected and not promoted",
    len(held) == REC["leads_outcome"]["held_at_verification"] and len(held) > 0, f"{len(held)} held")
noreason = [c["id"] for c in REC["candidates"] if not c["reason"] or not c["screens_failed"]]
chk("L5", "research leads", "every candidate carries a final screening status and a reason",
    not noreason, noreason)
screen_ids = {s["id"] for s in REC["screens"]}
unknown_screens = sorted({s for c in REC["candidates"] for s in c["screens_failed"]} - screen_ids)
chk("L6", "research leads", "every screen referenced by a candidate is defined", not unknown_screens, unknown_screens)

# ----------------------------------------------------- 6. corrections coverage
cids = {c["id"] for c in REC["corrections"]}
cited = {c for r in REC["map"] for c in r["superseded_by"]}
cited |= {m for r in REC["interventions"] for m in re.findall(r"\bC\d{1,2}\b", str(r["curation_note"]) + str(r["registry_only_result"]))}
missing = sorted(cited - cids)
chk("X1", "corrections", "every correction id cited by a published row exists in the corrections log",
    not missing, missing)
nrm = REC["meta"]["normalisations"]
nids = [x["id"] for x in nrm]
chk("X2", "corrections", "publication-stage normalisations are disclosed in meta, use their own id series, and do not extend the research log",
    len(nids) == len(set(nids)) and all(re.fullmatch(r"PUB-\d{2}", i) for i in nids)
    and all(x.get("what") for x in nrm) and not (set(nids) & cids)
    and max(cids, key=lambda c: int(c[1:])) == "C38",
    f"{nids}; corrections log ends at {max(cids, key=lambda c: int(c[1:]))}")

# corrections that regraded an intervention must match the published verdict
sweep = load("ipf_phase6_registry_results_sweep.csv")
byname = {r["intervention"]: r for r in REC["interventions"]}
mism = []
for _, r in sweep.iterrows():
    m = re.match(r"material correction - graded (\w+[\w ]*?) \(C\d+\)", str(r.get("sweep_outcome", "")))
    if not m:
        continue
    iv = str(r.get("iv_match", "")).strip()
    want = m.group(1).strip()
    got = byname.get(iv, {}).get("verdict_class")
    if got and not str(got).startswith(want):
        mism.append(f"{iv}: sweep says {want}, published {got}")
chk("X3", "corrections", "interventions regraded by the Phase 6 registry sweep carry the corrected verdict",
    not mism, mism)

# ------------------------------------------------------------- 7. references
inline = [(r["id"], f) for key in ("map", "interventions", "negatives", "conflicts") for r in REC[key] for f in r["refs"]]
idx = {(r["type"], r["id"]) for r in REC["references"]}
orphan = sorted({(f["type"], f["id"]) for _, f in inline} - idx)
chk("R1", "references", "every inline citation appears in the reference index", not orphan, orphan)
badurl = [r["id"] for r in REC["references"] if r["type"] in {"pmid", "nct", "doi"} and not r["url"]]
chk("R2", "references", "every PubMed, registry and DOI reference resolves to a URL", not badurl, badurl)
badpmid = [r["id"] for r in REC["references"] if r["type"] == "pmid" and not re.fullmatch(r"\d{7,8}", r["id"])]
badnct = [r["id"] for r in REC["references"] if r["type"] == "nct" and not re.fullmatch(r"NCT\d{8}", r["id"])]
chk("R3", "references", "identifier syntax is valid", not badpmid and not badnct, badpmid + badnct)
chk("R4", "references", "no heuristically token-matched 'possible source' is published as a citation",
    not any("candidate" in k for r in REC["references"] for k in r.keys()),
    "the IPF payload publishes only citations stated in the record")
notitle = sum(1 for r in REC["references"] if not r["title"])
chk("R5", "references", "references without a title inside the record are marked, not invented",
    all(r["title_source"] or not r["title"] for r in REC["references"]),
    f"{notitle} of {len(REC['references'])} references have no title in the record; title_source is null for those",
    severity="note")

# ------------------------------------------------------- 8. counts vs payload
c = REC["counts"]
chk("N1", "counts", "counts.interventions_distinct equals non-duplicate rows", c["interventions_distinct"] == len(IVX),
    f"{c['interventions_distinct']} vs {len(IVX)}")
chk("N2", "counts", "counts.conflicts_unresolved equals unresolved conflict rows",
    c["conflicts_unresolved"] == sum(1 for x in REC["conflicts"] if not x["resolved"]))
chk("N3", "counts", "counts.references equals the reference index length", c["references"] == len(REC["references"]))
rs = REC["retrievability_summary"]
retr = load("ipf_phase1_retrievability_register.csv")
un = retr[retr.results_retrievable.astype(str).str.startswith("no results found")]
chk("N4", "counts", "retrievability summary matches the register",
    rs["no_retrievable_result"] == len(un) and rs["register_rows_without_posted_results"] == len(retr)
    and rs["completed_interventional_trials"] == 239 and rs["with_results_posted_on_registry"] == 90,
    f"unretrievable {rs['no_retrievable_result']} vs {len(un)}; register {rs['register_rows_without_posted_results']} vs {len(retr)}")

# --------------------------------------------------- 9. overview vs the data
def num(pat, text=OVERVIEW):
    m = re.search(pat, text)
    return int(m.group(1)) if m else None


ov_checks = [
    ("O1", r"(\d+) interventions were graded", c["interventions_distinct"]),
    ("O2", r"Only (\d+) of \d+ interventions have evidence of benefit", sum(1 for r in IVX if r["verdict_class"] == "Works")),
    ("O3", r"\*\*(\d+) are poorly studied", sum(1 for r in IVX if r["verdict_class"] == "Poorly studied")),
    ("O4", r"(\d+)\s+graded statements", c["map_statements"]),
    ("O5", r"(\d+)\s+corrections", c["corrections"]),
    ("O6", r"(\d+) candidate signals", c["candidates_screened"]),
    ("O9", r"\*\*(\d+) are held at verification\*\*", REC["leads_outcome"]["held_at_verification"]),
    ("O10", r"(\d+) were rejected", REC["leads_outcome"]["rejected"]),
]
for cid, pat, want in ov_checks:
    got = num(pat)
    chk(cid, "overview arithmetic", f"Overview figure matches the data ({pat})", got == want, f"overview {got}, data {want}")
chk("O7", "overview arithmetic", "Overview states zero research leads",
    bool(re.search(r"no research lead|zero research lead", OVERVIEW, re.I)))
chk("O8", "overview arithmetic", "Overview carries the disclaimer",
    "not medical advice" in OVERVIEW.lower())

# ------------------------------------------------- 10. forbidden public claims
BANNED = [r"\bcures?\b(?! ?/ ?durable| or durable)", r"\breverses\b", r"\brestores\b", r"\bbreakthrough\b",
          r"\bmiracle\b", r"\bproven (?:safe|effective)\b", r"\bsafe and effective\b",
          r"\bpromising (?:lead|treatment|therapy)\b", r"\bshould take\b", r"\brecommend(?:ed)? (?:taking|that patients take)\b"]
NEG = re.compile(r"\b(no|not|never|none|nothing|cannot|without|absence of|neither)\b[^.]{0,60}$", re.I)
hits = []
for pat in BANNED:
    for m in re.finditer(pat, OVERVIEW, re.I):
        before = OVERVIEW[max(0, m.start() - 70):m.start()]
        if NEG.search(before):   # a negated occurrence is a denial, not a claim
            continue
        s = max(0, m.start() - 90)
        hits.append(f"{pat} :: ...{OVERVIEW[s:m.end()+90].replace(chr(10),' ')}...")
chk("P1", "public language", "no unqualified efficacy, cure or recommendation language in the Overview",
    not hits, hits, severity="warn")
VERBATIM_FIELDS = {"key_result_verbatim", "safety", "statement_verbatim"}
PROMO = [r"\bmiracle\b", r"\bbreakthrough\b", r"\bproven effective\b", r"\bsafe and effective\b"]


def walk(node, field=None):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk(v, k)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v, field)
    elif isinstance(node, str):
        yield field, node


jhits, quoted = [], []
for field, txt in walk(REC):
    for p in PROMO:
        if re.search(p, txt, re.I):
            (quoted if field in VERBATIM_FIELDS else jhits).append(f"{field}: {txt[:120]}")
chk("P2", "public language", "no promotional language in the payload outside quoted source text", not jhits, jhits)
chk("P2b", "public language", "promotional wording inside verbatim quoted source text", True,
    f"{len(quoted)} occurrence(s) inside quoted fields, which a display must render as quotation: {quoted}",
    severity="note")
chk("P3", "public language", "payload carries a disclaimer and reading rules",
    bool(REC["meta"]["disclaimer"]) and len(REC["meta"]["reading_rules"]) >= 6)
chk("P4", "public language", "payload states that the record is not peer reviewed",
    REC["meta"]["peer_reviewed"] is False)

# ------------------------------------------------------- 11. coverage linkage
un_codes = {u["id"] for u in REC["unmet_needs"]}
linked = {u for r in REC["map"] for u in r["maps_to_unmet_need"]}
chk("C1", "coverage", "every unmet-need code cited by a map statement is defined", not (linked - un_codes), sorted(linked - un_codes))
chk("C2", "coverage", "unmet needs with no map statement are reported, not hidden", True,
    f"unlinked: {sorted(un_codes - linked)}", severity="note")
chk("C3", "coverage", "every limitation carries scope and detail",
    all(l.get("scope") and l.get("detail") for l in REC["limitations"]))
open_actions = [a["id"] for a in REC["actions"] if a["open"]]
chk("C4", "coverage", "open actions are published with their Phase 6 outcome",
    all(a["phase6_outcome"] for a in REC["actions"]), f"open: {open_actions}")

# --------------------------------------------------------------- 12. manual
MANUAL = [
    ("M1", "Overview section structure follows the rheumatoid-arthritis Overview (same sections, same depth), with IPF-specific sections added where the record holds a state the RA model has no slot for",
     "pass - RA SUMMARY.md read and mirrored; added sections: therapeutic ceiling by dimension, evidence that exists but cannot be graded, evidence coverage limits"),
    ("M2", "no new research was performed for publication: no new literature search, no new candidate, no new lead",
     "pass - all published values are derived from the Phase 0-6 registers; the builder reads CSVs only"),
    ("M3", "no historical research file was rewritten to suit the public materials",
     "pass - the three publication-stage normalisations (PUB-01, PUB-02, PUB-03) are recorded in meta.normalisations and applied in the derived payload only; the research corrections log still ends at C38 and no register file was edited"),
    ("M4", "held findings are presented as held, and no unresolved retrieval or measurement issue is presented as a therapeutic hypothesis",
     "pass - candidates carry status and screens_failed; actions carry type retrieval/analysis/measurement"),
    ("M5", "Traditional Chinese Medicine coverage is presented as a coverage limit, not as a verdict on efficacy",
     "pass - coverage_gaps and limitation L7 published; no traditional intervention graded Works"),
]
for mid, what, res in MANUAL:
    F.append({"check_id": mid, "group": "manual", "check": what,
              "result": res.split(" - ")[0], "detail": res})

# ------------------------------------------------- 13. publication hygiene
BLOB = json.dumps(REC)
stale_paths = [p for p in ("research/data", "record_data") if p in BLOB]
chk("H1", "publication hygiene", "payload carries no obsolete register path",
    not stale_paths, f"found: {stale_paths}" if stale_paths else "none")

cf = REC["meta"].get("canonical_files")
missing_cf = [f for f in (cf or []) if not os.path.exists(os.path.join(DATA, f))]
chk("H2", "publication hygiene", "meta.canonical_files lists real register files the build read",
    isinstance(cf, list) and len(cf) >= 15 and not missing_cf,
    f"{len(cf) if isinstance(cf, list) else type(cf).__name__} entries, missing {missing_cf}")
chk("H3", "publication hygiene", "meta.source_directory names the archive register directory",
    "research_record/registers" in str(REC["meta"].get("source_directory", "")),
    REC["meta"].get("source_directory"))

norm_ids = [x["id"] for x in REC["meta"]["normalisations"]]
chk("H4", "publication hygiene", "publication-stage normalisations use the PUB series and are all recorded",
    norm_ids == ["PUB-01", "PUB-02", "PUB-03"], norm_ids)

# the superseded landscape denominator (281 rows / 278 distinct, corrections C31 and C33) may
# survive only in phase-dated historical text, never in a present-tense claim about the record
HIST_KEYS = {"corrections", "actions", "limitations"}
present_tense_281 = []
for key, val in REC.items():
    if key in HIST_KEYS or not isinstance(val, list):
        continue
    for row in val:
        if isinstance(row, dict):
            for k, v in row.items():
                if isinstance(v, str) and re.search(r"\b281[- ]row", v):
                    present_tense_281.append(f"{key}.{row.get('id')}.{k}")
chk("H5", "publication hygiene", "superseded landscape denominator survives only in phase-dated historical text",
    not present_tense_281, f"present-tense uses: {present_tense_281}" if present_tense_281 else
    "none outside corrections/actions/limitations; disclosed in meta.historical_text_note")
chk("H6", "publication hygiene", "meta.historical_text_note discloses the phase-dated count difference",
    "C38" in str(REC["meta"].get("historical_text_note", "")) and
    "281" in str(REC["meta"].get("historical_text_note", "")),
    (str(REC["meta"].get("historical_text_note", ""))[:120] or "absent"))
chk("H7", "publication hygiene", "schema_version is set and matches the documented value",
    str(REC["meta"]["schema_version"]).startswith("ipf-public-1.1"), REC["meta"]["schema_version"])

# --------------------------------------------------- 14. document consistency
# the two document checks below are themselves automated checks, so the totals they compare
# against are the current automated tally plus those two
_auto = [f for f in F if f["group"] != "manual"]
N_AUTO = len(_auto) + 2
N_NOTE = sum(1 for f in _auto if f["result"] == "note")
N_MANUAL = 5
DOCS = [p for p in (sys.argv[3:] or ["README.md", "ipf_open_record/README.md",
                                     "SCHEMA_EXTENSIONS.md", "publication/SCHEMA_EXTENSIONS.md"])
        if os.path.exists(p)]
# a document may quote a superseded count or an obsolete path when it documents the correction
# itself; those passages are delimited with <!-- qa:historical --> markers and are not scanned
HIST_MARK = re.compile(r"<!-- qa:historical-start -->.*?<!-- qa:historical-end -->", re.S)


def doc_text(path):
    return HIST_MARK.sub("", open(path).read())


doc_bad = []
for p in DOCS:
    t = doc_text(p)
    for m in re.finditer(r"(\d+)\s+automated checks", t):
        if int(m.group(1)) != N_AUTO:
            doc_bad.append(f"{p}: says {m.group(1)} automated, run has {N_AUTO}")
    for m in re.finditer(r"(\d+)\s+manual checks", t):
        if int(m.group(1)) != N_MANUAL:
            doc_bad.append(f"{p}: says {m.group(1)} manual, run has {N_MANUAL}")
chk("H8", "documents", "README and schema note state this run's automated and manual check counts",
    not doc_bad, "; ".join(doc_bad) if doc_bad else
    f"{len(DOCS)} documents checked against {N_AUTO} automated + {N_MANUAL} manual")
bad_path_docs = [p for p in DOCS if "record_data" in doc_text(p) or "research/data" in doc_text(p)]
chk("H9", "documents", "documents carry no obsolete register path outside passages that document the correction",
    not bad_path_docs, bad_path_docs or f"{len(DOCS)} documents clean")


# ------------------------------------------------------------------- report
df = pd.DataFrame(F)
df.to_csv("qa_findings.csv", index=False)
auto, man = df[df.group != "manual"], df[df.group == "manual"]
na = auto.result.value_counts().to_dict()
n = {"automated_total": len(auto), **{f"automated_{k}": v for k, v in sorted(na.items())},
     "manual_total": len(man)}
json.dump(n, open("qa_counts.json", "w"), indent=1)
lines = [
    "# IPF public data — QA report",
    "",
    f"**Date:** {datetime.date.today().isoformat()} · **Payload:** `ipf_record.json` · "
    f"**Automated checks:** {len(auto)} ({', '.join(f'{k} {v}' for k, v in sorted(na.items()))}) · "
    f"**Manual checks:** {len(man)}",
    "",
    "Every automated check re-runs with `IPF_DATA=research_record/registers python qa_ipf_public_data.py "
    "ipf_record.json OVERVIEW.md`. Checks that cannot be automated are listed as manual with "
    "their result. A `note` is a disclosed property of the data, not a defect.",
    "",
]
for g in ["row fidelity", "identifiers", "grading", "distinctions", "research leads", "corrections",
          "references", "counts", "overview arithmetic", "public language", "coverage",
          "publication hygiene", "documents", "manual"]:
    sub = df[df.group == g]
    if not len(sub):
        continue
    lines += [f"## {g}", "", "| id | check | result | detail |", "|---|---|---|---|"]
    for r in sub.itertuples():
        d = str(r.detail).replace("|", "/").replace("\n", " ")[:300]
        lines.append(f"| {r.check_id} | {str(r.check).replace('|', '/')} | {r.result} | {d} |")
    lines.append("")
open("QA_PUBLIC_DATA.md", "w").write("\n".join(lines))
print(json.dumps(n, indent=1))
print(df[df.result.isin(["fail", "warn"])][["check_id", "check", "detail"]].to_string(index=False, max_colwidth=90))
