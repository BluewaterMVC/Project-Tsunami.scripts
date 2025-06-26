<!-- Language Bar (automated on commit) -->
{{lang_url_bar}}

---

<!-- File Header Metadata Block (automated on commit) -->
{{file_header_block}}

---

# ✅ Bluewater Documentation Checklists

This document provides **canonical checklists for documentation authoring, status transitions, automation, and review**  
in the Bluewater Scripts ecosystem.  
Checklists support contributors and automation in maintaining consistency, auditability, and compliance across all project documentation.

---

## Table of Contents

1. [Authoring Checklist](#authoring-checklist)
2. [Review Checklist](#review-checklist)
3. [Status Transition Checklist](#status-transition-checklist)
4. [Automation Checklist](#automation-checklist)
5. [References](#references)

---

## 1. Authoring Checklist

Use this checklist **when creating or updating any documentation file**:

- [ ] Add the `{{lang_url_bar}}` at the top of the file.
- [ ] Insert the `{{file_header_block}}` placeholder immediately after the language bar.
- [ ] Write clear, concise, and accurate content following Bluewater’s Markdown standards.
- [ ] Provide code samples, diagrams, or references where relevant.
- [ ] Ensure that links and cross-references resolve and are up to date.
- [ ] If translating, use the correct `/docs/{lang}/` directory and maintain source structure.
- [ ] Run documentation linting and formatting tools as required.

---

## 2. Review Checklist

**For reviewers or maintainers:**  
Verify the following **before approving a PR** involving documentation:

- [ ] Metadata header is present and in correct format (wrapped in HTML comment markers).
- [ ] Status field in the header block is correct for current workflow stage.
- [ ] Content meets quality, accuracy, and completeness requirements.
- [ ] All required cross-links and references are present.
- [ ] Automation has updated metadata fields (status, date, version, etc.).
- [ ] If file is deprecated, deprecation notice and date are present as per policy.
- [ ] Translation files, if present, are up to date with source.

---

## 3. Status Transition Checklist

**Use these checks at each documentation status change:**

| Transition                | Trigger/Event                       | Required Actions                                   |
|---------------------------|-------------------------------------|----------------------------------------------------|
| NOT STARTED → IN PROGRESS | Initial substantive content added   | Update status in header; remove placeholder notice |
| IN PROGRESS → IN REVIEW   | PR opened and marked for review     | Set status in header to IN REVIEW                  |
| IN REVIEW → PUBLISHED     | PR approved and merged              | Set status in header to PUBLISHED                  |
| Any → NEEDS UPDATE        | Source doc changes/out-of-date flag | Set status in header to NEEDS UPDATE               |
| Any → DEPRECATED          | Scheduled for removal/obsolete      | Add deprecation block and update status            |

*All status changes are managed by automation where possible.*

---

## 4. Automation Checklist

- [ ] Script detects `{{file_header_block}}` and replaces with formatted metadata header, wrapped with `<!-- FILE HEADER:START -->` and `<!-- FILE HEADER:END -->`.
- [ ] Automation updates status, version, updated date, and scope as per policies.
- [ ] Placeholder metadata blocks are added to new/empty docs.
- [ ] Manual edits to the header block are detected and reported/overwritten.
- [ ] Status, author, and scope icons/text follow the project’s config files or standards.
- [ ] Automation reports missing or misformatted headers during CI.

---

## 5. References

* [Documentation Status Policy](./documentation-status-policy.md)
* [Header and Metadata Policy](./header-policy.md)
* [File Header Automation](../../technical/file-header-automation.md)
* [Translation Status Policy](../i18n/translation-status-policy.md)
* [Onboarding Automation](../workflow/onboarding-automation.md)
* [Workflow Automation Architecture](../workflow/workflow-automation.md)
* [Glossary](../contributors/glossary.md)

---

{{last_updated}}
