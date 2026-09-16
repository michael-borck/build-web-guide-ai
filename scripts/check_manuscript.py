#!/usr/bin/env python3
"""Regression checks for the revised manuscript (stdlib only).

Focuses on the defects found in the 2026-09-16 developmental audit:
rendered-numbering alignment for chapters and exercises, stale links,
the broken Bootstrap CDN listings, and the series build issues.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHAPTERS = [
    "index.qmd",
    "copyright.qmd",
    "chapters/reading-list.qmd",
    "acknowledgments.qmd",
    "chapters/chapter-ai-web-partner.qmd",
    "chapters/chapter-structure.qmd",
    "chapters/chapter-presentation.qmd",
    "chapters/chapter-behaviour.qmd",
    "chapters/chapter-connection.qmd",
    "projects/project-portfolio.qmd",
    "chapters/chapter-why-cms.qmd",
    "chapters/chapter-wordpress-platform.qmd",
    "chapters/chapter-extending-platforms.qmd",
    "chapters/chapter-headless-architecture.qmd",
    "projects/project-business-site.qmd",
    "chapters/chapter-component-thinking.qmd",
    "chapters/chapter-rapid-development.qmd",
    "chapters/chapter-professional-practices.qmd",
    "projects/project-react-integration.qmd",
    "chapters/chapter-emerging-technologies.qmd",
    "chapters/chapter-development-career.qmd",
    "chapters/chapter-ai-era-developer.qmd",
    "references.qmd",
    "about-author.qmd",
]

STALE_LINKS = (
    "michaelborck.dev",
    "michaelborck.education",
    "ship-it-python-in-production",
    "developer.css-tricks.com",
)


def skip_appledouble(paths):
    return [p for p in paths if not p.name.startswith("._")]


def chapter_text(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


class ManuscriptChecks(unittest.TestCase):
    def test_no_stale_links(self):
        for name in CHAPTERS + ["README.md", "CLAUDE.md"]:
            text = (ROOT / name).read_text(encoding="utf-8")
            for target in STALE_LINKS:
                with self.subTest(file=name, target=target):
                    self.assertNotIn(target, text)

    def test_no_mermaid_diagrams(self):
        for name in CHAPTERS:
            with self.subTest(file=name):
                self.assertNotIn("{mermaid}", chapter_text(name))

    def test_no_stale_part_scheme(self):
        for name in CHAPTERS:
            text = chapter_text(name)
            for match in re.finditer(r"\*\*Part \d+\*\*|\bPart 0\b", text):
                with self.subTest(file=name, ref=match.group(0)):
                    self.fail(f"stale part scheme: {match.group(0)}")

    def test_exercise_numbers_match_rendered_chapters(self):
        rendered = {
            "chapters/chapter-ai-web-partner.qmd": 1,
            "chapters/chapter-structure.qmd": 2,
            "chapters/chapter-presentation.qmd": 3,
            "chapters/chapter-behaviour.qmd": 4,
            "chapters/chapter-connection.qmd": 5,
            "chapters/chapter-why-cms.qmd": 7,
            "chapters/chapter-wordpress-platform.qmd": 8,
            "chapters/chapter-extending-platforms.qmd": 9,
            "chapters/chapter-headless-architecture.qmd": 10,
            "chapters/chapter-component-thinking.qmd": 12,
            "chapters/chapter-rapid-development.qmd": 13,
            "chapters/chapter-professional-practices.qmd": 14,
            "chapters/chapter-emerging-technologies.qmd": 16,
            "chapters/chapter-development-career.qmd": 17,
            "chapters/chapter-ai-era-developer.qmd": 18,
        }
        for name, number in rendered.items():
            text = chapter_text(name)
            found = re.findall(r"Exercise \d+\.", text)
            expected = f"Exercise {number}."
            with self.subTest(file=name):
                self.assertTrue(found, f"{name}: no exercises found")
                self.assertTrue(
                    all(item == expected for item in found),
                    f"{name}: {sorted(set(found))} do not match {expected}",
                )

    def test_chapter_references_stay_in_range(self):
        for name in CHAPTERS:
            text = chapter_text(name)
            for match in re.finditer(r"\bChapter (\d+)\b", text):
                number = int(match.group(1))
                with self.subTest(file=name, ref=match.group(0)):
                    self.assertTrue(1 <= number <= 18,
                                    f"{match.group(0)} out of range")

    def test_no_multiline_cdn_urls(self):
        # Bootstrap CDN hrefs were broken across lines, producing
        # invalid URLs with embedded whitespace.
        for name in CHAPTERS:
            text = chapter_text(name)
            for match in re.finditer(r'href=[^>]*\n[^>]*cdn\.jsdelivr', text):
                with self.subTest(file=name):
                    self.fail("multiline CDN URL")

    def test_bootstrap_demo_uses_single_line_urls(self):
        text = chapter_text("chapters/chapter-rapid-development.qmd")
        self.assertIn("bootstrap@5.3.3/dist/css/bootstrap.min.css", text)
        self.assertIn("bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js", text)

    def test_download_links_are_site_absolute(self):
        config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
        for target in ("build-web-guide-ai.pdf",
                       "build-web-guide-ai.epub"):
            with self.subTest(target=target):
                self.assertIn(f"href: /{target}", config)
                self.assertNotIn(f"href: {target}", config)

    def test_custom_stylesheet_ships(self):
        self.assertTrue((ROOT / "assets" / "custom.css").is_file())

    def test_source_encoding_is_utf8(self):
        paths = skip_appledouble(sorted(ROOT.glob("**/*.qmd")))
        for path in paths:
            if "_book" in path.parts or "_print_source" in path.parts:
                continue
            with self.subTest(file=str(path)):
                path.read_text(encoding="utf-8")


if __name__ == "__main__":
    unittest.main(verbosity=2)
