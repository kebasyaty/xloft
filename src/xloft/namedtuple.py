"""This module contains the implementation of the `NamedTuple` class.

`NamedTuple` class imitates the behavior of the _named tuple_.

Examples:
    >>> from xloft import NamedTuple
    >>> nt = NamedTuple(x=10, y="Hello")
    >>> nt.x
    10
    >>> nt.z
    KeyError
    >>> len(nt)
    2
    >>> nt.keys()
    ["x", "y"]
    >>> nt.values()
    [10, "Hello"]
    >>> nt.has_key("x")
    True
    >>> nt.has_key("z")
    False
    >>> nt.has_value(10)
    True
    >>> nt.has_value([1, 2, 3])
    False
    >>> nt.get("x")
    10
    >>> nt.get("z")
    None
    >>> nt.update("z", [1, 2, 3])
    KeyError
    >>> d = nt.to_dict()
    >>> d["x"]
    10
    >>> nt["z"] = [1, 2, 3]
    TypeError
    >>> nt.update("x", 20)
    >>> nt.x
    20
    >>> for key, val in nt.items():
    ...     print(f"Key: {key}, Value: {val}")
    "Key: x, Value: 10"
    "Key: y, Value: Hello"
    >>> nt.x = 20
    Error: AttributeDoesNotSetValue
    >>> del nt.x
    Error: AttributeCannotBeDelete
"""

from typing import Any

from xloft.errors import (
    AttributeCannotBeDelete,
    AttributeDoesNotSetValue,
)


class NamedTuple:
    """This class imitates the behavior of the _named tuple_."""

    def __init__(self, **kwargs: dict[str, Any]) -> None:  # noqa: D107
        self.__dict__["_jWjSaNy1RbtQinsN_keys"] = []
        for name, value in kwargs.items():
            self.__dict__[name] = value
            self._jWjSaNy1RbtQinsN_keys.append(name)

    def __len__(self) -> int:
        """Get the number of elements.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> len(nt)
            2

        Returns:
            The number of elements in the tuple.
        """
        return len(self._jWjSaNy1RbtQinsN_keys)

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
        raise AttributeDoesNotSetValue(name)

    def __delattr__(self, name: str) -> None:
        """Blocked Deleter."""
        raise AttributeCannotBeDelete(name)

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
        keys: list[str] = self._jWjSaNy1RbtQinsN_keys
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
        keys: list[str] = self._jWjSaNy1RbtQinsN_keys
        return {key: attrs[key] for key in keys}

    def items(self) -> list[tuple[str, Any]]:
        """Return a set-like object providing a view on the NamedTuple's items.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> for key, val in nt.items():
            ...     print(f"Key: {key}, Value: {val}")
            "Key: x, Value: 10"
            "Key: y, Value: Hello"

        Returns:
            list[tuple[str, Any]]
        """
        attrs: dict[str, Any] = self.__dict__
        keys: list[str] = self._jWjSaNy1RbtQinsN_keys
        return [(key, attrs[key]) for key in keys]

    def keys(self) -> list[str]:
        """Get a list of keys.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.keys()
            ["x", "y"]

        Returns:
            List of keys.
        """
        return self._jWjSaNy1RbtQinsN_keys

    def values(self) -> list[Any]:
        """Get a list of values.

        Examples:
            >>> from xloft import NamedTuple
            >>> nt = NamedTuple(x=10, y="Hello")
            >>> nt.values()
            [10, "Hello"]

        Returns:
            List of values.
        """
        attrs: dict[str, Any] = self.__dict__
        keys: list[str] = self._jWjSaNy1RbtQinsN_keys
        return [attrs[key] for key in keys]

    def has_key(self, key: str) -> bool:
        """Returns True if the key exists, otherwise False.

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
        keys: list[str] = self._jWjSaNy1RbtQinsN_keys
        return key in keys

    def has_value(self, value: Any) -> bool:
        """Returns True if the value exists, otherwise False.

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
        values = self.values()
        return value in values
