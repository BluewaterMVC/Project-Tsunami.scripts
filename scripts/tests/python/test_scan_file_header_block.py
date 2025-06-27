"""
------------------------------------------------------------------------------
Script Name   : test_scan_file_header_block.py
Description   : Tests insertion and updating of the file header metadata block.
Version       : 1.2.0
Author        : Bluewater Team <dev@bluewaterphp.org>
Maintainer    : Bluewater Team <dev@bluewaterphp.org>
Created       : 2025-06-27
Last Updated  : 2025-06-27
License       : MIT
Repository    : https://github.com/BluewaterMVC/bluewater-scripts
Status        : In Testing
------------------------------------------------------------------------------
"""

import os
import tempfile
from scripts.utils.scan_file_header_block import insert_or_update_header

def example_metadata():
    return {
        "File": "/docs/en/architecture/status/checklists.md",
        "Status_emoji": "🟡",
        "Scope_emoji": "🌐",
        "Version": "1.0",
        "Scope": "Public – All Contributors",
        "Author": "Bluewater Team"
    }

def create_temp_file(content):
    tmp = tempfile.NamedTemporaryFile("w+", delete=False, suffix=".md", encoding="utf-8")
    tmp.write(content)
    tmp.close()
    return tmp.name

def test_insert_placeholder():
    meta = example_metadata()
    orig_content = "{{lang_url_bar}}\n"
    path = create_temp_file(orig_content)
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content, action = insert_or_update_header(content, meta, "In Progress")
        print(f"\n==[ Insert Placeholder ({action}) ]==\n{new_content}")
        assert "{{file_header_block}}" in new_content
        assert action == "placeholder_added"
    finally:
        os.unlink(path)

def test_replace_placeholder_with_header():
    meta = example_metadata()
    content_with_placeholder = "{{lang_url_bar}}\n{{file_header_block}}\n"
    path = create_temp_file(content_with_placeholder)
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content, action = insert_or_update_header(content, meta, "In Progress")
        print(f"\n==[ Replace Placeholder ({action}) ]==\n{new_content}")
        assert "<!-- FILE HEADER:START -->" in new_content
        assert "In Progress" in new_content
        assert action == "block_inserted"
    finally:
        os.unlink(path)

def test_update_existing_header():
    meta = example_metadata()
    # Simulate a file with header already inserted and status "In Progress"
    header = (
        "<!-- FILE HEADER:START -->\n"
        "📄 **File:** /docs/en/architecture/status/checklists.md\n"
        "🟡 **Status:** In Progress\n"
        "🕒 **Updated:** 2025-06-27\n"
        "🔖 **Version:** 1.0\n"
        "🌐 **Scope:** Public – All Contributors\n"
        "👨‍💻 **Author:** Bluewater Team\n"
        "<!-- FILE HEADER:END -->\n"
    )
    content_with_header = f"{{{{lang_url_bar}}}}\n{header}"
    path = create_temp_file(content_with_header)
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content, action = insert_or_update_header(content, meta, "In Review")
        print(f"\n==[ Update Header Block ({action}) ]==\n{new_content}")
        assert "<!-- FILE HEADER:START -->" in new_content
        assert "In Review" in new_content
        assert action == "block_updated"
    finally:
        os.unlink(path)
