"""A collection of instruments for converting data to format is convenient for humans.

The module contains the following functions:

- `to_human_size(size)` - Returns a humanized string: 200 bytes | 1 KB | 1.5 MB etc.
"""

import math


def to_human_size(size: int) -> str:
    """Convert number of bytes to readable format.

    Examples:
        >>> from xloft import to_human_size
        >>> to_human_size(200)
        200 bytes
        >>> to_human_size(1048576)
        1 MB
        >>> to_human_size(1048575)
        1023.999 KB

    Args:
        size: The number of bytes.

    Returns:
        Returns a humanized string: 200 bytes | 1 KB | 1.5 MB etc.
    """
    idx: int = math.floor(math.log(size) / math.log(1024))
    ndigits: int = [0, 3, 6, 9, 12][idx]
    human_size: int | float = size if size < 1024 else abs(round(size / pow(1024, idx), ndigits))
    order = ["bytes", "KB", "MB", "GB", "TB"][idx]
    if math.modf(human_size)[0] == 0.0:
        human_size = int(human_size)
    return f"{human_size} {order}"
