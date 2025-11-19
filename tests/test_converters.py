"""Testing a `Converters` module."""

from __future__ import annotations

from xloft.converters import int_to_roman, roman_to_int, to_human_size
from xloft.converters.roman import ROMAN


def test_to_human_size() -> None:
    """Testing a `to_human_size` method."""
    sample_data: dict[int, str] = {
        200: "200 bytes",
        1023: "1023 bytes",
        1024: "1 KB",
        1536: "1.5 KB",
        1048574: "1023.998 KB",
        1048575: "1023.999 KB",
        1048576: "1 MB",
        1572864: "1.5 MB",
        1073741822: "1023.999998 MB",
        1073741823: "1023.999999 MB",
        1073741824: "1 GB",
        1610612736: "1.5 GB",
        1099511627774: "1023.999999998 GB",
        1099511627775: "1023.999999999 GB",
        1099511627776: "1 TB",
        1649267441664: "1.5 TB",
    }
    for key, val in sample_data.items():
        assert to_human_size(key) == val


def test_int_to_roman() -> None:
    """Testing a `int_to_roman` method."""
    data = [*ROMAN, (3, "III"), (58, "LVIII"), (1994, "MCMXCIV")]
    for item in data:
        assert int_to_roman(item[0]) == item[1]


def test_roman_to_int() -> None:
    """Testing a `roman_to_int` method."""
    data = [*ROMAN, (3, "III"), (58, "LVIII"), (1994, "MCMXCIV")]
    for item in data:
        assert roman_to_int(item[1]) == item[0]
