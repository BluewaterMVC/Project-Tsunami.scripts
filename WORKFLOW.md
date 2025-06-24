<!-- Language Bar (automated on commit) -->
{{lang_url_bar}}

---

<!-- File Header Metadata Block -->
{{file_header_block}}

---

# Bluewater Project Workflow

This document defines the **canonical workflow** for all contributors and maintainers working with the Bluewater project.
Adherence to this workflow is required for all code, documentation, translation, and process changes.

---

## Table of Contents

1. [Overview](#overview)
2. [Branching & Version Control](#branching--version-control)
3. [Development Workflow](#development-workflow)
4. [Documentation Workflow](#documentation-workflow)
5. [Translation & Localization Workflow](#translation--localization-workflow)
6. [Automated Tools & Sync Process](#automated-tools--sync-process)
7. [Integration with Project Management Tools](#integration-with-project-management-tools)
8. [Pull Request Process](#pull-request-process)
9. [Quality Standards & Review](#quality-standards--review)
10. [Release & Versioning](#release--versioning)
11. [Roles & Responsibilities](#roles--responsibilities)
12. [References](#references)

---

## Overview

Bluewater is a multi-repository, multi-language platform consisting of:

* **bluewater-framework:** All source code, code-level documentation (PHPDoc), and technical assets.
* **bluewater-docs:** All architecture, governance, workflow, and user-facing documentation.

This workflow document is **binding** for all contributors and maintainers.
**Deviations must be discussed and approved by project governance.**

---

## Branching & Version Control

* The `main` branch is always deployable and protected.
* All work must be performed in branches, following this pattern:

    * `feature/short-description`
    * `bugfix/short-description`
    * `docs/short-description`
    * `i18n/lang-xx-description`
    * `refactor/short-description`
* Pull Requests (PRs) must originate from a fork or branch and reference a clear issue number if applicable.
* **All changes must be tracked via Git and follow [Conventional Commits](https://www.conventionalcommits.org/).**

---

## Development Workflow

1. **Fork** the relevant repository and create a descriptive branch.
2. **Write code:**

    * Adhere to [PSR-12](https://www.php-fig.org/psr/psr-12/) and all [Bluewater PHPDoc standards](./docs/en/contribute/phpdoc.md).
    * Use `declare(strict_types=1);` at the top of every PHP file.
    * Commit frequently with meaningful messages.
3. **Test thoroughly:**

    * Write and run unit/integration tests.
    * Run code quality tools and static analyzers.
4. **Document:**

    * Ensure all classes, methods, and components include complete, up-to-date PHPDoc.
    * Update relevant user/architecture documentation in `/docs/{lang}` as needed.
5. **Push changes** and open a Pull Request following the PR workflow.

---

## Documentation Workflow

* All documentation (architecture, governance, workflow, technical, user) must reside in `/docs/{lang}` (where `{lang}` is the language code, e.g., `en`).
* **Every code or architectural change must be accompanied by updated documentation.**
* Use clear Markdown (`.md`) and follow Bluewater’s doc formatting standards.
* Major documentation changes require peer review and may require translation updates.
* **All documentation changes are validated and, where possible, auto-checked for completeness and proper formatting using automated scripts and CI.**

---

## Translation & Localization Workflow

* Bluewater supports multi-language documentation and user interfaces.
* All language folders under `/docs/{lang}` must mirror the structure of the `en` (English) source.
* Use the [i18n sync tools](./tools/i18n/README.md) and maintain the language list in `lang.yml`.
* Translators should update only their language folders and follow placeholder conventions until content is available.
* All code examples in translations must comply with [PHPDoc standards](./docs/en/contribute/phpdoc.md).
* **Automated scripts detect out-of-sync documentation and missing language trees.**

---

## Automated Tools & Sync Process

* **Automation is core to Bluewater’s quality and consistency.**
* The `/tools/i18n/sync_docs_structure.py` script enforces consistency and structure for all language directories based on `lang.yml`.
* **On every commit or PR affecting `/docs/` or language configuration:**

    * Automated checks verify directory structure, presence of placeholder files, and content synchronization.
    * Scripts automatically update `mkdocs.yml` and `requirements.txt` to reflect supported languages.
    * Contributors are notified via CI of any discrepancies or required manual intervention.
* Do **not** edit generated files or directory structures by hand—always use the automation scripts.
* For workflow details and troubleshooting, see [SYNC\_PROCESS.md](./SYNC_PROCESS.md) and [Tools README](./tools/i18n/README.md).
* **All automation scripts are tracked and versioned in the repository, with usage described in their respective READMEs.**

---

## Integration with Project Management Tools

* **Issues and Pull Requests**:

    * All development, documentation, and translation work must be tracked via GitHub Issues and Pull Requests.
    * Each commit, branch, and PR should reference the corresponding issue number (e.g., `Closes #123`).
    * Use [issue templates](.github/ISSUE_TEMPLATE/README.md) and [PR templates](.github/PULL_REQUEST_TEMPLATE/) for consistency.
* **Boards & Projects**:

    * Project Boards are used to plan, track, and review work for each milestone and release.
    * Contributors should move issues and PRs through columns as work progresses.
* **Labels and Milestones**:

    * Apply appropriate labels (e.g., `bug`, `enhancement`, `docs`, `i18n`) and set milestones where applicable.
* **Automated Status Checks**:

    * CI/CD is integrated with GitHub to run checks for tests, code standards, PHPDoc compliance, and documentation structure.
    * Status checks must pass before merge approval.

---

## Pull Request Process

1. Ensure your branch is up to date with the latest `main`.
2. Open a Pull Request:

    * Use the correct PR template for your change type (`feature`, `bugfix`, `docs`, `i18n`, etc.).
    * Complete all checklist items, including references to documentation and [PHPDoc standards](./docs/en/contribute/phpdoc.md).
    * Link to relevant issues and reference project boards/milestones as needed.
    * Provide a clear description and summary of changes.
3. Your PR will be reviewed for:

    * Code quality and compliance.
    * Complete and accurate PHPDoc.
    * Updated documentation and translations as required.
    * Passing all automated checks (CI, linter, sync, documentation).
    * Alignment with project goals and standards.
4. Revisions may be requested. Once approved, the PR will be merged by a maintainer.

---

## Quality Standards & Review

* **PHPDoc compliance** is enforced for all code via automation and manual review.
* All documentation must be clear, accurate, and match the prescribed templates.
* Tests, code coverage, and CI results must pass before merge.
* All changes must respect the [Code of Conduct](./CODE_OF_CONDUCT.md) and [GOVERNANCE.md](./GOVERNANCE.md).
* Project boards and dashboards are monitored for stalled, outdated, or conflicting work.

---

## Release & Versioning

* All significant changes are versioned using [Semantic Versioning](https://semver.org/).
* Release notes and the [CHANGELOG.md](./CHANGELOG.md) are updated with every release.
* Tag releases appropriately and update any language or documentation artifacts affected.
* Automated scripts and release pipelines may be used to generate artifacts, deploy documentation, and notify stakeholders.

---

## Roles & Responsibilities

* **Contributors:**

    * Write code, documentation, and translations according to standards.
    * Participate in code and doc reviews.
    * Submit issues and propose improvements.
    * Use project boards and GitHub tools for tracking and status updates.
* **Maintainers:**

    * Review PRs for quality, completeness, and standards compliance.
    * Manage releases and coordinate cross-repository changes.
    * Enforce governance, workflow, and documentation policies.
    * Oversee automation scripts and tooling.
* **Translators:**

    * Maintain accuracy and currency of language folders.
    * Ensure translated docs stay in sync with English source structure.
    * Flag or open issues for missing or unclear original content.
    * Use automation scripts for structure validation.

---

## References

* [CONTRIBUTING.md](./CONTRIBUTING.md)
* [PHPDoc Standards](./docs/en/contribute/phpdoc.md)
* [SYNC\_PROCESS.md](./SYNC_PROCESS.md)
* [Tools README](./tools/i18n/README.md)
* [GOVERNANCE.md](./GOVERNANCE.md)
* [Code of Conduct](./CODE_OF_CONDUCT.md)
* [Semantic Versioning](https://semver.org/)
* [PSR-12](https://www.php-fig.org/psr/psr-12/)

---

> **This workflow is binding for all contributors and maintainers.
> For questions or clarifications, open an issue or contact project leadership.
> All code and documentation must comply with the PHPDoc guide, documentation structure, and governance standards.
> Automation and integration with project management tools are mandatory for quality and transparency.**

---

{{last_updated}}
