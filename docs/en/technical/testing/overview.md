<!-- Language Navigation Bar (automated on commit) -->

{{lang\_url\_bar}}

---

<!-- File Header Metadata Block (automated on commit) -->

{{file\_header\_block}}

---

# 🧪 Bluewater Scripts Testing Overview

This document defines the **testing philosophy, standards, and workflows** for all automation scripts and tooling in the Bluewater Scripts repository, regardless of language.
It is the entry point for understanding testing expectations across Python, Bash, Batch, PHP, and any other automation components.

---

## 1. Philosophy

* **Quality is Non-Negotiable:**
  Every script or tool—regardless of language—must be testable, verifiable, and safely maintainable.
* **Automated & Repeatable:**
  Tests must be runnable by automation (CI/CD), locally and in team workflows.
* **Language-Specific, Unified Principles:**
  Testing tools and approaches will differ by language, but all share the same standard of coverage, reliability, and review.

---

## 2. General Testing Requirements

* **Test All Core Logic:**
  Every script must have one or more automated tests covering main features and edge cases.
* **Continuous Integration (CI):**
  All tests are run on every Pull Request and before merging to `main`.
* **No Manual Testing Alone:**
  Manual testing is allowed only as a supplement, never as a replacement for automated tests.
* **Documentation:**
  Each test suite must be documented in the corresponding language-specific guide.

---

## 3. Supported Languages & Test Environments

| Language | Test Tool(s)             | Reference Guide                     |
|----------|--------------------------|-------------------------------------|
| Python   | `pytest`                 | [Python Testing Guide](./python.md) |
| Bash     | `bats`                   | [Bash Testing Guide](./bash.md)     |
| Batch    | [Recommended: `batunit`] | [Batch Testing Guide](./batch.md)   |
| PHP      | `phpunit`                | [PHP Testing Guide](./php.md)       |
| Other    | (Document as adopted)    | To be added                         |

> If you add a new language or tool, create a corresponding `testing/<language>.md` file and update this table.

---

## 4. Directory Structure & Naming

* All tests must reside in `/tests/` or `/tests/<language>/` subfolders.
* Test files must clearly indicate the language/tool and script being tested.
* Use descriptive function names and maintain clear organization.

---

## 5. How to Run Tests

* **Python:**
  See [Python Testing Guide](./python.md) for setup and usage.
* **Bash:**
  See [Bash Testing Guide](./bash.md) for details on `bats`.
* **Batch:**
  See [Batch Testing Guide](./batch.md).
* **PHP:**
  See [PHP Testing Guide](./php.md) for `phpunit` usage.

**All contributors should ensure their code passes all relevant tests before submitting a Pull Request.**

---

## 6. References & Further Reading

* [CONTRIBUTING.md](/CONTRIBUTING.md)
* [CI Configuration](../../.github/workflows/)
* [Python Testing Guide](./python.md)
* [Bash Testing Guide](./bash.md)
* [Batch Testing Guide](./batch.md)
* [PHP Testing Guide](./php.md)

---

{{last_updated}}
