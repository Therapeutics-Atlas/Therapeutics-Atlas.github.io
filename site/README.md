# Static site for the open record

No frontend dependencies, build step, or backend. The disease pages use derived public-data files
that are preserved alongside their canonical research archives:

```
site/
  index.html        Home — introduces Therapeutics Atlas and lists the diseases studied
  ra.html           #001 Rheumatoid arthritis — plain-language overview
  ipf.html          #002 Idiopathic pulmonary fibrosis — final publication overview
  map.html          shared Treatment Map explorer (selects the RA or IPF public schema)
  site.css          shared base styles for the home and overview pages
  ra_record.json    a copy of ../data/ra_record.json
  ipf_record.json   a copy of ../ipf/data/ipf_record.json
  ipf_overview.md   a byte-identical copy of ../ipf/publication/OVERVIEW.md
```

The visitor path is **Home → disease → Overview → Treatment Map**. Each disease's overview and
explorer read its final public payload. The IPF Overview text is loaded from a byte-identical
site copy of `../ipf/publication/OVERVIEW.md`; its counts, candidates, lead outcome, and actions
come from `ipf_record.json`.

## Run it

```
cd site
python -m http.server 8000     # then open the URL shown by the server
```

Opening the pages by double-clicking will **not** work: browsers block `fetch` from `file://`.
Each page detects this and says so.

## Deploy it

GitHub Pages deploys this folder through `.github/workflows/pages.yml`. The workflow uploads only
`site/`; research and publication files elsewhere in the repository remain repo-only. Public links
to those materials open their canonical paths in the GitHub repository.

## What it does

**Home (`index.html`)** introduces the project and lists the diseases studied. The disease list is
a `DISEASES` array in the page: adding a disease is one entry (number, name, blurb, overview page,
record file). Each card fills its counts by fetching that disease's record, so the numbers stay
live.

**RA Overview (`ra.html`)** is a plain-language reading of the record, not a second copy of the
database. Six flat blocks — what we know, what works, what does not, what is uncertain, what we do
not know, and the preliminary research candidates — read straight through. Each block shows a short
substantive summary of what the research found (in `SECTION_SUMMARY`, synthesised from `SUMMARY.md`
and `phases/` — every claim traceable there, with the caveats that keep it from overstating), the
block's evidence-tier distribution, and a `View these records in the Treatment Map`
link (`map.html?section=<key>`, which opens the explorer pre-filtered to that section). Below the
blocks, the research leads show their status and question and expand for detail. The individual
records themselves live only in the Treatment Map.

**IPF Overview (`ipf.html`)** renders the final publication `OVERVIEW.md` without changing its
scientific text. It also renders the explicit zero-Research-Lead outcome, all 41 investigated
candidates with their held/rejected states, and the 12 retained evidence actions from the public
payload.

**Treatment Map (`map.html`)** is the shared queryable explorer. The default RA configuration
retains its existing nine tabs. `map.html?data=ipf_record.json` selects the IPF schema extension
configuration, including evidence access, therapeutic ceiling, endpoint and measurement states,
retrievability, investigated candidates, screens, and retained actions. In both configurations:

- facets with live counts (section, evidence tier, verdict class, domain, unmet need, evidence
  level, topic) and full-text search across every field of the current tab
- deep links: `map.html#TM-042` or `map.html#RL-01` opens the tab that owns that id and scrolls to
  it, so any single statement can be cited by URL; `map.html?section=works` opens the treatment-map
  tab pre-filtered to one section (the overview's block links use this)
- verbatim citations render as links to PubMed/DOI/registry; label-matched candidates render
  separately, in italics, labelled as possible sources rather than citations
- research leads carry their next steps with the strengthen and falsify criteria inline

## What it deliberately does not do

No symptom lookup, no ranking of treatments, no "what should I take" flow, no filtering that
returns a treatment list in response to a description of a patient. The dataset does not support
those questions, and the framing would convert a record of evidence into advice. If you extend the
viewer, that is the line worth keeping.

Nor does it hide a grade or a caveat. Every statement renders with its evidence tier or verdict
class, and the disclaimer is in the page header on every view, because a deep link means any page
can be someone's first.

## Release constraint

Row ids (`TM-001`, `IV-013`, `REF-077`) are assigned by row order when `build_api.py` runs. They
stay stable if the CSVs are appended to, and break if a CSV is reordered. Once you have published
links, treat CSV row order as part of the public interface.

## Editing

`ra_record.json` is generated — do not hand-edit it. Change the CSVs in `../data/`, re-run
`python -c "import build_api; build_api.build()"`, and copy the result here.

The `RA_TABS` and `IPF_TABS` arrays near the top of `map.html`'s script hold the explorer view configurations:
which dataset a tab reads, which field is its heading, which badges it shows, which fields it lists
and which facets it offers. Adding a tab for a new dataset is one entry in that array. `map.html`
also accepts an optional `?data=<name>.json` (same-folder filename only), so the same explorer can
serve another disease's record without editing it.

`ipf_record.json` and `ipf_overview.md` are generated/publication artifacts — do not hand-edit
them. Rebuild and QA the canonical IPF archive using the commands in `../ipf/README.md`, then copy
the verified outputs into `site/`.

`meta.licence` in the JSON is still `TODO`. The page prints it verbatim, so it will read TODO to
visitors until you set it in `build_api.py`.
