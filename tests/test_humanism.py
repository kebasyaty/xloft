"""Testing Humanism."""

from  xloft import to_human_size

def test_to_human_size() -> None:
    """Testing a `to_human_size` method."""
    data: dict[int, str] = {
        200: "200 bytes",
        1023: "1023 bytes",
        1024: "1 KB",
        1536: "1.5 KB",
        1048575: "1024 KB",
        1048576: "1 MB",
        1572864: "1.5 MB",
        1073741823: "1024 MB",
        1073741824: "1 GB",
        1610612736: "1.5 GB",
        1099511627775: "1024 GB",
        1099511627776: "1 TB",
        1649267441664: "1.5 TB",
    }
    for key, val in data.items():
        assert to_human_size(key) == val
