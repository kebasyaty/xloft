"""Testing a `AliasDict` module."""

from __future__ import annotations

from xloft import AliasDict


class TestPositive:
    """Positive tests."""

    def test_create_empty(self) -> None:
        """Test the creation of an empty dictionary."""
        adict = AliasDict()
        assert isinstance(adict.store, list)
        assert isinstance(adict.all_alias_set, set)
        assert adict.store == []
        assert adict.all_alias_set == set()

    def test_get_value_from_empty(self) -> None:
        """Test get value from empty dictionary."""
        adict = AliasDict()
        assert adict.get("alias is missing") is None
