# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Converts text to a hexadecimal color code.

The module contains the following functions:

- `word_to_color(word)` - Returns a humanized string: 200 bytes | 1 KB | 1.5 MB etc.
"""

from __future__ import annotations

__all__ = ("word_to_color",)


def word_to_color(word: str) -> str:
    """Converts text to a hexadecimal color code.

    Examples:
        >>> from xloft import word_to_color
        >>> word_to_hex("xloft")
        #09cacd
        >>> word_to_color("Hello World!")
        #1db63c

    Args:
        word: The number of bytes.

    Returns:
        Hexadecimal color code: #ffffff | #000000 | #09cacd etc.
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
