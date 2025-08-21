"""A collection of instruments for converting data to format is convenient for humans.

The module contains the following functions:

- `to_human_size(size)` - Returns a humanized string: 200 bytes | 1 KB | 1.5 MB etc.
"""

from __future__ import annotations

__all__ = (
    "to_human_size",
    "get_cach_human_size",
)

import math

# To caching the results from to_human_size method.
_cach_human_size: dict[int, str] = {}


def get_cach_human_size() -> dict[int, str]:
    """Get a copy of the variable _cach_human_size.

    Hint: To tests.
    """
    return _cach_human_size.copy()


def to_human_size(n_bytes: int) -> str:
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
        n_bytes: The number of bytes.

    Returns:
        Returns a humanized string: 200 bytes | 1 KB | 1.5 MB etc.
    """
    result: str | None = _cach_human_size.get(n_bytes)
    if result is not None:
        return result
    idx: int = math.floor(math.log(n_bytes) / math.log(1024))
    ndigits: int = [0, 3, 6, 9, 12][idx]
    human_size: int | float = n_bytes if n_bytes < 1024 else abs(round(n_bytes / pow(1024, idx), ndigits))
    order = ["bytes", "KB", "MB", "GB", "TB"][idx]
    if math.modf(human_size)[0] == 0.0:
        human_size = int(human_size)
    result = f"{human_size} {order}"
    _cach_human_size[n_bytes] = result
    return result
