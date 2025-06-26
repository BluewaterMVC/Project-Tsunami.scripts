{{lang_url_bar}}

---

{{file_header_block}}

---

# 🏷️ File Header Automation

This document provides a comprehensive guide for implementing and maintaining the **automated metadata header block** (`{{file_header_block}}`) in Bluewater Scripts documentation.  
It describes how the system ensures every file is consistently labeled, up-to-date, and compliant with project metadata standards.

---

## 1. Purpose

Automating the file header block guarantees all documentation includes standardized metadata such as file path, status, version, and authorship. This supports searchability, auditability, translation tracking, and transparency across the project.

---

## 2. Scope

This process applies to **all Markdown documentation files** (root, architecture, technical, i18n, etc.) in the Bluewater Scripts repository and is enforced for all language trees.

---

## 3. What is the File Header Block?

The **file header block** is an automated section at the top of each document. It replaces the `{{file_header_block}}` tag with up-to-date metadata:

```

📄 **File:** /docs/en/technical/file-header-automation.md
🔄 **Status:** In Progress
🕒 **Updated:** 2025-07-01
🔖 **Version:** 1.0
📦 **Scope:** 🌐 Public – All Contributors
👨‍💻 **Author:** Bluewater Team

````

**Do not hand-edit this block.**  
All changes are made by the automation process on commit or push.

---

## 4. Automation Process Overview

### a. **Trigger Points**

- On every commit or push, the pre-commit hook or CI job:
    - Scans files for the `{{file_header_block}}` placeholder.
    - Replaces it with a rendered header containing up-to-date metadata.
    - Updates the header if any metadata changes (file path, date, status, etc.).

### b. **How Values are Determined**

| Field   | Source/Logic                                                                     |
|---------|----------------------------------------------------------------------------------|
| File    | Calculated from repo path; always absolute from project root                     |
| Status  | Detected by script: Not Started, In Progress, In Review, Published, Needs Update |
| Updated | Set to last commit affecting the file                                            |
| Version | Default is `1.0`; can be overridden in config or tags                            |
| Scope   | Default or set per repo/config (e.g., "Public – All Contributors")               |
| Author  | Default is "Bluewater Team"; can be set in config or contributor list            |

### c. **Automation Responsibilities**

- Insert or update the header block.
- Prevent manual drift—warn if hand edits are detected.
- Support root and language-specific files.
- Log all automated changes (for CI traceability).

---

## 5. Setup & Configuration

### a. **Pre-commit Hook / CI Workflow**

- Use the provided Python (or shell) script located at `/tools/file-header-update.py`.
- Add to the `.pre-commit-config.yaml` or your project’s CI workflow (see `/.github/workflows/`).
- Configuration file:  
  - Defaults can be set in `/tools/config/header-config.yml`.

### b. **Manual Overrides**

- Rarely needed.  
- If required, document in a YAML frontmatter block above the header (automation will preserve these).

---

## 6. Error Handling & Troubleshooting

- **Missing `{{file_header_block}}`:** Script will insert the block at the top after any language banner.
- **Header Drift/Manual Edit:** Script will overwrite and log a warning.
- **Config Errors:** CI fails with error message and link to documentation.
- **Unsupported File Types:** Skipped with notice.

---

## 7. Handling Translations

- The header block is rendered per file, per language.
- The `Status:` field reflects translation status if under `/docs/{lang}/`.
- Automation updates all corresponding translated files upon source changes (see [Translation Status Policy](../architecture/i18n/translation-status-policy.md)).

---

## 8. Example Automation Script Usage

```shell
python3 tools/file-header-update.py --all
````

* Scans all docs, updates/inserts header blocks as needed.

Add to pre-commit in `.pre-commit-config.yaml`:

```yaml
-   repo: local
    hooks:
      - id: file-header-update
        name: Update File Header Block
        entry: python3 tools/file-header-update.py
        language: python
        files: \.md$
```

---

## 9. References & Cross-links

* [Header and Metadata Policy](/docs/en/architecture/status/header-policy.md)
* [Documentation Status Policy](/docs/en/architecture/status/documentation-status-policy.md)
* [Checklist Templates](/docs/en/architecture/status/checklists.md)
* [Translation Status Policy](/docs/en/architecture/i18n/translation-status-policy.md)
* [Onboarding Automation](/docs/en/architecture/workflow/onboarding-automation.md)
* [Technical Scripts Usage](/docs/en/technical/git-scripts-usage.md)

---

{{last_updated}}
