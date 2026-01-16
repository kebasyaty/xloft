# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Custom data types.

This module exports the following data types:

- `AliasDict` - Pseudo dictionary with supports aliases for keys.
- `NamedTuple` - Imitates the behavior of the *named tuple*.
"""

from __future__ import annotations

__all__ = (
    "AliasDict",
    "NamedTuple",
)

from xloft.types.alias_dict import AliasDict
from xloft.types.named_tuple import NamedTuple
