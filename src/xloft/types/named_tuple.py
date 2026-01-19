# XLOFT - X-Library of tools.
# Copyright (c) 2025 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""`NamedTuple` - Imitates the behavior of the *named tuple*.

Class `NamedTuple` contains the following methods:

- `get` - Return the value for key if key is in the dictionary, else `None`.
- `update` - Update a value of key.
- `to_dict` - Convert to the dictionary.
- `items` - Returns a generator of list of `NamedTuple` elements grouped into tuples.
- `keys` - Get a generator of list of keys.
- `values` - Get a generator of list of values.
- `has_key` - Returns True if the key exists, otherwise False.
- `has_value` - Returns True if the value exists, otherwise False.
"""

from __future__ import annotations

__all__ = ("NamedTuple",)

from collections.abc import Generator
from typing import Any

from xloft.errors import (
    AttributeCannotBeDeleteError,
    AttributeDoesNotSetValueError,
)


class NamedTuple:
    """This class imitates the behavior of the `named tuple`."""

    def __init__(self, **kwargs: dict[str, Any]) -> None:  # noqa: D107
        self.__dict__["_0D5rSmH9Sy2XUWb5_keys"] = []
        for name, value in kwargs.items():
            self.__dict__[name] = value
            self._0D5rSmH9Sy2XUWb5_keys.append(name)

    def __len__(self) -> int:
        """Get the number of elements in the tuple.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> len(nt)
            2

        Returns:
            The number of elements in the tuple.
        """
        return len(self._0D5rSmH9Sy2XUWb5_keys)

    def __getattr__(self, name: str) -> Any:
        """Getter.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.x
            10

        Args:
            name: Key name.

        Returns:
            Value of key.
        """
        return self.__dict__[name]

    def __setattr__(self, name: str, value: Any) -> None:
        """Blocked Setter."""
        raise AttributeDoesNotSetValueError(name)

    def __delattr__(self, name: str) -> None:
        """Blocked Deleter."""
        raise AttributeCannotBeDeleteError(name)

    def get(self, key: str) -> Any:
        """Return the value for key if key is in the dictionary, else `None`.

        Args:
            key: Key name.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.get("x")
            10

        Returns:
            Value of key.
        """
        value = self.__dict__.get(key)
        if value is not None:
            return value
        return None

    def update(self, key: str, value: Any) -> None:
        """Update a value of key.

        Attention: This is an uncharacteristic action for the type `tuple`.

        Args:
            key: Key name.
            value: Value of key.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.update("x", 20)
            >>> nt.x
            20

        Returns:
            None
        """
        keys: list[str] = self._0D5rSmH9Sy2XUWb5_keys
        if key not in keys:
            err_msg = f"The key `{key}` is missing!"
            raise KeyError(err_msg)
        self.__dict__[key] = value

    def to_dict(self) -> dict[str, Any]:
        """Convert to the dictionary.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> d = nt.to_dict()
            >>> d["x"]
            10

        Returns:
            Dictionary with keys and values of the tuple.
        """
        attrs: dict[str, Any] = self.__dict__
        keys: list[str] = self._0D5rSmH9Sy2XUWb5_keys
        return {key: attrs[key] for key in keys}

    def items(self) -> Generator[tuple[str, Any]]:
        """Returns a generator of list containing a tuple for each key-value pair.

        This is convenient for use in a `for` loop.
        If you need to get a list, do it list(instance.items()).

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> for key, val in nt.items():
            ...     print(f"Key: {key}, Value: {val}")
            "Key: x, Value: 10"
            "Key: y, Value: Hello"

        Returns:
            Returns a list containing a tuple for each key-value pair.
            Type: `list[tuple[str, Any]]`.
        """
        attrs: dict[str, Any] = self.__dict__
        keys: list[str] = self._0D5rSmH9Sy2XUWb5_keys
        return ((key, attrs[key]) for key in keys)

    def keys(self) -> Generator[str]:
        """Get a generator of list of keys.

        If you need to get a list, do it list(instance.items()).

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> list(nt.keys())
            ["x", "y"]

        Returns:
            List of keys.
        """
        keys: list[str] = self._0D5rSmH9Sy2XUWb5_keys
        return (item for item in keys)

    def values(self) -> Generator[Any]:
        """Get a generator of list of values.

        If you need to get a list, do it list(instance.items()).

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> list(nt.values())
            [10, "Hello"]

        Returns:
            List of values.
        """
        attrs: dict[str, Any] = self.__dict__
        keys: list[str] = self._0D5rSmH9Sy2XUWb5_keys
        return (attrs[key] for key in keys)

    def has_key(self, key: str) -> bool:
        """Check if the key exists.

        Args:
            key: Key name.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.has_key("x")
            True

        Returns:
            True if the key exists, otherwise False.
        """
        return key in self._0D5rSmH9Sy2XUWb5_keys

    def has_value(self, value: Any) -> bool:
        """Check if the value exists.

        Args:
            value: Value of key.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.has_value(10)
            True

        Returns:
            True if the value exists, otherwise False.
        """
        return value in self.values()
