"""Testing a `Converter` module."""

from __future__ import annotations

from xloft.converter.human_size import (
    clean_cache_human_size,
    get_cache_human_size,
    to_human_size,
)

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


def test_to_human_size() -> None:
    """Testing a `to_human_size` method."""
    clean_cache_human_size()
    assert get_cache_human_size() == {}

    for key, val in sample_data.items():
        assert to_human_size(key) == val
    assert get_cache_human_size() == sample_data

    for key, val in sample_data.items():
        assert to_human_size(key) == val
    assert get_cache_human_size() == sample_data

    clean_cache_human_size()
    assert get_cache_human_size() == {}
