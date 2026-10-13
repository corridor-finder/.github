#!/usr/bin/env python3
"""Validates the community-health files in this repository. Requires PyYAML."""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors: list[str] = []
warnings: list[str] = []

REQUIRED_FILES = [
    "LICENSE", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "SECURITY.md",
    "PULL_REQUEST_TEMPLATE.md", "profile/README.md", "labels.tsv",
    "ISSUE_TEMPLATE/config.yml",
]
BODY_TYPES = {"markdown", "textarea", "input", "dropdown", "checkboxes"}


def err(msg: str) -> None:
    errors.append(msg)


def load_yaml(path: pathlib.Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf8"))
    except yaml.YAMLError as exc:
        err(f"{path.relative_to(ROOT)}: invalid YAML: {str(exc).splitlines()[0]}")
        return None


for name in REQUIRED_FILES:
    if not (ROOT / name).is_file():
        err(f"missing required file: {name}")

# Issue forms
for path in sorted((ROOT / "ISSUE_TEMPLATE").glob("*.yml")):
    data = load_yaml(path)
    if data is None:
        continue
    rel = path.relative_to(ROOT)
    if path.name == "config.yml":
        if not isinstance(data.get("blank_issues_enabled"), bool):
            err(f"{rel}: blank_issues_enabled must be true or false")
        for link in data.get("contact_links", []):
            for key in ("name", "url", "about"):
                if not link.get(key):
                    err(f"{rel}: contact link missing '{key}'")
        continue
    for key in ("name", "description", "body"):
        if not data.get(key):
            err(f"{rel}: missing top-level '{key}'")
    ids: set[str] = set()
    for i, item in enumerate(data.get("body") or []):
        kind = item.get("type")
        if kind not in BODY_TYPES:
            err(f"{rel}: body[{i}] has unknown type {kind!r}")
            continue
        attrs = item.get("attributes") or {}
        if kind == "markdown":
            if not attrs.get("value"):
                err(f"{rel}: body[{i}] markdown needs attributes.value")
            continue
        if not attrs.get("label"):
            err(f"{rel}: body[{i}] ({kind}) needs attributes.label")
        item_id = item.get("id")
        if kind != "checkboxes" and not item_id:
            err(f"{rel}: body[{i}] ({kind}) needs an id")
        if item_id:
            if item_id in ids:
                err(f"{rel}: duplicate id {item_id!r}")
            ids.add(item_id)
        if kind == "dropdown" and not attrs.get("options"):
            err(f"{rel}: body[{i}] dropdown needs options")

# Labels
seen: set[str] = set()
for n, line in enumerate((ROOT / "labels.tsv").read_text(encoding="utf8").splitlines(), 1):
    if not line.strip():
        continue
    cols = line.split("\t")
    if len(cols) != 3:
        err(f"labels.tsv:{n}: expected 3 tab-separated columns, got {len(cols)}")
        continue
    name, color, desc = cols
    if not re.fullmatch(r"[0-9a-f]{6}", color):
        err(f"labels.tsv:{n}: color must be 6 lowercase hex digits")
    if len(desc) > 100:
        err(f"labels.tsv:{n}: description exceeds GitHub's 100 characters")
    if name in seen:
        err(f"labels.tsv:{n}: duplicate label {name!r}")
    seen.add(name)

# Workflows parse
for path in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
    load_yaml(path)

# Relative markdown links resolve
for path in sorted(ROOT.rglob("*.md")):
    if ".git" in path.parts:
        continue
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", path.read_text(encoding="utf8")):
        if re.match(r"[a-z]+:", target):
            continue
        if not (path.parent / target).resolve().exists():
            err(f"{path.relative_to(ROOT)}: broken relative link {target!r}")

# Not an error: a reminder for the maintainers.
if "[INSERT CONTACT METHOD]" in (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf8"):
    warnings.append("CODE_OF_CONDUCT.md still contains [INSERT CONTACT METHOD]; add an enforcement contact.")

for w in warnings:
    print(f"warning: {w}")
if errors:
    print(f"\n{len(errors)} problem(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("All community-health files valid.")
