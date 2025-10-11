"""Collection of tools for converting data.

The module contains the following functions:

- `to_human_size(n_bytes)` - Returns a humanized string: 200 bytes | 1 KB | 1.5 MB etc.
"""

from __future__ import annotations

__all__ = ("to_human_size",)

from xloft.converters.human_size import to_human_size
