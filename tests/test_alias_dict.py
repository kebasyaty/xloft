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

    def test_add_value_to_empty(self) -> None:
        """Test add value to empty dictionary."""
        d = AliasDict()

        d.add("alias name", "Hello world!")
        assert d.get("alias name") == "Hello world!"

        d.add(5, 5)
        assert d.get(5) == 5

        d.add(5.1, 5.1)
        assert d.get(5.1) == 5.1

        assert "alias name" in d.all_alias_set
        assert 5 in d.all_alias_set
        assert 5.1 in d.all_alias_set

    def test_get_value(self) -> None:
        """Test get value from dictionary."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
        ]
        d = AliasDict(data)

        assert d.get("English") == "lemmatize_en_all"
        assert d.get("en") == "lemmatize_en_all"

        assert d.get("Russian") == "lemmatize_ru_all"
        assert d.get("ru") == "lemmatize_ru_all"

        assert d.get("German") == "lemmatize_de_all"
        assert d.get("de") == "lemmatize_de_all"
