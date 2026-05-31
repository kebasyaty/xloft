# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Tools for determining something.

The module contains the following functions:

- `is_number` - Check if a string is a number.
"""

from __future__ import annotations

__all__ = ("is_number",)


def is_number(value: str) -> bool:
    """Check if a string is a number.

    Only decimal numbers.

    Examples:
        >>> from xloft import is_number
        >>> is_number("123")
        True

    Args:
        value (str): Some kind of string.

    Returns:
        True, if the string is a number.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False
