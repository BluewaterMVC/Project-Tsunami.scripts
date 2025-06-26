<!-- Language Navigation Bar (automated on commit) -->

{{lang_url_bar}}

---

<!-- File Header Metadata Block (automated on commit) -->

{{file_header_block}}

---

# 📑 Bluewater Scripts: File Header & Metadata Policy

This document defines the **standards, required fields, placement, and automation policies** for the file header metadata block that appears at the top of all documentation files in the Bluewater Scripts repository.
It ensures consistent, up-to-date, and machine-readable metadata for every document in all languages.

---

## 1. Purpose & Goals

* **Single Source of Metadata:**
  Establish a uniform, automated metadata block for every doc to support traceability, status tracking, versioning, and automation.
* **Automation-First:**
  Eliminate manual drift and error by assigning header management to scripts, not contributors.
* **Machine & Human Readability:**
  Ensure both automated tooling and project contributors can quickly find document status, scope, and authorship.

---

## 2. Header Block Fields & Format

Every documentation file must begin with the following metadata block, directly below the language navigation bar (if present):

```markdown
📄 **File:** /path/to/file.md  
🔄 **Status:** IN PROGRESS  
🕒 **Updated:** YYYY-MM-DD  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – All Contributors  
👨‍💻 **Author:** Bluewater Team
```

**Field Definitions:**

* **File:** Full repo path, always relative from repo root
* **Status:** Current workflow status (see [Documentation Status Policy](./documentation-status-policy.md)); e.g. NOT STARTED, IN PROGRESS, IN REVIEW, PUBLISHED, NEEDS UPDATE, DEPRECATED
* **Updated:** Last modification date (auto-set by automation)
* **Version:** Semantic version or doc version (auto or config)
* **Scope:** Audience and visibility, e.g., Public, Internal, Translation Team
* **Author:** Primary authors/maintainers (can be default or configured)

---

## 3. Placement & Template Use

* **Always appears as the very first Markdown block** (after the language banner)
* **NEVER manually edited by contributors**
* Contributors place a `{{file_header_block}}` placeholder in new files; automation replaces or updates this placeholder.
* If missing, automation should insert the block and notify contributor.

---

## 4. Status Field Workflow

* **Statuses include:**

    * NOT STARTED (empty or placeholder files)
    * IN PROGRESS (actively authored, but not ready for review)
    * IN REVIEW (under peer/maintainer review)
    * PUBLISHED (approved and current)
    * NEEDS UPDATE (detected out of date by automation or flagged by contributors)
    * DEPRECATED (marked for deprecation, not deleted)
* **Transitions** are managed by automation based on workflow events (see [Documentation Status Policy](./documentation-status-policy.md))

---

## 5. Versioning & Change Tracking

* **Version:** Updated when content changes, major updates, or structural changes occur.
* Use [Semantic Versioning](https://semver.org/) for major doc sets; patch version can auto-increment with script logic.
* **Updated:** Field is always set to the last commit date that modified the file.

---

## 6. Extensibility & Custom Fields

* New fields may be proposed and added via architectural review.
* All scripts must tolerate unrecognized fields (for forward compatibility).
* Custom fields (e.g., reviewer, language team, review deadline) can be added as project needs grow, but must be documented here and in technical docs.

---

## 7. Automation Policy

* **Automation is authoritative:**

    * Only scripts update or create the metadata block.
    * Manual edits to the header are discouraged and may be overwritten.
* **Pre-commit hook or CI job**:

    * Scans files for the `{{file_header_block}}` tag.
    * Inserts or updates the block according to policy.
    * Updates status, date, and any other required metadata.
* All automation must reference this document and [file-header-automation.md](../../technical/file-header-automation.md).

---

## 8. Manual Overrides & Exceptions

* In rare cases (emergencies, custom workflow), maintainers may override automation with a documented reason.
* Such changes must be reviewed and reverted to automated control as soon as feasible.

---

## 9. References & Cross-links

* [Documentation Status Policy](./documentation-status-policy.md)
* [Checklist Templates](./checklists.md)
* [Workflow Automation Architecture](../workflow/workflow-automation.md)
* [Technical Header Automation Guide](../../technical/file-header-automation.md)
* [System Overview](../system-overview.md)

---

{{last_updated}}
