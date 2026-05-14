# Script Inventory

The skill ships 89 runtime scripts. The authoritative inventory check is:

```bash
python3 scripts/validate_skill_inventory.py
```

Expected result:

```text
Inventory: 16 skills, 10 agents, 89 scripts (88 Python + 1 shell)
OK: documented inventory matches files on disk.
```

## Core Collection and Reporting

- `audit_runner.py`
- `fetch_page.py`
- `parse_html.py`
- `generate_report.py`
- `finding_verifier.py`
- `seo_common.py`

## Technical SEO and Indexability

- `robots_checker.py`
- `robots_path_tester.py`
- `llms_txt_checker.py`
- `llms_txt_generator.py`
- `canonical_checker.py`
- `redirect_checker.py`
- `indexability_matrix.py`
- `x_robots_header_checker.py`
- `security_headers.py`
- `javascript_render_audit.py`
- `crawl_audit.py`

## Sitemaps, Hreflang, and URL Quality

- `sitemap_checker.py`
- `sitemap_generator.py`
- `hreflang_checker.py`
- `hreflang_sitemap_validator.py`
- `orphan_pages_from_sitemap.py`
- `url_quality.py`
- `faceted_nav_audit.py`

## Performance, Images, and Rendering

- `pagespeed.py`
- `lighthouse_runner.py`
- `lcp_subparts.py`
- `critical_request_chain.py`
- `cache_compression_checker.py`
- `third_party_script_audit.py`
- `font_audit.py`
- `image_inventory.py`
- `image_weight_audit.py`
- `capture_screenshot.py`
- `analyze_visual.py`
- `visual_regression_snapshot.py`
- `mobile_render_checker.py`

## Content, E-E-A-T, GEO, and AEO

- `readability.py`
- `article_seo.py`
- `duplicate_content.py`
- `content_decay_detector.py`
- `content_intent_matcher.py`
- `freshness_checker.py`
- `eeat_signal_checker.py`
- `entity_checker.py`
- `answer_block_scanner.py`
- `citation_readiness.py`
- `topical_cluster_mapper.py`
- `ai_crawler_policy_matrix.py`

## Schema, Local SEO, and Ecommerce

- `validate_schema.py`
- `schema_required_props.py`
- `schema_template_generator.py`
- `schema_diff.py`
- `review_schema_checker.py`
- `rich_results_guard.py`
- `product_schema_checker.py`
- `video_schema_checker.py`
- `collection_page_checker.py`
- `local_seo_checker.py`

## Links and Backlinks

- `internal_links.py`
- `broken_links.py`
- `link_profile.py`
- `anchor_text_audit.py`
- `external_link_quality.py`
- `redirect_backlink_reclaim.py`
- `competitor_gap.py`

## GitHub Repository SEO

- `github_api.py`
- `github_repo_audit.py`
- `github_readme_lint.py`
- `github_community_health.py`
- `github_search_benchmark.py`
- `github_competitor_research.py`
- `github_seo_report.py`
- `github_traffic_archiver.py`
- `github_weekly_scorecard.py`
- `repo_docs_site_checker.py`
- `repo_file_inventory.py`
- `repo_release_seo.py`
- `repo_social_preview_checker.py`
- `repo_topic_suggester.py`

## Validation and Maintenance

- `reference_freshness.py`
- `validate_skill_inventory.py`
- `pre_commit_seo_check.sh`
- `env_loader.py`

