"""Turn the Studio Desk's saved edits into CLAUDE/WEBSITE/overrides.json.

The Studio Desk (https://claude.ai/artifact/LdsMioQyopHQUNfhYQPA7C) keeps one document per
piece in its database. When Greg presses Publish, Claude exports the products collection
with ArtifactData (list, out_dir=dashboard/export) and runs:

    python3 apply.py            # writes overrides.json from dashboard/export/products/*.json

Then: generate/build_products.py (prices), checkout/build.py --deploy (prices charged),
generate/museum_emit.py (site), checkout/deploy_site.py --deploy --launch (live), and the
dirty flags in the desk are cleared.

overrides.json holds every field the desk edits, for every piece. Price is used by
build_products.py and the checkout worker; track, story, details and the SEO fields are for
museum_emit.py to read (the website agent wires those).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "overrides.json"
FIELDS = ("price", "track", "story", "details", "seoTitle", "seoDescription")


def main():
    files = sorted((HERE / "export" / "products").glob("*.json"))
    if not files:
        raise SystemExit("No export found in dashboard/export/products")
    over, changed = {}, []
    for f in files:
        doc = json.load(open(f))
        body = doc.get("data", doc)
        slug = doc.get("id") or f.stem
        over[slug] = {k: body[k] for k in FIELDS if k in body}
        if body.get("dirty"):
            changed.append(slug)
    OUT.write_text(json.dumps(over, indent=1, ensure_ascii=False))
    print("%d pieces -> %s; changed since last publish: %s" % (len(over), OUT.name, ", ".join(changed) or "none"))


if __name__ == "__main__":
    main()
