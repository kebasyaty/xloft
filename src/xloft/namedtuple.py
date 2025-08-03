"""Named Tuple."""

from typing import Any

from xloft.errors import (
    AttributeCannotBeDelete,
    AttributeDoesNotSetValue,
)


class NamedTuple:
    """Named Tuple."""

    def __init__(self, **kwargs: dict[str, Any]) -> None:  # noqa: D107
        self.__dict__["_keys"] = []
        for name, value in kwargs.items():
            self.__dict__[name] = value
            self._keys.append(name)
        else:
            self.__dict__["_len"] = len(self._keys)

    def __len__(self) -> int:
        """Get the number of elements."""
        return self._len

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
        if not key in self._keys:
            err_msg = f"The key `{key}` is missing!"
            raise KeyError(err_msg)
        self.__dict__[key] = value

    def to_dict(self) -> dict[str, Any]:
        """Convert to the dictionary."""
        return {
            key: value
            for key, value in self.__dict__.items()
            if not callable(value) and not key in ["_keys", "_len"]
        }

    def items(self) -> list[tuple[str, Any]]:
        """Return a set-like object providing a view on the NamedTuple's items."""
        return [
            (key, value)
            for key, value in self.__dict__.items()
            if not callable(value) and not key in ["_keys", "_len"]
        ]
