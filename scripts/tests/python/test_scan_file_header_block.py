"""
------------------------------------------------------------------------------
Script Name   : test_scan_file_header_block.py
Description   : Tests scan_file_header_block.py header insertion utility.
                - Test 1: Missing placeholder raises error.
                - Test 2: Placeholder is replaced with rendered metadata, showing BEFORE and AFTER content.
Version       : 1.0.0
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
import yaml
import pytest
from scripts.utils.scan_file_header_block import insert_file_header_block

def load_example_metadata():
    """
    Loads example metadata from the standard config location.
    Edit path if you use a different config dir or metadata filename.
    """
    config_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config'))
    metadata_path = os.path.join(config_dir, 'example_header_metadata.yml')
    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = yaml.safe_load(f)
    return metadata

def test_insert_file_header_block_raises_if_missing():
    print("\nTEST 1: Missing {{file_header_block}} should raise ValueError.")
    metadata = load_example_metadata()
    content = '''{{lang_url_bar}}

Some doc body here.
'''
    try:
        insert_file_header_block(content, metadata)
        print("FAIL: No ValueError was raised when placeholder was missing!")
        assert False, "ValueError was NOT raised when placeholder was missing."
    except ValueError as e:
        print(f"PASS: Caught expected ValueError: {e}")

def test_insert_file_header_block_with_external_configs():
    print("\nTEST 2: Placeholder is present and should be replaced with header metadata.")
    metadata = load_example_metadata()
    content = '''{{lang_url_bar}}
{{file_header_block}}

Some doc body here.
'''

    # Show content BEFORE header insertion
    print("\n==[ Temp file contents BEFORE update: ]==")
    print(content)

    # Insert header and write to temp file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.md', encoding='utf-8') as tmpfile:
        temp_path = tmpfile.name
        new_content = insert_file_header_block(content, metadata)
        tmpfile.write(new_content)

    # Show content AFTER header insertion
    print(f"\n==[ Temp file created at: {temp_path} ]==")
    with open(temp_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        print("\n==[ Temp file contents AFTER update: ]==")
        print(file_content)

    os.remove(temp_path)

    # Assert
    if "{{file_header_block}}" not in file_content:
        print("PASS: Placeholder was replaced with header metadata.")
    else:
        print("FAIL: Placeholder was NOT replaced.")
    assert "{{file_header_block}}" not in file_content, "Placeholder should be replaced"
    assert "File:" in file_content and "Status:" in file_content, "Header fields missing"
