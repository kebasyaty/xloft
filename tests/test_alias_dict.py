"""Testing a `AliasDict` module."""

from __future__ import annotations

from xloft import AliasDict


class TestPositive:
    """Positive tests."""

    def test_create_empty(self) -> None:
        """Test the creation of an empty dictionary."""
        d = AliasDict()
        assert isinstance(d.store, list)
        assert isinstance(d.all_alias_set, set)
        assert d.store == []
        assert d.all_alias_set == set()

    def test_get_value_from_empty(self) -> None:
        """Test get value from empty dictionary."""
        d = AliasDict()
        assert d.get("alias is missing") is None

    def test_set_value_to_empty(self) -> None:
        """Test set value to empty dictionary."""
        d = AliasDict()

        d.set("alias name", "Hello world!")
        assert d.get("alias name") == "Hello world!"

        d.set(5, 5)
        assert d.get(5) == 5

        d.set(5.1, 5.1)
        assert d.get(5.1) == 5.1

        assert "alias name" in d.all_alias_set
        assert 5 in d.all_alias_set
        assert 5.1 in d.all_alias_set
