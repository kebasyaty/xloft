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
        value (str): Some kind of string.

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
        >>> is_palindrome("Go hang a salami, I'm a lasagna hog")
        True

    Args:
        value (str): Alpha-numeric string.

    Returns:
        Boolean value.
    """
    if not isinstance(value, str):
        raise TypeError("The value is not a string!")
    if not len(value):
        raise ValueError("The string must not be empty!")
    string_list = [char.lower() for char in value if char.isalnum()]
    reverse_list = string_list[::-1]
    return reverse_list == string_list
