"""(XLOFT) X-Library of tools.

Modules exported by this package:

- `NamedTuple`: Class imitates the behavior of the _named tuple_.
"""

__all__ = (
    "to_human_size",
    "NamedTuple",
)

from xloft.humanism import to_human_size
from xloft.namedtuple import NamedTuple
