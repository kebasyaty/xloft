# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""`AliasDict` - Pseudo dictionary with supports aliases for keys."""

from __future__ import annotations

__all__ = ("AliasDict",)

from typing import Any


class AliasDict:  # noqa: B903
    """Pseudo dictionary with supports aliases for keys."""

    def __init__(self, data: list[tuple[list[str | int | float], Any]]) -> None:  # noqa: D107
        self.store = data
