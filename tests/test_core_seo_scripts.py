import importlib.util
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sitemap_generator_urlset():
    sitemap_generator = load_script("sitemap_generator")
    xml = sitemap_generator.build_urlset([
        {"url": "https://example.com/", "lastmod": "2026-05-15"},
        {"url": "https://example.com/about"},
    ])

    assert "<loc>https://example.com/</loc>" in xml
    assert "<lastmod>2026-05-15</lastmod>" in xml
    assert xml.count("<url>") == 2


def test_url_quality_flags_tracking_and_facets():
    url_quality = load_script("url_quality")
    result = url_quality.analyze_urls([
        "https://example.com/Products/List?utm_source=x&sort=price&color=red",
    ])

    row = result["rows"][0]
    assert "uppercase_path" in row["flags"]
    assert "tracking_parameters" in row["flags"]
    assert "facet_parameters" in row["flags"]
