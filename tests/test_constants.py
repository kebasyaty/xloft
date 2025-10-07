"""Testing Constants."""

from __future__ import annotations

from xloft.constants import REGEX_IS_NUMBER


def test_db_root() -> None:
    """Test a REGEX_IS_NUMBER variable."""
    original_pattern_string = REGEX_IS_NUMBER.pattern
    assert original_pattern_string == r"^[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$"
