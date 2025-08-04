"""NamedTuple.

This module contains the implementation of the `NamedTuple` class.

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
    """Named Tuple."""

    VAR_NAME_FOR_KEYS_LIST: str = "_jWjSaNy1RbtQinsN_keys"

    def __init__(self, **kwargs: dict[str, Any]) -> None:  # noqa: D107
        vnkl = self.__class__.VAR_NAME_FOR_KEYS_LIST
        self.__dict__[vnkl] = []
        for name, value in kwargs.items():
            self.__dict__[name] = value
            self.__dict__[vnkl].append(name)

    def __len__(self) -> int:
        """Get the number of elements."""
        return len(self.__dict__[self.__class__.VAR_NAME_FOR_KEYS_LIST])

    def __getattr__(self, name: str) -> Any:
        """Getter."""
        return self.__dict__[name]

    def __setattr__(self, name: str, value: Any) -> None:
        """Fail Setter."""
        raise AttributeDoesNotSetValue(name)

    def __delattr__(self, name: str) -> None:
        """Fail Deleter."""
        raise AttributeCannotBeDelete(name)

    def get(self, key: str) -> Any:
        """Return the value for key if key is in the dictionary, else `None`."""
        value = self.__dict__.get(key)
        if value is not None:
            return value
        return None

    def update(self, key: str, value: Any) -> Any:
        """Update a value of key.

        Attention: This is an uncharacteristic action for the type `tuple`.
        """
        keys: list[str] = self.__dict__[self.__class__.VAR_NAME_FOR_KEYS_LIST]
        if not key in keys:
            err_msg = f"The key `{key}` is missing!"
            raise KeyError(err_msg)
        self.__dict__[key] = value

    def to_dict(self) -> dict[str, Any]:
        """Convert to the dictionary."""
        attrs: dict[str, Any] = self.__dict__
        keys: list[str] = attrs[self.__class__.VAR_NAME_FOR_KEYS_LIST]
        return {key: attrs[key] for key in keys}

    def items(self) -> list[tuple[str, Any]]:
        """Return a set-like object providing a view on the NamedTuple's items."""
        attrs: dict[str, Any] = self.__dict__
        keys: list[str] = attrs[self.__class__.VAR_NAME_FOR_KEYS_LIST]
        return [(key, attrs[key]) for key in keys]

    def keys(self) -> list[str]:
        """Get a list of keys."""
        return self.__dict__[self.__class__.VAR_NAME_FOR_KEYS_LIST]

    def values(self) -> list[Any]:
        """Get a list of values."""
        attrs: dict[str, Any] = self.__dict__
        keys: list[str] = attrs[self.__class__.VAR_NAME_FOR_KEYS_LIST]
        return [attrs[key] for key in keys]

    def has_key(self, key: str) -> bool:
        """Returns True if the key exists, otherwise False."""
        keys: list[str] = self.__dict__[self.__class__.VAR_NAME_FOR_KEYS_LIST]
        return key in keys

    def has_value(self, value: Any) -> bool:
        """Returns True if the value exists, otherwise False."""
        values = self.values()
        return value in values
