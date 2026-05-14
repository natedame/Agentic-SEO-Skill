# Changelog

All notable changes to this project should be documented here.

## Unreleased

### Added

- CI workflow for Python syntax compilation, inventory validation, and reference freshness checks.
- Inventory validator for README/SKILL/script drift.
- Reference freshness validator for `resources/references/`.
- Governance files: contributing guide, code of conduct, security policy, support guide, citation metadata, issue templates, pull request template, CODEOWNERS, and Dependabot configuration.

### Changed

- Documented script inventory now reflects 36 scripts: 35 Python scripts plus one shell helper.
- Release packaging workflow now only publishes for `v*` tags.
- `.gitignore` now excludes common Python caches, build output, generated SEO reports, screenshots, traffic archives, and local credentials.

### Fixed

- Added missing freshness markers to reference files that lacked `<!-- Updated: YYYY-MM-DD -->`.
