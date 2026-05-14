# Live Audit Example

This example documents a real skill run against:

```text
https://www.hackingdream.net/
```

The installed Codex skill was invoked through the bundled audit runner:

```bash
python3 ~/.codex/skills/seo/scripts/audit_runner.py https://www.hackingdream.net/ --output-dir tmp/live-hackingdream-skill
```

Generated local artifacts:

- `audit-results.json`
- `SEO-REPORT.html`
- `FULL-AUDIT-REPORT.md`
- `ACTION-PLAN.md`

Observed result:

- Overall score: `59/100`
- Confidence: `Medium`
- PageSpeed evidence: blocked by Google API rate limit during that run

How to interpret this:

- The score is useful for prioritization, but findings should still be checked against evidence.
- Rate-limited checks are not confirmed site defects.
- The action plan should separate confirmed issues from unknowns.

