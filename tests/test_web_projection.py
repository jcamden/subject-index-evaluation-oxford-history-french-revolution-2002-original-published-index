"""Regression tests for the deterministic V7 customer web projection."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import unittest
from decimal import Decimal
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_web_projection as projection_builder  # noqa: E402


OUTPUT = ROOT / "web/v7-published-index"


def load(relative: str) -> dict:
    return json.loads((OUTPUT / relative).read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(str(values["id"]))
        if tag in {"a", "link"} and values.get("href"):
            self.links.append(str(values["href"]))
        if tag == "script" and values.get("src"):
            self.links.append(str(values["src"]))


class WebProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.projection = projection_builder.validate_projection_output(OUTPUT)

    def test_primary_and_secondary_view_roles_are_frozen(self) -> None:
        primary = self.projection["primary_view"]
        secondary = self.projection["secondary_view"]
        self.assertEqual("canonical_as_delivered", primary["view_id"])
        self.assertEqual("primary_observed_evaluation", primary["role"])
        self.assertEqual(72.5, primary["score"])
        self.assertEqual("representation_adjusted", secondary["view_id"])
        self.assertEqual(
            "secondary_counterfactual_representation_view", secondary["role"]
        )
        self.assertEqual(73.5, secondary["score"])
        self.assertTrue(secondary["gate_outcomes_equal_to_primary"])
        self.assertIn("counterfactual", secondary["role"])

    def test_six_canonical_dimensions_match_regression_values(self) -> None:
        actual = [
            (
                row["dimension_id"],
                row["rating"],
                row["awarded_points"],
                row["maximum_points"],
            )
            for row in self.projection["primary_view"]["dimensions"]
        ]
        self.assertEqual(
            [
                ("meaningful_coverage", 3.5, 14, 20),
                ("editorial_selectivity", 3.6667, 11, 15),
                ("conceptual_stance_fidelity", 4, 12, 15),
                ("page_reference_reliability", 3.5, 17.5, 25),
                ("findability_navigation", 3.5, 14, 20),
                ("mechanics_consistency", 4, 4, 5),
            ],
            actual,
        )

    def test_collection_bindings_and_source_order(self) -> None:
        expected_counts = {
            "paths": 1904,
            "headings": 1904,
            "locators": 5338,
            "cross_references": 16,
            "source_subjects": 1366,
        }
        for binding in self.projection["item_grades"]["collections"]:
            collection = load(binding["artifact_path"])
            kind = binding["item_kind"]
            self.assertEqual(expected_counts[kind], collection["count"])
            self.assertEqual(binding["sha256"], digest(OUTPUT / binding["artifact_path"]))
            self.assertEqual(
                list(range(collection["count"])),
                [item["source_order"] for item in collection["items"]],
            )

    def test_every_locator_grade_equals_frozen_combined_credit(self) -> None:
        collection = load("data/locators.v1.json")
        for item in collection["items"]:
            credit = Decimal(item["detail"]["locator_utility"]["combined_credit"])
            grade = Decimal(str(item["grade"]["score"]))
            self.assertEqual(Decimal(100) * credit, grade, item["item_id"])

    def test_defect_caps_and_popover_evidence_are_deterministic(self) -> None:
        for relative in (
            "data/paths.v1.json",
            "data/headings.v1.json",
            "data/cross-references.v1.json",
        ):
            collection = load(relative)
            for item in collection["items"]:
                for factor in item["factors"]:
                    caps = factor.get("severity_caps", [])
                    cap_ids = [cap["defect_id"] for cap in caps]
                    evidence_ids = factor.get("evidence_ids", [])
                    self.assertEqual(sorted(set(cap_ids)), cap_ids, item["item_id"])
                    self.assertTrue(set(cap_ids).issubset(evidence_ids), item["item_id"])
                    self.assertEqual(len(evidence_ids), len(set(evidence_ids)), item["item_id"])

    def test_source_artifact_file_hash_bindings_resolve(self) -> None:
        for binding in self.projection["provenance"]["source_artifacts"]:
            path = ROOT / binding["artifact_path"]
            self.assertTrue(path.is_file(), binding["artifact_path"])
            self.assertEqual(binding["sha256"], digest(path), binding["artifact_path"])

    def test_renderer_is_dependency_free_and_links_local_assets(self) -> None:
        html = (OUTPUT / "index.html").read_text(encoding="utf-8")
        javascript = (OUTPUT / "app.js").read_text(encoding="utf-8")
        self.assertIn('href="styles.css"', html)
        self.assertIn('src="app.js"', html)
        self.assertNotRegex(html, r'<(?:script|link)[^>]+https?://')
        self.assertNotIn("analytics", html.lower())
        self.assertNotIn("telemetry", javascript.lower())
        builder_source = self.projection["builder"]["source"]
        self.assertEqual(
            builder_source["sha256"], digest(ROOT / builder_source["artifact_path"])
        )

    def test_repository_relative_links_resolve(self) -> None:
        parser = LinkParser()
        parser.feed((OUTPUT / "index.html").read_text(encoding="utf-8"))
        for target in parser.links:
            if target.startswith("#"):
                self.assertIn(target[1:], parser.ids, target)
            elif not re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
                self.assertTrue((OUTPUT / target).is_file(), target)

        for markdown, base in (
            (ROOT / "README.md", ROOT),
            (OUTPUT / "README.md", OUTPUT),
        ):
            text = markdown.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
                if target.startswith(("https://", "http://", "#")):
                    continue
                self.assertTrue((base / target).exists(), f"{markdown}: {target}")

    def test_public_safety_scan(self) -> None:
        projection_builder.privacy_scan(OUTPUT)
        safety = self.projection["public_safety"]
        self.assertFalse(safety["source_excerpts_included"])
        self.assertFalse(safety["restricted_files_included"])
        self.assertFalse(safety["third_party_javascript"])
        self.assertFalse(safety["tracking_or_telemetry"])


if __name__ == "__main__":
    unittest.main()
