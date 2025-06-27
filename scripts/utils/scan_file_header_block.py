"""
------------------------------------------------------------------------------
Script Name   : scan_file_header_block.py
Description   : Detects, inserts, or updates a file header metadata block in Markdown files.
Version       : 1.1.0
Author        : Bluewater Team <dev@bluewaterphp.org>
Maintainer    : Bluewater Team <dev@bluewaterphp.org>
Created       : 2025-06-27
Last Updated  : 2025-06-27
License       : MIT
Repository    : https://github.com/BluewaterMVC/bluewater-scripts
Status        : In Testing
------------------------------------------------------------------------------
"""

import re
import os
import yaml
from datetime import datetime

HEADER_START = "<!-- FILE HEADER:START -->"
HEADER_END = "<!-- FILE HEADER:END -->"
HEADER_BLOCK_RE = re.compile(
    r"<!-- FILE HEADER:START -->(.*?)<!-- FILE HEADER:END -->",
    re.DOTALL,
)

def load_metadata(yml_path):
    with open(yml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def render_header_block(metadata, status):
    now = datetime.now().strftime("%Y-%m-%d")
    metadata["Status"] = status
    metadata["Updated"] = now

    return (
        f"{HEADER_START}\n"
        f"📄 **File:** {metadata.get('File', '')}\n"
        f"{metadata.get('Status_emoji', '')} **Status:** {metadata.get('Status', '')}\n"
        f"🕒 **Updated:** {metadata.get('Updated', '')}\n"
        f"🔖 **Version:** {metadata.get('Version', '')}\n"
        f"{metadata.get('Scope_emoji', '')} **Scope:** {metadata.get('Scope', '')}\n"
        f"👨‍💻 **Author:** {metadata.get('Author', '')}\n"
        f"{HEADER_END}"
    )

def insert_or_update_header(content, metadata, next_status):
    # 1. If no header placeholder and no header block, add placeholder after lang_url_bar and loop.
    if "{{file_header_block}}" not in content and HEADER_START not in content:
        # Add after {{lang_url_bar}}
        content = content.replace("{{lang_url_bar}}\n", "{{lang_url_bar}}\n{{file_header_block}}\n")
        return content, 'placeholder_added'
    # 2. If placeholder is found, replace with new header block and next_status, and loop.
    elif "{{file_header_block}}" in content:
        block = render_header_block(metadata, next_status)
        content = content.replace("{{file_header_block}}", block)
        return content, 'block_inserted'
    # 3. If header block is found, update just the block (change status).
    elif HEADER_START in content and HEADER_END in content:
        def replacer(match):
            return render_header_block(metadata, next_status)
        content = HEADER_BLOCK_RE.sub(replacer, content)
        return content, 'block_updated'
    else:
        raise RuntimeError("Could not insert or update file header block.")
