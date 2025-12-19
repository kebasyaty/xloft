#  ____  ____  _____       ___   ________  _________
# |_  _||_  _||_   _|    .'   `.|_   __  ||  _   _  |
#   \ \  / /    | |     /  .-.  \ | |_ \_||_/ | | \_|
#    > `' <     | |   _ | |   | | |  _|       | |
#  _/ /'`\ \_  _| |__/ |\  `-'  /_| |_       _| |_
# |____||____||________| `.___.'|_____|     |_____|
#
#
# Copyright (c) 2025 Gennady Kostyunin
# XLOFT is free software under terms of the MIT License.
# Repository https://github.com/kebasyaty/xloft
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
