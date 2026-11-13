# AROL Studio Desk

Private editor for A Rock on a Lens piece prices, descriptions and search listings.

This repository is a **code backup only**. The desk runs on claude.ai, where it stores its data;
opened anywhere else it cannot load or save anything.

- `studio.html` — the desk page (published as a claude.ai artifact with the `db` and `user` capabilities).
- `apply.py` — turns an export of the desk's saved pieces into `overrides.json` for the website build.

Publishing to arockonalens.com happens from Claude Code ("publish the studio desk"), which follows
the steps in `CLAUDE/WEBSITE/GO_LIVE_PLAN.md`. No prices, customer data or keys are kept here.
