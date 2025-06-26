<!-- Language Bar (automated on commit) -->
{{lang_url_bar}}

---

<!-- File Header Metadata Block (automated on commit) -->
{{file_header_block}}

---

# 📑 Bluewater Documentation Status Policy

This document defines the **official policy and automation standards** for tracking, updating, and displaying the status of all documentation files in the Bluewater Scripts repository and downstream projects.
It describes recognized status states, automation workflows, update triggers, and contributor responsibilities, ensuring visibility, accountability, and quality throughout the documentation lifecycle.

---

## 1. 🎯 Purpose

* **Applies to:** All documentation files in English and all translations, across all directories and language trees.
* **Goal:**
  * Track the lifecycle of every doc: `NOT STARTED` → `IN PROGRESS` → `IN REVIEW` → `PUBLISHED`
  * Ensure out-of-date docs are flagged as `NEEDS UPDATE`
  * Enforce consistency, transparency, and auditability via automation

---

## 2. Status Lifecycle & Definitions

Every documentation file must declare its current lifecycle status via the file header block. The following statuses are supported:

| Icon | Status         | Meaning                                      |
|------|----------------|----------------------------------------------|
| 🟠   | `NOT STARTED`  | File is a placeholder, stub, or outline only |
| 🟡   | `IN PROGRESS`  | Initial draft or content under development   |
| 🟦   | `IN REVIEW`    | Draft submitted, pending review and feedback |
| 🟢   | `PUBLISHED`    | Approved, current, and in active use         |
| 🔄   | `NEEDS UPDATE` | Outdated, requires update to stay current    |
| 🗑️  | `DEPRECATED`   | Obsolete, replaced, or scheduled for removal |
| 📦   | `ARCHIVED`     | No longer maintained, retained for reference |

> **Note:** Additional statuses may be introduced as project needs evolve.

---

## 3. Automation Policy

### a. **Empty or Reserved Files**

* When a documentation file is **created and left empty** (no content but whitespace), automation will:

  * Insert `{{lang_url_bar}}` and `{{file_header_block}}` at the top
  * Set status to `NOT STARTED`
  * Insert a placeholder body:

    ```markdown
    > **TODO:** This page has not yet been authored.  
    > Content will be added soon.
    <!-- Do not remove this placeholder. It is managed by automation. -->
    ```

### b. **Transition to IN PROGRESS**

* When any **substantive content** (beyond the placeholder) is added, automation changes the status to `IN PROGRESS`.

### c. **Transition to IN REVIEW**

* When a Pull Request or explicit review is initiated and marked as “ready for review,” status transitions to `IN REVIEW`.

### d. **Transition to PUBLISHED**

* Once approved and merged, and all checks pass, status is set to `PUBLISHED`.

### e. **Transition to NEEDS UPDATE**

* If the English source or any referenced file changes, or if automation detects out-of-date content, status is set to `NEEDS UPDATE` for affected docs (including translations).

### f. **Manual Override**

* **Manual status changes are NOT permitted.**
  Status can only be updated by automation or designated workflow scripts.

### g. **Deprecation Block**

* No documentation file is hard deleted.
* If deprecated:

  * Status is set to `DEPRECATED` (🗑️).
  * Insert a deprecation block, reason, and deprecation date at the top:

    ```markdown
    > **DEPRECATED:** This page is obsolete as of YYYY-MM-DD.  
    > Reason: [Replacement or reason here.]
    <!-- Managed by documentation automation. -->
    ```

---

## 4. Status Block Placement

* The **file header block** containing the status is always inserted (and updated) automatically at the top of each doc file, immediately following the language navigation bar.
* Authors must **never edit the block by hand**; use `{{file_header_block}}` placeholder only.
* If the placeholder is missing, automation inserts both the language bar and the header block automatically.

**Sample Render:**
```markdown
📄 **File:** /docs/en/architecture/status/document-status-policy.md  
🔄 **Status:** 🟦 In Review  
🕒 **Updated:** 2025-07-01  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public  
👨‍💻 **Author:** Bluewater Team
```

---

## 5. Policy for Translations

* Translated docs follow the same status flow as English docs.
* If a translation is missing or outdated, status will be set to `NOT STARTED` or `NEEDS UPDATE` as appropriate, with a localized placeholder message.

---

## 6. Sample: Reserved/Empty File

**Example placeholder for a new doc:**

```markdown
{{lang_url_bar}}
{{file_header_block}}

> **TODO:** This page has not yet been authored.  
> Content will be added soon.
<!-- Do not remove this placeholder. It is managed by automation. -->
```

---

## 7. 🔄 Triggers for Status Change

* **On file creation:** Set to `NOT STARTED` if empty.
* **On commit:** Script inspects changes, updates status if needed.
* **On merge:** Sets `PUBLISHED`.
* **On upstream change:** Sets downstream/translation files to `NEEDS UPDATE`.
* **On scheduled review:** Optional automation can revalidate doc age/currency.

---

## 8. 🛡️ Policy for Deprecated or Deleted Docs

* No documentation file is ever hard deleted.
* Deprecated docs must:

  * Set status to `DEPRECATED`.
  * Insert a clear deprecation block, reason, and date.
  * Update all language variants accordingly.

**Example Deprecation Block:**

```markdown
> **DEPRECATED:** This page is obsolete as of 2025-08-01.  
> Reason: Replaced by [new-feature.md](./new-feature.md)
<!-- Managed by documentation automation. -->
```

---

## 9. 🔗 Cross-Links & References

* [Header and Metadata Policy](../status/header-policy.md)
* [Checklist & Template Docs](../status/checklists.md)
* [Internationalization Policy](../i18n/i18n-policy.md)
* [Translation Status Policy](../i18n/translation-status-policy.md)
* [Workflow Automation Architecture](../workflow/workflow-automation.md)
* [Onboarding Automation](../workflow/onboarding-automation.md)
* [Notification and Team Assignment Policy](../notification/notification-policy.md)
* [Glossary](../contributors/glossary.md)

---

## 10. 📋 Example Status Banner Table

Automation may also render an at-a-glance summary:

| Document                 | Status          | Last Updated |
|--------------------------|-----------------|--------------|
| system-overview\.md      | 🟢 PUBLISHED    | 2025-07-01   |
| roadmap-extensibility.md | 🟦 IN REVIEW    | 2025-06-30   |
| i18n-policy.md           | 🔄 NEEDS UPDATE | 2025-06-29   |

---

## 11. 🚧 Review & Update

* This policy is reviewed every quarter, or as the project evolves.
* Suggestions and improvement PRs are welcome!

---

{{last_updated}}
