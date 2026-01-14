# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""`AliasDict` - Pseudo dictionary with supports aliases for keys."""

from __future__ import annotations

__all__ = ("AliasDict",)

from typing import Any, Never, assert_never


class AliasDict:
    """Pseudo dictionary with supports aliases for keys."""

    def __init__(self, data: list[tuple[set[str | int | float], Any]]) -> None:  # noqa: D107
        self.store = []
        for item in data:
            self.store.append(list(item))

    def run_action(
        self,
        alias: str | int | float,
        value: Any | None = None,
        action: str | None = None,
    ) -> bool:
        """Perform an action on a dictionary."""
        is_alias_present: bool = False

        for item in self.store:
            if alias in item[0]:
                is_alias_present = True
                match action:
                    case "get":
                        pass
                    case "set":
                        item[1] = value
                    case "delete":
                        pass
                    case "add_alias":
                        pass
                    case "delete_alias":
                        pass
                    case "has_alias":
                        pass
                    case "has_value":
                        pass
                    case _ as unreachable:
                        assert_never(Never(unreachable))  # pyrefly: ignore[not-callable]

        return is_alias_present
