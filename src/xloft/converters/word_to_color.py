# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Convert text to a hexadecimal color code.

The module contains the following functions:

- `word_to_color(word)` - Returns a hexadecimal color code: #ffffff | #09cacd | #1db63c etc.
"""

from __future__ import annotations

__all__ = ("word_to_color",)


def word_to_color(word: str) -> str:
    """Convert text to a hexadecimal color code.

    Examples:
        >>> from xloft import word_to_color
        >>> word_to_color("xloft")
        #09cacd
        >>> word_to_color("Hello World!")
        #1db63c

    Args:
        word: The number of bytes.

    Returns:
        Hexadecimal color code: #ffffff | #09cacd | #1db63c etc.
    """
    hash_val = 0
    # Calculate hash for word
    for char in word:
        hash_val = ord(char) + ((hash_val << 5) - hash_val)

    # Convert hash to HEX code
    color_hex = "#"
    for i in range(3):
        # Extract byte and convert to hexadecimal format
        color_hex += f"{(hash_val >> (i * 8)) & 0xFF:02x}"

    return color_hex
