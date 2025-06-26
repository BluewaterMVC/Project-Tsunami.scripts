"""
------------------------------------------------------------------------------
Script Name   : scan_file_header_block.py
Description   : Replaces the {{file_header_block}} placeholder in a Markdown file
                with a rendered metadata block using external config files and a template.
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
import yaml

# --- Configuration ---
CONFIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))
STATUS_CONFIG = "status_options.yml"
SCOPE_CONFIG = "scope_options.yml"
TEMPLATE_FILE = "header_template.txt"

def load_yaml_dict(filename):
    """Load YAML from file and return as dict."""
    path = os.path.join(CONFIG_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def load_template(filename):
    """Load template text file."""
    path = os.path.join(CONFIG_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def render_file_header_block(metadata):
    """Render the file header block using template and icon configs."""
    status_icons = load_yaml_dict(STATUS_CONFIG)
    scope_icons = load_yaml_dict(SCOPE_CONFIG)
    template = load_template(TEMPLATE_FILE)

    # Add emoji fields for template substitution
    status = metadata.get("Status", "")
    scope = metadata.get("Scope", "")
    metadata = dict(metadata)  # Copy to avoid mutating caller's dict
    metadata["Status_emoji"] = status_icons.get(status, "")
    metadata["Scope_emoji"] = scope_icons.get(scope, "")

    # Replace all {{Field}} in template with metadata values
    rendered = template
    for key, value in metadata.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", str(value))
    return rendered

def insert_file_header_block(content, metadata):
    """
    Replaces the {{file_header_block}} placeholder in content with the rendered file header block.
    Raises ValueError if the placeholder is not found.
    """
    placeholder = "{{file_header_block}}"
    if placeholder not in content:
        raise ValueError("File header block placeholder not found in content.")
    header_block = render_file_header_block(metadata)
    return content.replace(placeholder, header_block, 1)

# --- Optional: CLI usage for manual testing ---
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Insert Bluewater file header block into a Markdown file.")
    parser.add_argument("markdown_file", help="Markdown file to update (in-place).")
    parser.add_argument("metadata_file", help="YAML metadata file for header.")
    args = parser.parse_args()

    # Load inputs
    with open(args.markdown_file, "r", encoding="utf-8") as f:
        content = f.read()
    metadata = load_yaml_dict(args.metadata_file)

    # Update content
    new_content = insert_file_header_block(content, metadata)
    with open(args.markdown_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Header block inserted/updated in {args.markdown_file}")
