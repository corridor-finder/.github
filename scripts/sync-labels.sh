#!/usr/bin/env bash
# Creates or updates the standard labels in every Corridor Finder repository.
# Requires the GitHub CLI (`gh auth login`) with permission to edit labels.
# Usage: scripts/sync-labels.sh [--dry-run] [repo ...]
set -euo pipefail

ORG="corridor-finder"
DRY=0
if [[ "${1:-}" == "--dry-run" ]]; then DRY=1; shift; fi

REPOS=("$@")
if [[ ${#REPOS[@]} -eq 0 ]]; then
  REPOS=(corridor-finder corridor-finder-registry corridor-finder-api corridor-finder-web .github)
fi

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
while IFS=$'\t' read -r name color description; do
  [[ -z "$name" ]] && continue
  for repo in "${REPOS[@]}"; do
    cmd=(gh label create "$name" --color "$color" --description "$description" --repo "$ORG/$repo" --force)
    if [[ $DRY -eq 1 ]]; then printf '%q ' "${cmd[@]}"; echo; else "${cmd[@]}"; fi
  done
done < "$HERE/../labels.tsv"
