"""(XLOFT) X-Library of tools.

Modules exported by this package:

- `namedtuple`: Class imitates the behavior of the _named tuple_.
- `humanism` - A collection of instruments for converting data to format is convenient for humans.
"""

__all__ = (
    "to_human_size",
    "NamedTuple",
)

from xloft.humanism import to_human_size
from xloft.namedtuple import NamedTuple
