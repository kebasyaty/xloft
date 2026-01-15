#        ___              ___  __
#       /\_ \           /'___\/\ \__
#  __  _\//\ \     ___ /\ \__/\ \ ,_\
# /\ \/'\ \ \ \   / __`\ \ ,__\\ \ \/
# \/>  </  \_\ \_/\ \L\ \ \ \_/ \ \ \_
#  /\_/\_\ /\____\ \____/\ \_\   \ \__\
#  \//\/_/ \/____/\/___/  \/_/    \/__/
#
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""(XLOFT) X-Library of tools.

Modules exported by this package:

- `types`- Custom data types.
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
    "AliasDict",
    "NamedTuple",
)

from xloft.converters import int_to_roman, roman_to_int, to_human_size
from xloft.itis import is_number, is_palindrome
from xloft.types.alias_dict import AliasDict
from xloft.types.named_tuple import NamedTuple
