"""???"""

from __future__ import annotations

import re

REGEX_IS_NUMBER = re.compile(r"^[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$")


def is_number(value: str) -> bool:
    """Check if a string is a number.

    Only decimal numbers.
    """
    return REGEX_IS_NUMBER.match(value) is not None
