"""Tools for determining something.

The module contains the following functions:

- `is_number` - Check if a string is a number.
- `is_palindrome` - Check if a string is a palindrome.
"""

from __future__ import annotations

__all__ = (
    "is_number",
    "is_palindrome",
)


def is_number(value: str) -> bool:
    """Check if a string is a number.

    Only decimal numbers.

    Examples:
        >>> from xloft import is_number
        >>> is_number("123")
        True

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


def is_palindrome(value: str) -> bool:
    """Check if a string is a palindrome.

    Examples:
        >>> from xloft import is_palindrome
        >>> is_palindrome("123aa321")
        True

    Args:
        value: Alpha-numeric string.

    Returns:
        Boolean value.
        ValueError - If the string is not alpha-numeric.
    """
    string_list = []
    for char in value:
        if not char.isalnum():
            raise ValueError("The value is not an alpha-numeric string!")
        string_list.append(char.lower())
    reverse_list = string_list[::-1]
    return reverse_list == string_list
