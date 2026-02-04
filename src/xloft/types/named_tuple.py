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

import copy
from typing import Any

from xloft.errors import (
    AttributeCannotBeDeleteError,
    AttributeDoesNotSetValueError,
)


class NamedTuple:
    """This class imitates the behavior of the `named tuple`."""

    def __init__(self, **kwargs: dict[str, Any]) -> None:  # noqa: D107
        self.__dict__["_store"] = copy.deepcopy(kwargs)

    def __repr__(self) -> str:
        """Called by the repr built-in function.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> repr(nt)
            'NamedTuple(x=10, y="Hello")'

        Returns:
            Returns raw data used for internal representation in python.
        """
        args = []
        for key, val in self.__dict__["_store"].items():
            if isinstance(val, str):
                args.append(f'{key}="{val}"')  # pyrefly: ignore[bad-argument-type]
            else:
                args.append(f"{key}={val}")  # pyrefly: ignore[bad-argument-type]

        return f"NamedTuple({', '.join(args)})"

    def __str__(self) -> str:
        """Get a string representation of NamedTuple.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> str(nt)
            ''

        Returns:
            String representation of NamedTuple.
        """
        return str(self.__dict__["_store"])

    def __bool__(self) -> bool:
        """Called when checking for truth.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> bool(nt)
            True

        Returns:
            Boolean value.
        """
        return len(self.__dict__["_store"]) > 0

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
        return len(self._store)

    def __getattr__(self, name: str) -> Any:
        """Getter.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.x
            10

        Args:
            name (str): Key name.

        Returns:
            Value of key.
        """
        value = self._store[name]
        return copy.deepcopy(value)

    def __setattr__(self, name: str, value: Any) -> None:
        """Blocked Setter."""
        raise AttributeDoesNotSetValueError(name)

    def __delattr__(self, name: str) -> None:
        """Blocked Deleter."""
        raise AttributeCannotBeDeleteError(name)

    def __getitem__(self, key: str) -> Any:
        """Get value by [key_name].

        Args:
            key (str): Key name.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt["x"]
            10

        Returns:
            Return the value for key, else KeyError.
        """
        value = self._store[key]
        return copy.deepcopy(value)

    def get(self, key: str, default: Any = None) -> Any:
        """Return the value for key if key is in the NamedTuple, else default.

        Args:
            key (str): Key name.
            default (Any): Returns if the value is missing.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.get("x")
            10

        Returns:
            Return the value for key if key is in the NamedTuple, else default.
        """
        try:
            value = self._store[key]
            return copy.deepcopy(value)
        except KeyError:
            return default

    def update(self, key: str, value: Any) -> None:
        """Update a value of key.

        Attention: This is an uncharacteristic action for the type `tuple`.

        Args:
            key (str): Key name.
            value (Any): Value of key.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.update("x", 20)
            >>> nt.x
            20

        Returns:
            `None` or `KeyError` is missing.
        """
        keys: list[str] = self._store.keys()
        if key not in keys:
            err_msg = f"The key `{key}` is missing!"
            raise KeyError(err_msg)
        self._store[key] = value

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
        return dict(self._store)

    def items(self) -> Any:
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
        return self._store.items()

    def keys(self) -> Any:
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
        return self._store.keys()

    def values(self) -> Any:
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
        return self._store.values()

    def has_key(self, key: str) -> bool:
        """Check if the key exists.

        Args:
            key (str): Key name.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.has_key("x")
            True

        Returns:
            True if the key exists, otherwise False.
        """
        keys = self._store.keys()
        return key in keys

    def has_value(self, value: Any) -> bool:
        """Check if the value exists.

        Args:
            value (Any): Value of key.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.has_value(10)
            True

        Returns:
            True if the value exists, otherwise False.
        """
        values = self._store.values()
        return value in values
