<!-- Language Navigation Bar (automated on commit) -->

{{lang_url_bar}}

---

<!-- File Header Metadata Block (automated on commit) -->

{{file_header_block}}

---

# 🐍 Python Script Metadata Policy

This document defines the **mandatory metadata header format** for all Python scripts in the Bluewater Scripts repository. Adhering to this policy ensures every automation script is clearly versioned, attributed, and traceable—critical for maintenance, security, and collaborative work.

---

## 1. Purpose

To enforce a **consistent, machine- and human-readable header block** at the top of every automation script, supporting documentation automation, audit, and code review processes.

---

## 2. Required Metadata Fields

Every Python automation script must begin with a docstring containing the following fields:

* **Script Name**
* **Description**
* **Version**
* **Author**
* **Maintainer** (if different)
* **Created**
* **Last Updated**
* **License**
* **Repository**
* **Status** (`Draft`, `In Progress`, `Published`, `Deprecated`, etc.)

---

## 3. Standard Metadata Header Template

> **Copy and paste this template at the top of all new Python scripts.**

```python
"""
------------------------------------------------------------------------------
Script Name   : scan_file_header_block.py
Description   : Scans a Markdown file for the {{file_header_block}} placeholder and returns its position.
Version       : 1.0.0
Author        : Bluewater Team <dev@bluewaterphp.org>
Maintainer    : Bluewater Team <dev@bluewaterphp.org>
Created       : 2025-06-27
Last Updated  : 2025-06-27
License       : MIT
Repository    : https://github.com/BluewaterMVC/bluewater-scripts
Status        : Published
------------------------------------------------------------------------------
"""
```

---

## 4. Placement and Formatting

* Place the header **as the very first block** in the script, above all imports.
* Use triple double-quoted strings (`""" ... """`).
* Do not modify the template order or field names; automation relies on this format.
* Always keep `Last Updated` current when editing the script.
* Update `Status` as the script moves through its lifecycle.

---

## 5. Additional Guidance

* For **multi-file scripts**, each script should have its own metadata header.
* If a script is deprecated, set `Status: Deprecated` and add a `Deprecation Notice` comment below the header.

---

## 6. Sample Script (First 10 Lines)

```python
"""
------------------------------------------------------------------------------
Script Name   : scan_file_header_block.py
Description   : Scans a Markdown file for the {{file_header_block}} placeholder and returns its position.
Version       : 1.0.0
Author        : Bluewater Team <dev@bluewaterphp.org>
Maintainer    : Bluewater Team <dev@bluewaterphp.org>
Created       : 2025-06-27
Last Updated  : 2025-06-27
License       : MIT
Repository    : https://github.com/BluewaterMVC/bluewater-scripts
Status        : Published
------------------------------------------------------------------------------
"""

import sys
# ... rest of your script
```

---

## 7. Compliance

All contributions must pass a **metadata header check** during pre-commit and CI.
Pull requests missing the standardized header will be rejected or auto-corrected by automation.

---

## 8. References & Cross-Links

* [General Coding Standards](../coding-standards.md)
* [Header and Metadata Policy (Markdown Docs)](../../architecture/status/header-policy.md)
* [CONTRIBUTING.md](/CONTRIBUTING.md)

---

{{last_updated}}
