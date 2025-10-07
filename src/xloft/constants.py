"""Constant variables.

The module contains the following variables:

- `DB_ROOT` - Path to root directory of database. `By default = "ScrubyDB"` (*in root of project*).
"""

from __future__ import annotations

__all__ = ("REGEX_IS_NUMBER",)

import re

REGEX_IS_NUMBER = re.compile(r"^[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$")
