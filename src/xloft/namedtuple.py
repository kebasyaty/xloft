"""Named Tuple."""

from typing import Any, Callable


class NamedTuple:
    """Named Tuple."""

    def __init__(self, **kwargs: dict[str, Any]) -> None:  # noqa: D107
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def __getattr__(self, key: str) -> Any:
        """Getter."""
        return self.__dict__[key]

    def __setattr__(self, key: str, value: Any) -> None:
        """Setter."""
        raise Exception("It is read only!")

    def __delattr__(self, str: Any, /) -> None:
        """Deleter."""
        raise Exception("It is read only!")
