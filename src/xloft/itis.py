"""Tools for determining something."""

from __future__ import annotations

__all__ = ("is_number",)

from xloft.constants import REGEX_IS_NUMBER


def is_number(value: str) -> bool:
    """Check if a string is a number.

    Only decimal numbers.

    Args:
        value: Some kind of string.

    Returns:
        True, if the string is a number.
    """
    return REGEX_IS_NUMBER.match(value) is not None
