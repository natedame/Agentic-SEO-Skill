# Installation

Use the latest release package when installing for normal use.

Current release: `v3.0.0`

Release page:

https://github.com/Bhanunamikaze/Agentic-SEO-Skill/releases/tag/v3.0.0

## Codex

```bash
curl -fsSLO https://raw.githubusercontent.com/Bhanunamikaze/Agentic-SEO-Skill/main/install.sh
bash install.sh --online --ref v3.0.0 --target codex --force
```

This installs the skill at:

```text
~/.codex/skills/seo
```

## Claude

```bash
curl -fsSLO https://raw.githubusercontent.com/Bhanunamikaze/Agentic-SEO-Skill/main/install.sh
bash install.sh --online --ref v3.0.0 --target claude --force
```

This installs the skill at:

```text
~/.claude/skills/seo
```

## Project-Scoped Install

```bash
bash install.sh --online --ref v3.0.0 --target project --project-dir /path/to/project --force
```

Project targets include Antigravity, Cowork, Cursor, Windsurf, Continue, Copilot, and Cline formats.

## Windows PowerShell

```powershell
iwr https://raw.githubusercontent.com/Bhanunamikaze/Agentic-SEO-Skill/main/install.ps1 -OutFile install.ps1
pwsh ./install.ps1 --online --ref v3.0.0 --target codex --force
```

## Optional Dependencies

The core scripts use Python and common parsing/network libraries.

Install optional runtime dependencies from a checkout when needed:

```bash
python3 -m pip install -r requirements.txt
```

Visual analysis needs Playwright:

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
```

## What Gets Installed

Only these paths are required by the skill runtime:

- `SKILL.md`
- `scripts/`
- `resources/`

Tests, CI files, issue templates, and governance files are repository maintenance assets and are not part of installed skill bundles.

