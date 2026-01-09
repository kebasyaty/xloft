#             oooo             .o88o.     .
#             `888             888 `"   .o8
# oooo    ooo  888   .ooooo.  o888oo  .o888oo
#  `88b..8P'   888  d88' `88b  888      888
#    Y888'     888  888   888  888      888
#  .o8"'88b    888  888   888  888      888 .
# o88'   888o o888o `Y8bod8P' o888o     "888"
#
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
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
