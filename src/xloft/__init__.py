"""(XLOFT) X-Library of tools.

Modules exported by this package:

- `namedtuple`- Class imitates the behavior of the _named tuple_.
- `converter` - A collection of instruments for converting data to format is convenient for humans.
- `itis` - Tools for determining something.
"""

from __future__ import annotations

__all__ = (
    "to_human_size",
    "is_number",
    "NamedTuple",
)

from xloft.converter.human_size import to_human_size
from xloft.itis import is_number
from xloft.namedtuple import NamedTuple
