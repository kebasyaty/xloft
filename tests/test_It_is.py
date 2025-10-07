"""Testing a `ItIs` module."""

from __future__ import annotations

from xloft.it_is import (
    is_number,
)


def test_is_number() -> None:
    """Testing a `is_number` method."""
    # Negative tests.
    for item in [
        "",
        " ",
        "1230.",
        "123ayu456",
        "0x5",
        "0o5",
    ]:
        assert not is_number(item)
    # Positive tests.
    for item in [
        "-1230.0123",
        "+1230.0123",
        "1230.0123",
        "1230.0",
        "1230",
        "1.23e-5",
        "1.23E-5",
        "1.23e-05",
        "1.23E-05",
        ".5",
    ]:
        assert is_number(item)
