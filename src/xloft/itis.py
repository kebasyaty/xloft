"""Tools for determining something."""

from __future__ import annotations

__all__ = ("is_number",)


def is_number(value: str) -> bool:
    """Check if a string is a number.

    Only decimal numbers.

    Args:
        value: Some kind of string.

    Returns:
        True, if the string is a number.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False
