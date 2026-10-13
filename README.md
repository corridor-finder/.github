# .github

Organization-wide community health files for [Corridor Finder](https://github.com/corridor-finder). GitHub applies the files here to every repository in the organization that does not define its own.

| File | Purpose |
| --- | --- |
| `profile/README.md` | The organization's profile page |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` | Default policies |
| `PULL_REQUEST_TEMPLATE.md`, `ISSUE_TEMPLATE/` | Default PR template and issue forms |
| `labels.tsv`, `scripts/sync-labels.sh` | The standard label set (GitHub does not sync labels automatically) |

## Applying the labels

```bash
gh auth login
scripts/sync-labels.sh --dry-run     # show what would run
scripts/sync-labels.sh               # create or update labels in all repositories
```

## Checking changes

```bash
pip install pyyaml
python scripts/validate.py
```

## Maintainer to-do

- Replace `[INSERT CONTACT METHOD]` in `CODE_OF_CONDUCT.md` with a real enforcement contact.
- Enable **private vulnerability reporting** in each repository's Security settings (the policy relies on it).
