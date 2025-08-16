"""Humanism.

Examples:
    >>> from xloft import to_human_size
    >>> to_human_size(1048576)
    1 MB
"""

import math


def to_human_size(size: int) -> str:
    """Convert number of bytes to readable format.

    Examples:
    >>> from xloft import to_human_size
    >>> to_human_size(1048576)
    1 MB

    Args:
        size: The number of bytes.

    Returns:
        Returns a humanized string: 200 bytes | 1 KB | 1.5 MB etc.
    """
    idx: int = math.floor(math.log(size) / math.log(1024))
    human_size: int | float = size if size < 1024 else abs(round(size / pow(1024, idx), 2))
    order = ["bytes", "KB", "MB", "GB", "TB"][idx]
    return "{:g} {}".format(human_size, order)
