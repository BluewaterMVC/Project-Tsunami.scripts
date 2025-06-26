<!-- Language Navigation Bar (automated on commit) -->

{{lang_url_bar}}

---

<!-- File Header Metadata Block (automated on commit) -->

{{file_header_block}}

---

# 🐍 Python Testing Guide (pytest)

This document describes the **standard for testing Python automation scripts** in the Bluewater Scripts repository.
It covers setup, usage, and best practices for using [`pytest`](https://docs.pytest.org/)—our tool of choice for Python testing.

---

## 1. Why pytest?

* **Readability:**
  Clean test discovery and assertion syntax.
* **Rich Features:**
  Fixtures, parametrization, powerful reporting, and plugin ecosystem.
* **CI-Friendly:**
  Easy to integrate with GitHub Actions and other CI pipelines.
* **Community Support:**
  Standard in modern Python projects.

---

## 2. Directory Structure

* All Python tests are stored in `/tests/python/`.
* Test files must be named `test_*.py` and correspond to their target scripts.
* Example:

  ```
  /scripts/utils/scan_file_header_block.py
  /tests/python/test_scan_file_header_block.py
  ```

---

## 3. Getting Started

### a. **Install pytest**

```bash
pip install pytest
```

If using a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements-dev.txt
```

### b. **Running Tests**

From the repo root or `/tests/python/` directory:

```bash
pytest
```

Or to run a specific test:

```bash
pytest tests/python/test_scan_file_header_block.py
```

---

## 4. Writing Tests

* All test functions should begin with `test_`.
* Use plain `assert` for checks.
* Use pytest’s `tmp_path` or fixtures for file-based testing.

**Example Test:**

```python
from scripts.utils.scan_file_header_block import scan_for_file_header_block

def test_finds_header_block(tmp_path):
    test_file = tmp_path / "test.md"
    test_file.write_text("Intro text\n\n{{file_header_block}}\nContent")
    assert scan_for_file_header_block(str(test_file)) is True
```

---

## 5. Output & Reporting

* Test output shows PASS/FAIL for each function.
* Use `pytest --tb=short` for concise tracebacks.
* Use plugins like `pytest-cov` for coverage reports if needed.

---

## 6. Best Practices

* Each script function should have at least one corresponding test.
* Cover both expected and failure/error cases.
* Use fixtures to set up test data or environments.
* Keep test files and script files in sync.
* Document new or updated tests in PRs.

---

## 7. CI/CD Integration

* All tests are run in GitHub Actions on push and PR.
* Tests **must pass** before merge.

---

## 8. References

* [pytest Documentation](https://docs.pytest.org/)
* [Python Scripts Policy](../python-scripts.md)
* [Technical Testing Overview](./overview.md)
* [System Overview](../../architecture/system-overview.md)

---

{{last_updated}}
