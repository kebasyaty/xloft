"""Humanism."""

import math


def to_human_size(size: int) -> str:
    """Convert number of bytes to readable format."""
    idx: int = math.floor(math.log(size) / math.log(1024))
    human_size: int | float = size if size < 1024 else abs(round(size / pow(1024, idx), 2))
    order = ["bytes", "KB", "MB", "GB", "TB"][idx]
    return "{:g} {}".format(human_size, order)
