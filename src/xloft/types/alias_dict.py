# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""`AliasDict` - Simulates the behavior of a dictionary and supports aliases for keys."""

from __future__ import annotations

__all__ = ("AliasDict",)

from typing import Any


class AliasDict:
    """Dictionary with supports aliases for keys."""

    def __init__(self, **kwargs: dict[list[str | int | float], Any]) -> None:  # noqa: D107
        self.store: list[tuple[list[str | int | float], Any]] = []
