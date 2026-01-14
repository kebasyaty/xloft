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

    def _run_action(
        self,
        alias: str | int | float,
        value: Any | None = None,
        action: str | None = None,
    ) -> tuple[Any, bool]:
        """Action to work with a dictionary.

        Args:
            alias (str | int | float): Alias of key.
            value (Any): Value for key.
            action (str | None): Type of action for working with a dictionary.

        Returns:
            Returns `True` if the key is present.
        """
        is_alias_present: bool = False

        for item in self.store:
            if alias in item[0]:
                is_alias_present = True
                match action:
                    case "get":
                        value = item[1]
                        break
                    case "set":
                        item[1].add(value)
                        break
                    case "delete":
                        self.store = [item for item in self.store if alias not in item[0]]
                        break
                    case "add_alias":
                        break
                    case "delete_alias":
                        break
                    case "has_alias":
                        break
                    case "has_value":
                        break
                    case _ as unreachable:
                        assert_never(Never(unreachable))  # pyrefly: ignore[not-callable]

        return (value, is_alias_present)
