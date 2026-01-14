# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""`AliasDict` - Pseudo dictionary with supports aliases for keys."""

from __future__ import annotations

__all__ = ("AliasDict",)

import copy
import logging
from typing import Any


class AliasDict:
    """Pseudo dictionary with supports aliases for keys."""

    def __init__(self, data: list[tuple[set[str | int | float], Any]]) -> None:  # noqa: D107
        self.store = []
        self.all_alias_set = set()  # for uniqueness check
        for item in data:
            if len(item[0].difference(self.all_alias_set)) == len(item[0]):
                self.all_alias_set.union(item[0])
                self.store.append(list(item))

    def get(self, alias: str | int | float, default: Any = None) -> Any:
        """Get value by alias.

        If there is no alias, return the default value.

        Args:
            alias (str | int | float): Alias of key.
            default (Any): Value by default.

        Returns:
            Deep copy of the value associated with the key or value by default.
        """
        for item in self.store:
            if alias in item[0]:
                return copy.deepcopy(item[1])

        return default

    def set(self, alias: str | int | float, value: Any) -> None:
        """Add a new (key and value) or update an existing one.

        Args:
            alias (str | int | float): Alias of key.
            value (Any): Value associated with key.

        Returns:
            `None` or `KeyError` is missing.
        """
        for item in self.store:
            if alias in item[0]:
                item[1] = value
                return

        self.store.append([{alias}, value])

    def delete(self, alias: str | int | float) -> None:
        """Delete the value associated with the key and all its aliases.

        Args:
            alias (str | int | float): Alias of key.

        Returns:
            `None` or `KeyError` is missing.
        """
        for item in self.store:
            if alias in item[0]:
                self.all_alias_set = {alias for alias in self.all_alias_set if alias not in item[0]}
                self.store = [item for item in self.store if alias not in item[0]]
                return

        err_msg = f"Alias: `{alias}` is missing!"
        logging.error(err_msg)
        raise KeyError(err_msg)

    def add_alias(
        self,
        alias: str | int | float,
        new_alias: str | int | float,
    ) -> None:
        """Add a new alias to an existing set.

        Args:
            alias (str | int | float): Existing alias.
            new_alias (str | int | float): The alias that needs to be added to the existing set.

        Returns:
            `None` or `KeyError` is missing.
        """
        if new_alias in self.all_alias_set:
            err_msg = f"New Alias: `{new_alias}` is already exists!"
            logging.error(err_msg)
            raise KeyError(err_msg)

        for item in self.store:
            if alias in item[0]:
                item[0].add(new_alias)
                self.all_alias_set.add(new_alias)
                return

        err_msg = f"Alias: `{alias}` is missing!"
        logging.error(err_msg)
        raise KeyError(err_msg)

    def delete_alias(self, alias: str | int | float) -> None:
        """Remove the alias from the existing set.

        If the alias was the last one, then the value associated with it is deleted.

        Args:
            alias (str | int | float): Existing alias.

        Returns:
            `None` or `KeyError` is missing.
        """
        for item in self.store:
            if alias in item[0]:
                if len(item[0]) == 1:
                    self.store = [item for item in self.store if alias not in item[0]]
                else:
                    item[0].remove(alias)
                self.all_alias_set.remove(alias)
                return

        err_msg = f"Alias: `{alias}` is missing!"
        logging.error(err_msg)
        raise KeyError(err_msg)

    def has_alias(self, alias: str | int | float) -> bool:
        """Check for the presence of an alias.

        Args:
            alias (str | int | float): Some alias.

        Returns:
            `True` if the alias is present.
        """
        return alias in self.all_alias_set
