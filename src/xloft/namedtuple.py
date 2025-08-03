"""Named Tuple."""

from typing import Any

from xloft.errors import (
    AttributeCannotBeDelete,
    AttributeDoesNotSetValue,
)


class NamedTuple:
    """Named Tuple."""

    def __init__(self, **kwargs: dict[str, Any]) -> None:  # noqa: D107
        for name, value in kwargs.items():
            self.__dict__[name] = value

    def __getattr__(self, name: str) -> Any:
        """Getter."""
        return self.__dict__[name]

    def __setattr__(self, name: str, value: Any) -> None:
        """Fail Setter."""
        raise AttributeDoesNotSetValue(name)

    def __delattr__(self, name: str) -> None:
        """Fail Deleter."""
        raise AttributeCannotBeDelete(name)

    def get(self, key: str, default: Any | None = None) -> Any | None:
        """Return the value for key if key is in the dictionary, else default."""
        value = self.__dict__.get(key)
        if value is not None:
            return value
        return default

    def update(self, key: str, value: Any) -> Any:
        """Update a value of key.

        Attention: This is an uncharacteristic action for the type `tuple`.
        """
        self.__dict__[key] = value

    def to_dict(self) -> dict[str, Any]:
        """Convert to the dictionary."""
        return {key: value for key, value in self.__dict__.items() if not callable(value)}

    def items(self) -> list[tuple[str, Any]]:
        """Return a set-like object providing a view on the NamedTuple's items."""
        return [(key, value) for key, value in self.__dict__.items() if not callable(value)]
