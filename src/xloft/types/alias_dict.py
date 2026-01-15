# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""`AliasDict` - Pseudo dictionary with supports aliases for keys."""

from __future__ import annotations

__all__ = ("AliasDict",)

import copy
import logging
from typing import Any

from xloft.errors import (
    AttributeCannotBeDeleteError,
    AttributeDoesNotGetValueError,
    AttributeDoesNotSetValueError,
)


class AliasDict:
    """Pseudo dictionary with supports aliases for keys."""

    def __init__(self, data: list[tuple[set[str | int | float], Any]] | None = None) -> None:  # noqa: D107
        self.__dict__["store"] = []
        self.__dict__["all_alias_set"] = set()  # for uniqueness check
        if data is not None:
            for item in data:
                if not self.all_alias_set.isdisjoint(item[0]):
                    err_msg = "In some keys, aliases are repeated."
                    logging.error(err_msg)
                    raise KeyError(err_msg)
                self.all_alias_set.update(item[0])
                self.store.append(list(item))

    def __getattr__(self, name: str) -> None:
        """Blocked Getter."""
        raise AttributeDoesNotGetValueError(name)

    def __setattr__(self, name: str, value: Any) -> None:
        """Blocked Setter."""
        raise AttributeDoesNotSetValueError(name)

    def __delattr__(self, name: str) -> None:
        """Blocked Deleter."""
        raise AttributeCannotBeDeleteError(name)

    def get(self, alias: str | int | float, default: Any = None) -> Any:
        """Get value by alias.

        If there is no alias, return the default value.

        Args:
            alias (str | int | float): Alias of key.
            default (Any): Value by default.

        Returns:
            Deep copy of the value associated with the key or value by default.
        """
        for item in self.__dict__["store"]:
            if alias in item[0]:
                return copy.deepcopy(item[1])

        return default

    def add(self, aliases: set[str | int | float], value: Any) -> None:
        """Add a new key and value pair.

        Args:
            aliases (set[str | int | float]): List (set) aliases of key.
            value (Any): Value associated with key.

        Returns:
            `None` or `KeyError` is missing.
        """
        if not self.all_alias_set.isdisjoint(aliases):
            err_msg = "In some keys, aliases are repeated."
            logging.error(err_msg)

        self.store.append([aliases, value])
        self.all_alias_set.update(aliases)

    def update(self, alias: set[str | int | float], value: Any) -> None:
        """Update the value of an existing key.

        Args:
            aliases (set[str | int | float]): Alias of key.
            value (Any): Value associated with key.

        Returns:
            `None` or `KeyError` if alias is missing.
        """
        for item in self.__dict__["store"]:
            if alias in item[0]:
                item[1] = value
                return

    def delete(self, alias: str | int | float) -> None:
        """Delete the value associated with the key and all its aliases.

        Args:
            alias (str | int | float): Alias of key.

        Returns:
            `None` or `KeyError` if alias is missing.
        """
        for item in self.__dict__["store"]:
            if alias in item[0]:
                self.__dict__["all_alias_set"] = {
                    alias for alias in self.__dict__["all_alias_set"] if alias not in item[0]
                }
                self.__dict__["store"] = [item for item in self.__dict__["store"] if alias not in item[0]]
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
            `None` or `KeyError` if new alias is already exists.
        """
        if new_alias in self.__dict__["all_alias_set"]:
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
            `None` or `KeyError` if alias is missing.
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
        """Check if the alias exists.

        Args:
            alias (str | int | float): Some alias.

        Returns:
            `True` if the alias is exists.
        """
        return alias in self.__dict__["all_alias_set"]

    def has_value(self, value: Any) -> bool:
        """Check if the value exists.

        Args:
            value (Any): Value associated with key.

        Returns:
            `True` if the value is exists.
        """
        is_present = False
        for item in self.store:
            if value == item[1]:
                is_present = True
                break

        return is_present

    def items(self) -> list[tuple[set[str | int | float], Any]]:
        """Returns a list of `AliasDict` elements grouped into tuples.

        This is convenient for use in a `for` loop.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> for aliases, value in ad.items():
            ...     print(f"Aliases: {aliases}, Value: {value}")
            "Key: x, Value: lemmatize_en_all"

        Returns:
            `list[tuple[set[str | int | float], Any]]` or `[]`
        """
        return [(item[0], item[1]) for item in self.store]
