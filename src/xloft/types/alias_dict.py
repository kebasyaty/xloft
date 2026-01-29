# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""`AliasDict` - Pseudo dictionary with supports aliases for keys.

Class `AliasDict` contains the following methods:

- `get` - Get value by alias.
- `add` - Add a new key and value pair.
- `update` - Update the value of an existing key.
- `delete` - Delete the value associated with the key and all its aliases.
- `add_alias` - Add a new alias to an existing set.
- `delete_alias` - Remove the alias from the existing set.
- `has_key` - Check if the alias exists.
- `has_value` - Check if the value exists.
- `items` - Returns a generator of list of `AliasDict` elements grouped into tuples.
- `keys` - Get a generator of list of all aliases.
- `values` - Get a generator of list of all values.
"""

from __future__ import annotations

__all__ = ("AliasDict",)

import copy
from collections.abc import Generator
from typing import Any

from xloft.errors import (
    AttributeCannotBeDeleteError,
    AttributeDoesNotGetValueError,
    AttributeDoesNotSetValueError,
)


class AliasDict:
    """Pseudo dictionary with supports aliases for keys."""

    def __init__(self, data: list[tuple[set[str | int | float], Any]] | None = None) -> None:  # noqa: D107
        self.__dict__["_store"] = []
        self.__dict__["all_alias_set"] = set()  # for uniqueness check
        if data is not None:
            for item in data:
                if not self.all_alias_set.isdisjoint(item[0]):
                    err_msg = "In some keys, aliases are repeated!"
                    raise KeyError(err_msg)
                self.all_alias_set.update(item[0])
                self._store.append(list(item))

    def __len__(self) -> int:
        """Get the number of elements in the dictionary.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> len(ad)
            1

        Returns:
            The number of elements in the dictionary.
        """
        return len(self.__dict__["_store"])

    def __getattr__(self, name: str) -> None:
        """Blocked Getter."""
        raise AttributeDoesNotGetValueError(name)

    def __setattr__(self, name: str, value: Any) -> None:
        """Blocked Setter."""
        raise AttributeDoesNotSetValueError(name)

    def __delattr__(self, name: str) -> None:
        """Blocked Deleter."""
        raise AttributeCannotBeDeleteError(name)

    def __getitem__(self, alias: str | int | float) -> Any:
        """Get value by [key_name].

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> ad["en"]
            "lemmatize_en_all"

        Args:
            alias (str | int | float): Alias of key.

        Returns:
            Return the value for alias, else KeyError.
        """
        for item in self.__dict__["_store"]:
            if alias in item[0]:
                return copy.deepcopy(item[1])
        raise KeyError(f"Alias `{alias}` is missing!")

    def get(self, alias: str | int | float, default: Any = None) -> Any:
        """Return the value for alias if alias is in the dictionary, else default.

        If there is no alias, return the default value.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> ad.get("en")
            "lemmatize_en_all"

        Args:
            alias (str | int | float): Alias of key.
            default (Any): Value by default.

        Returns:
            Return the value for alias if alias is in the dictionary, else default.
        """
        for item in self.__dict__["_store"]:
            if alias in item[0]:
                return copy.deepcopy(item[1])

        return default

    def add(self, aliases: set[str | int | float], value: Any) -> None:
        """Add a new key and value pair.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> ad.add({"Russian", "ru"}, "lemmatize_ru_all")
            >>> ad.get("ru")
            "lemmatize_ru_all"

        Args:
            aliases (set[str | int | float]): List (set) aliases of key.
            value (Any): Value associated with key.

        Returns:
            `None` or `KeyError` if alias is missing.
        """
        if not self.all_alias_set.isdisjoint(aliases):
            err_msg = "Some aliases already exist."
            raise KeyError(err_msg)

        self._store.append([aliases, value])
        self.all_alias_set.update(aliases)

    def update(self, alias: str | int | float, value: Any) -> None:
        """Update the value of an existing key.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> ad.update("en", "Hello world!")
            >>> ad.get("English")
            "Hello world!"

        Args:
            alias (str | int | float): Alias of key.
            value (Any): Value associated with key.

        Returns:
            `None` or `KeyError` if alias is missing.
        """
        for item in self.__dict__["_store"]:
            if alias in item[0]:
                item[1] = value
                return

        err_msg = f"Alias `{alias}` is missing!"
        raise KeyError(err_msg)

    def delete(self, alias: str | int | float) -> None:
        """Delete the value associated with the key and all its aliases.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> ad.delete("en")
            >>> ad.get("English")
            None

        Args:
            alias (str | int | float): Alias of key.

        Returns:
            `None` or `KeyError` if alias is missing.
        """
        for item in self.__dict__["_store"]:
            if alias in item[0]:
                self.__dict__["all_alias_set"] = {
                    alias for alias in self.__dict__["all_alias_set"] if alias not in item[0]
                }
                self.__dict__["_store"] = [item for item in self.__dict__["_store"] if alias not in item[0]]
                return

        err_msg = f"Alias `{alias}` is missing!"
        raise KeyError(err_msg)

    def add_alias(
        self,
        alias: str | int | float,
        new_alias: str | int | float,
    ) -> None:
        """Add a new alias to an existing set.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English"}, "lemmatize_en_all")])
            >>> ad.add_alias("English", "en")
            >>> ad.get("en")
            "lemmatize_en_all"

        Args:
            alias (str | int | float): Existing alias.
            new_alias (str | int | float): The alias that needs to be added to the existing set.

        Returns:
            `None` or `KeyError` if new alias is already exists.
        """
        if new_alias in self.__dict__["all_alias_set"]:
            err_msg = f"New Alias `{new_alias}` is already exists!"
            raise KeyError(err_msg)

        for item in self.__dict__["_store"]:
            if alias in item[0]:
                item[0].add(new_alias)
                self.all_alias_set.add(new_alias)
                return

        err_msg = f"Alias `{alias}` is missing!"
        raise KeyError(err_msg)

    def delete_alias(self, alias: str | int | float) -> None:
        """Remove the alias from the existing set.

        If the alias was the last one, then the value associated with it is deleted.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> ad.delete_alias("en")
            >>> ad.keys()
            ["English"]

        Args:
            alias (str | int | float): Existing alias.

        Returns:
            `None` or `KeyError` if alias is missing.
        """
        for item in self.__dict__["_store"]:
            if alias in item[0]:
                if len(item[0]) == 1:
                    self._store = [item for item in self._store if alias not in item[0]]
                else:
                    item[0].remove(alias)
                self.all_alias_set.remove(alias)
                return

        err_msg = f"Alias `{alias}` is missing!"
        raise KeyError(err_msg)

    def has_key(self, alias: str | int | float) -> bool:
        """Check if the alias exists.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> ad.has_key("en")
            True

        Args:
            alias (str | int | float): Some alias.

        Returns:
            True if the key exists, otherwise False.
        """
        return alias in self.__dict__["all_alias_set"]

    def has_value(self, value: Any) -> bool:
        """Check if the value exists.

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> ad.has_value("lemmatize_en_all")
            True

        Args:
            value (Any): Value associated with key.

        Returns:
            True if the value exists, otherwise False.
        """
        is_exists = False
        for item in self.__dict__["_store"]:
            if value == item[1]:
                is_exists = True
                break

        return is_exists

    def items(self) -> Generator[tuple[list[str | int | float], Any]]:
        """Returns a generator of list containing a tuple for each key-value pair.

        This is convenient for use in a `for` loop.
        If you need to get a list, do it list(instance.items()).

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> for aliases, value in ad.items():
            ...     print(f"Aliases: {aliases}, Value: {value}")
            "Key: ['English', 'en'], Value: lemmatize_en_all"

        Returns:
            Returns a list containing a tuple for each key-value pair.
            Type: `list[tuple[list[str | int | float], Any]]` or `[]`.
        """
        store = self.__dict__["_store"]
        return ((list(item[0]), item[1]) for item in store)

    def keys(self) -> Generator[str | int | float]:
        """Get a generator of list of all aliases.

        If you need to get a list, do it list(instance.keys()).

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> list(ad.keys())
            ["English", "en"]

        Returns:
            List of all aliases.
        """
        all_alias_set = self.__dict__["all_alias_set"]
        return (item for item in all_alias_set)

    def values(self) -> Generator[Any]:
        """Get a generator of list of all values.

        If you need to get a list, do it list(instance.values()).

        Examples:
            >>> from xloft import AliasDict
            >>> ad = AliasDict([({"English", "en"}, "lemmatize_en_all")])
            >>> list(ad.values())
            ["lemmatize_en_all"]

        Returns:
            List of all values.
        """
        store = self.__dict__["_store"]
        return (item[1] for item in store)
