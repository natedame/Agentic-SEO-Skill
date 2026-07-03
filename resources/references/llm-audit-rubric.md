<!-- Updated: 2026-05-14 -->

# LLM Audit Rubric

Use this rubric for all SEO analyses to keep outputs consistent across:
- full-site audits
- single-page audits
- blog/article audits

## 1) Scope

Define the audit scope before analyzing:
- `full-site`: multiple pages, technical + content + structure
- `single-page`: one URL, on-page + technical + content
- `article`: one post, editorial quality + intent match + metadata

State scope in the first paragraph of the report.

## 2) Evidence Standard

Base every finding on explicit evidence. For each finding, include:
- `Finding`: concise issue statement
- `Evidence`: observable proof (HTML element, metric, URL, script output)
- `Impact`: SEO consequence (indexing, ranking, CTR, UX, crawl efficiency)
- `Fix`: concrete implementation step

If evidence is missing, mark as `Unknown` instead of guessing.

## 3) Confidence Labels

Attach one confidence label to each finding:
- `Confirmed`: directly observed in source/script output
- `Likely`: strong signal but incomplete verification
- `Hypothesis`: possible issue requiring additional checks

Never present `Likely` or `Hypothesis` as confirmed facts.

## 4) Severity Rules

Apply consistent severity:
- `Critical`: indexing blocked, severe rendering/crawl failures, major schema breakage
- `Warning`: important optimization opportunity with measurable impact
- `Pass`: meets expected baseline
- `Info`: contextual note or not-applicable item

Escalate to `Critical` only when clear evidence shows direct search-impacting failure.

## 5) Prioritization Method

Prioritize fixes using:
- `Impact`: expected SEO outcome if fixed
- `Effort`: implementation complexity/time
- `Dependency`: prerequisite ordering

Classify action items:
- `Quick win`: high impact, low effort
- `Strategic`: high impact, higher effort
- `Maintenance`: medium/low impact, low urgency

## 6) Scoring Policy

Use scores as directional summaries, not absolute truth.
- include category scores only when evidence is sufficient
- explain score penalties in plain language
- avoid precision theater (for example, avoid unsupported decimal-heavy scoring)

If data is incomplete, show `Score confidence: Low`.

## 7) Output Contract (Required)

Use this report structure in order.

### A) Audit Summary
- scope
- overall rating / score band
- top 3 issues
- top 3 opportunities

### B) Findings Table

Columns:
- Area
- Severity
- Confidence
- Finding
- Evidence
- Fix

### C) Prioritized Action Plan

List actions in execution order:
1. immediate blockers
2. quick wins
3. strategic improvements

### D) Unknowns and Follow-ups

List open checks needed to move `Likely/Hypothesis` to `Confirmed`.

## 8) Area Checklist

Evaluate these areas when in scope:
- crawlability and indexability
- on-page metadata and heading structure
- internal linking and information architecture
- Core Web Vitals and performance signals
- structured data quality and eligibility
- image optimization and accessibility
- content quality and E-E-A-T signals
- GEO/AI citation readiness signals

## 9) Anti-Hallucination Guardrails

Do not claim:
- rankings, traffic, or penalties without explicit data
- PageSpeed/CrUX values without measured output
- competitor facts without sources

When uncertain, say exactly what data is missing and how to collect it.

## 10) Reusable Finding Template

Use this block for each major issue:

```text
[Area] <name>
Severity: <Critical|Warning|Pass|Info>
Confidence: <Confirmed|Likely|Hypothesis>
Finding: <one sentence>
Evidence: <specific proof>
Impact: <why this matters>
Fix: <clear implementation step>
```

## 11) Binary-Checklist Scoring Protocol

Score every category from a FIXED yes/no checklist with a fixed denominator — never from invented, self-capped signal tallies. This is the CheckEval pattern (decompose into independent binary checks, roll up mechanically): reproducible run-to-run because the denominator does not float, and debuggable because you can see exactly which checks failed. Each category score produced here is what the weighted rollup in `resources/config/scoring.json` averages into the overall SEO Health Score.

**Why the old ratio was replaced:** `base_score = positive_count / (positive_count + deficit_count)` let the model invent BOTH counts (each capped at "max 5"), so the same page scored differently depending on how many signals it happened to name. A fixed checklist removes that floating denominator.

**For each scored category:**

### Step 1 — Fix the checklist FIRST (before looking at the score)
- If the category has a pre-authored yes/no checklist, use it EXACTLY (E-E-A-T → `eeat-framework.md` "Signals to Check"; GEO → `seo-geo.md` per-dimension signal lists). Do not add, drop, cap, or reorder items.
- If the category has no pre-authored list, enumerate its checks into an explicit yes/no list and FREEZE it before scoring. No "max 5" cap — list every real check.
- The frozen list length is the fixed denominator (`total`).

### Step 2 — Answer each item independently
For each checklist item record:
- **pass / fail** — a genuine binary (pass = the page satisfies it). If an item is truly N/A for this page type, mark **N/A** and exclude it from the denominator, noting why.
- **Evidence** — one specific proof from the page or script output.
- **Confidence** — Confirmed / Likely / Hypothesis. Never score a Hypothesis as a pass.

### Step 3 — Roll up mechanically
```
category_score = round(100 × passed / total)      # total = frozen checklist length − genuine N/A
```
No pos/(pos+deficit), no self-cap: same page, same checklist → same score every run.

### Step 4 — Apply severity penalties (unchanged)
- Each **Critical** finding: −15 points
- Each **Warning** finding: −5 points
- Maximum penalty cap: −50 (floor = 0)
```
final_score = max(0, category_score − (critical_count × 15) − (warning_count × 5))
```

### Step 5 — Show the derivation
State `passed/total` and the failed items so the number is auditable:

> "On-Page 71: 5/7 checks pass; failed — missing JSON-LD schema (Critical, −15), two images lacking alt text (Warning×2, −10). Final 46."

> **Rule (N/A is bounded — it must not become a denominator-shrink loophole):** mark an item **N/A only when it is genuinely inapplicable to this page type** (not merely inconvenient or failing — a failing item is a **fail**, never an N/A). Hard ceiling: **if more than 1/3 of a category's checklist is N/A, the category scores `Insufficient data`**, not a passed/total number — so the denominator can't be gamed down silently. Never guess a pass.
