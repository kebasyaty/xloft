"""(XLOFT) X-Library of tools.

Modules exported by this package:

- `namedtuple`- Class imitates the behavior of the _named tuple_.
- `human` - A collection of instruments for converting data to format is convenient for humans.
"""

from __future__ import annotations

__all__ = (
    "to_human_size",
    "is_number",
    "NamedTuple",
)

from xloft.human import to_human_size
from xloft.it_is import is_number
from xloft.namedtuple import NamedTuple
