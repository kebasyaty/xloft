"""Testing Humanism."""

from  xloft import to_human_size

def test_to_human_size() -> None:
    """Testing a `to_human_size` method."""
    data: dict[int, str] = {
        200: "200 bytes",
    }
    for key, val in data.items():
        assert to_human_size(key) == val
