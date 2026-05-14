# Agentic SEO Skill Wiki

This wiki is the reader-facing guide for Agentic SEO Skill `v3.0.0`.

The runtime source of truth remains the repository payload:

- `SKILL.md`
- `scripts/`
- `resources/`

The wiki exists to explain how to install, run, interpret, and release the skill without making the README larger.

## What This Skill Does

Agentic SEO Skill provides deterministic, LLM-first SEO audits for:

- Websites and single pages
- Blog posts and editorial content
- Technical SEO checks
- Schema.org JSON-LD validation and generation
- Core Web Vitals and performance evidence
- Image SEO and visual checks
- E-E-A-T, GEO, and AEO reviews
- GitHub repository SEO and discoverability

The package currently includes 16 sub-skills, 10 specialist agents, and 89 scripts.

## Most Useful Pages

- [[Installation]]: install targets, release packages, optional dependencies.
- [[Command Reference]]: supported `seo ...` commands.
- [[Audit Workflow]]: what to run for page, site, article, and GitHub audits.
- [[Reports and Outputs]]: how to interpret generated reports.
- [[Script Inventory]]: script groups and when to use them.
- [[Release and Packaging]]: what ships in release archives.
- [[Troubleshooting]]: common failures and fixes.

## Expected Audit Outputs

Full and page audits should normally produce:

- `FULL-AUDIT-REPORT.md`
- `ACTION-PLAN.md`

When the HTML report generator is used, it also produces:

- `SEO-REPORT.html`

GitHub repository audits may produce:

- `GITHUB-SEO-REPORT.md`
- `GITHUB-ACTION-PLAN.md`

## Release Package Contents

Release archives intentionally include only the runtime skill payload:

- `SKILL.md`
- `scripts/`
- `resources/`

Repository-only files such as tests, CI configuration, governance docs, and local generated audit output are not needed inside an installed skill bundle.

