# Contributing to Corridor Finder

Thank you for helping. These guidelines apply to every repository in the organization unless a repository's own `CONTRIBUTING.md` says otherwise.

## Where things live

| Repository | What goes there |
| --- | --- |
| [`corridor-finder`](https://github.com/corridor-finder/corridor-finder) | Product definition, architecture, decisions, roadmap |
| [`corridor-finder-registry`](https://github.com/corridor-finder/corridor-finder-registry) | Sourced anchor and corridor data, schema, validator |
| [`corridor-finder-api`](https://github.com/corridor-finder/corridor-finder-api) | Verifiers and the REST API |
| [`corridor-finder-web`](https://github.com/corridor-finder/corridor-finder-web) | The web application |

## Ground rules

1. **No fabricated information.** Fees, limits, speed, routes, countries and assets appear only when a source supports them, with that source and a date. Unknown is shown as unavailable.
2. **Claim before you start.** Comment on an open issue and wait to be assigned. Do not open a large PR for unassigned work.
3. **Stay in scope.** Do what the issue says. Propose anything else as a separate issue.
4. **Tests and docs ship with the change.**
5. **Run the repository's `pnpm check` before pushing.** It runs what CI runs.
6. **AI-assisted work is welcome, unreviewed AI output is not.** You are responsible for every line and every data value you submit, and you must be able to explain them. Never submit data you did not verify against its source.

## Pull requests

Link the issue (`Closes #123`), fill in the PR template, keep the PR focused, and respond to review. Maintainers aim to review within a few working days.

## Conduct and security

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Report vulnerabilities as described in [SECURITY.md](SECURITY.md).

## Licensing

Code is Apache-2.0. Data in the registry is CC BY 4.0. By contributing you agree your contribution is licensed the same way.
