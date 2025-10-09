"""Converts the number of bytes into a human-readable format.

The module contains the following functions:

- `to_human_size(n_bytes)` - Returns a humanized string: 200 bytes | 1 KB | 1.5 MB etc.
- `get_cache_human_size` - Gets a copy of variable _cach_human_size.
- `clean_cache_human_size` - Resets of variable _cach_human_size.
"""

from __future__ import annotations

__all__ = (
    "to_human_size",
    "get_cache_human_size",
    "clean_cache_human_size",
)

import math

# To caching the results from to_human_size method.
_cache_human_size: dict[int, str] = {}


def get_cache_human_size() -> dict[int, str]:
    """Gets a copy of variable _cach_human_size.

    Hint: To tests.
    """
    return _cache_human_size.copy()


def clean_cache_human_size() -> None:
    """Resets of variable _cach_human_size."""
    global _cache_human_size  # noqa: PLW0603
    _cache_human_size = {}


def to_human_size(n_bytes: int) -> str:
    """Converts the number of bytes into a human-readable format.

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
    result: str | None = _cache_human_size.get(n_bytes)
    if result is not None:
        return result
    idx: int = math.floor(math.log(n_bytes) / math.log(1024))
    ndigits: int = [0, 3, 6, 9, 12][idx]
    human_size: int | float = n_bytes if n_bytes < 1024 else abs(round(n_bytes / pow(1024, idx), ndigits))
    order = ["bytes", "KB", "MB", "GB", "TB"][idx]
    if math.modf(human_size)[0] == 0.0:
        human_size = int(human_size)
    result = f"{human_size} {order}"
    _cache_human_size[n_bytes] = result
    return result
