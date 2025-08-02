"""Named Tuple."""

from typing import Any, Callable


class NamedTuple:
    """Named Tuple."""

    def __init__(self, **kwargs: dict[str, Any]) -> None:  # noqa: D107
        for key, value in kwargs.items():
            self.__dict__[key] = value
        else:
            self.add_property()

    def add_property(self) -> None:
        """Add properties."""
        for name, data in self.__dict__.items():
            if not callable(data):

                def getter(self) -> Callable[[Any, Any], None] | None:  # type: ignore[no-untyped-def]
                    """To add Getter."""
                    return self.__dict__.get(name)

                setattr(self.__class__, name, property(getter, None, None, "Getter."))
