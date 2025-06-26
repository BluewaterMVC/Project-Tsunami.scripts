<!-- Language Bar (automated on commit) -->

{{lang_url_bar}}

---

<!-- File Header Metadata Block (automated on commit) -->

{{file_header_block}}

---

# 📂 Project-Driven Documentation Location Source Architecture

This document defines the architectural approach for using the Bluewater Scripts GitHub Project board as the authoritative source for all documentation file locations, status, and task management—eliminating the need for static mapping files and enabling reliable, real-time automation.

---

## 1. Purpose & Rationale

Traditional mapping files for tracking documentation status and file locations quickly fall out of sync with reality, especially as teams and content scale.
**Project-driven location sourcing** establishes the GitHub Project board (or table) as the single source of truth for:

* The canonical location and path of each documentation file
* File and documentation status (e.g., NOT STARTED, IN PROGRESS, IN REVIEW, PUBLISHED)
* Additional metadata (title, category, maintainers, etc.)

All automation, validation, and reporting should reference this live project data instead of error-prone static maps.

---

## 2. GitHub Project Structure & Fields

* **Custom Field: `location`**
  Stores the full, relative path and filename for each documentation file (e.g., `/docs/en/architecture/status/checklists.md`)
* **Custom Field: `status`**
  Reflects the documentation workflow stage (see [Documentation Status Policy](../status/documentation-status-policy.md))
* **Other Recommended Fields:**

    * `title`
    * `type` (e.g., Task, Epic, Doc)
    * `assignee`
    * `reviewer`
    * `priority`
    * `last updated`
    * `related tasks`

**Organization:**

* Every documentation task corresponds to a project item with a valid `location`.
* The Project board is the definitive index of all docs—there is no secondary mapping file.

---

## 3. Architectural Requirements

* **Canonical Source:**
  All scripts and automations (e.g., status checkers, doc generators, translators) must consume their file lists and metadata from the GitHub Project API, not from local mapping files.
* **Sync & Validation:**
  Automation should periodically (or on-demand) validate that each project `location` exists in the repo and that all files are accounted for.
* **Real-Time Status:**
  Documentation status, review, and progress should be visualized and tracked via the project board, and rendered in dashboards or reports as needed.
* **Change Triggers:**
  Any update to a `location` or status field can trigger downstream automation (e.g., update file status header, notify translation teams).
* **Automated Metadata Sync:**  
  The file header metadata block in each documentation file is automatically managed by project automation and always reflects the authoritative status and path as tracked on the GitHub Project board. For header format and marker details, see [Header and Metadata Policy](../status/header-policy.md).

---

## 4. System Workflow

```mermaid
flowchart TD
    A[GitHub Project Board] -->|API Query| B[Automation Script]
    B -->|Reads location field| C[Repo Docs Directory]
    B -->|Updates status| C
    C -->|Sync/validate| D[Status Reports/Dashboards]
    B -->|Notify| E[Maintainers/Translators]
````

---

## 5. Benefits & Justification

* **Zero drift:** All changes are centralized and visible in real time.
* **No manual mapping file maintenance:** The board is always the ground truth.
* **Integrated project management:** Docs are never “orphaned” from tasks or owners.
* **Automatable:** Easy to build scripts/tools that scale with the project.

---

## 6. Architectural Constraints

* Requires all contributors to use and maintain the project board for doc work.
* Automation must be resilient to missing or malformed `location` fields (fail gracefully).
* GitHub API access tokens must have appropriate permissions.

---

## 7. Cross-References

* [Documentation Status Policy](../status/documentation-status-policy.md)
* [Header and Metadata Policy](../status/header-policy.md)
* [Onboarding Automation](../workflow/onboarding-automation.md)
* [Sync/Automation Reference](../workflow/sync-reference.md)
* [Checklist Templates](../status/checklists.md)

---

## 8. Maintenance & Governance

* The architecture team must periodically review project board usage and enforce consistent custom field use.
* Significant changes to the workflow or fields must be documented here and communicated to all teams.

---

{{last_updated}}
