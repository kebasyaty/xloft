#
#
# `YMM'   `MP' `7MMF'        .g8""8q. `7MM"""YMM MMP""MM""YMM
#   VMb.  ,P     MM        .dP'    `YM. MM    `7 P'   MM   `7
#    `MM.M'      MM        dM'      `MM MM   d        MM
#      MMb       MM        MM        MM MM""MM        MM
#    ,M'`Mb.     MM      , MM.      ,MP MM   Y        MM
#   ,P   `MM.    MM     ,M `Mb.    ,dP' MM            MM
# .MM:.  .:MMa..JMMmmmmMMM   `"bmmd"' .JMML.        .JMML.
#
#

"""(XLOFT) X-Library of tools.

Modules exported by this package:

- `namedtuple`- Class imitates the behavior of the _named tuple_.
- `converters` - Collection of tools for converting data.
- `itis` - Tools for determining something.
"""

from __future__ import annotations

__all__ = (
    "int_to_roman",
    "roman_to_int",
    "to_human_size",
    "is_number",
    "is_palindrome",
    "NamedTuple",
)


from xloft.converters import int_to_roman, roman_to_int, to_human_size
from xloft.itis import is_number, is_palindrome
from xloft.namedtuple import NamedTuple
