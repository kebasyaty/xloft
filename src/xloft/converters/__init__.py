# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Collection of tools for converting data.

The module contains the following functions:

- `to_human_size(n_bytes)` - Returns a humanized string: 200 bytes | 1 KB | 1.5 MB etc.
- `int_to_roman` - Convert an integer to Roman.
- `roman_to_int` - Convert to integer from Roman.
- `word_to_color` - Converts text to a hexadecimal color code.
"""

from __future__ import annotations

__all__ = (
    "to_human_size",
    "int_to_roman",
    "roman_to_int",
    "word_to_color",
)

from xloft.converters.human_size import to_human_size
from xloft.converters.roman import int_to_roman, roman_to_int
from xloft.converters.word_to_color import word_to_color
