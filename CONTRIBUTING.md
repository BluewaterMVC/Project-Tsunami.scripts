<!-- Language Bar (automated on commit) -->
{{lang_url_bar}}

---

<!-- File Header Metadata Block -->
{{file_header_block}}

---

<img src="docs/en/assets/bw-git-banner.png" alt="Bluewater"/>

# 🌊 Contributing to Bluewater Scripts

Thank you for your interest in contributing to **Bluewater Scripts**!
This repository provides the shared automation, CI/CD, and language management scripts that support the entire Bluewater project ecosystem.
**Please read this guide carefully before submitting issues, code, or documentation.**

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Where to Start](#where-to-start)
3. [General Guidelines](#general-guidelines)
4. [Script Style & Standards](#script-style--standards)
5. [Documentation Standards](#documentation-standards)
6. [Pull Requests](#pull-requests)
7. [Issues & Feature Requests](#issues--feature-requests)
8. [Sync, Integration & Tooling](#sync-integration--tooling)
9. [Licensing](#licensing)
10. [Contact](#contact)

---

## Code of Conduct

Participation in this project is governed by our 
[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).
We expect all contributors to treat others with respect, inclusivity, and professionalism.

---

## Where to Start

* **New to Bluewater Scripts?** Start with the 
[README.md](README.md).
* Review open [issues](../../issues) and [pull requests](../../pulls).
* See our [GOVERNANCE.md](GOVERNANCE.md) for how decisions are made.

---

## General Guidelines

* **Be respectful** and keep all discussions professional.
* Always search for existing [issues](../../issues) before creating new ones.
* For major changes or features, open an issue or [discussion](../../discussions) first.
* Contributions are welcome for Python, Bash/Shell, or Batch scripts as appropriate.

---

## Script Style & Standards

* All scripts **must** be cross-platform whenever possible.
* **Python** is the preferred language for new automation, unless system-level integration or performance requires Bash/Shell or Batch.
* Script headers should clearly indicate the language, author, and a short description.
* Use clear, modular, maintainable code—well-commented and following the [PEP8](https://peps.python.org/pep-0008/) style guide for Python, and best practices for shell and batch scripts.
* Provide sample usage in the script’s docstring or as a comment at the top.
* **Security:** Do not include sensitive data, and always validate input where relevant.
* Scripts that directly modify files must be safe, non-destructive, and provide clear error messages.
* **No PHPDoc required in this repository**; focus on language-appropriate documentation.

---

## Documentation Standards

* All documentation for scripts must reside in `/docs/{lang}/technical/` or `/docs/{lang}/architecture/` as appropriate.
* Each script or tool must have:

    * A clear description of its purpose, usage, and configuration options.
    * Examples for installation and execution.
    * Any platform-specific requirements or caveats.
* Keep documentation up to date as scripts change.
* Markdown (`.md`) is required for all documentation.

---

## Pull Requests

* Fork the repository and create a new branch for your change.
* Follow the PR template for your contribution type (feature, bugfix, docs, etc.).
* Ensure all code is tested, and passes all CI checks (linting, security, etc.).
* Link relevant issues by number (`Closes #123`).
* Keep PRs focused—one logical change per PR.
* All PRs must:

    * Update documentation as needed.
    * Pass linting and security checks.
    * Provide a clear summary of the purpose and impact.
* PRs that do not meet these criteria will be reviewed, but may be closed or asked for revision.

---

## Issues & Feature Requests

* Before submitting, search [existing issues](../../issues) to avoid duplicates.
* Provide clear, descriptive titles and context.
* For documentation or workflow issues, specify affected scripts or files.
* Use the provided issue templates to speed up triage.
* Be constructive—describe *why* and *how* the change is needed.

---

## Sync, Integration & Tooling

* This repository is the **single source of truth** for all shared automation and workflow scripts.
* Scripts may be distributed to other Bluewater repositories via onboarding/setup scripts, submodules, or manual copy as described in the [README.md](./README.md).
* Do not break backward compatibility or repo integration without discussion.
* Coordinate with maintainers for major changes that affect downstream repositories.
* **Automation scripts may be called by CI/CD pipelines, Git hooks, or contributors locally.**
  Ensure your scripts are robust, well-documented, and provide clear output for all platforms.

---

## Licensing

* Contributions are accepted under the [Open Software License (OSL 3.0)](./LICENSE).
* Do not submit code you are not legally entitled to contribute.
* All files must retain their license headers and copyright.

---

## Contact

* For help, use [GitHub Discussions](../../discussions) or open an [issue](../../issues).
* For sensitive matters, email the core team: [contact@bluewatermvc.org](mailto:contact@bluewatermvc.org)

---

> **All contributions—code, documentation, and scripts—are reviewed for compliance with these standards.
> Thank you for making Bluewater Scripts better!**

---

{{last_updated}}
