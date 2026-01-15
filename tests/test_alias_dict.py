"""Testing a `AliasDict` module."""

from __future__ import annotations

import pytest

from xloft import AliasDict
from xloft.errors import (
    AttributeCannotBeDeleteError,
    AttributeDoesNotGetValueError,
    AttributeDoesNotSetValueError,
)


class TestNegative:
    """Negative tests."""

    @pytest.mark.xfail(raises=AttributeDoesNotGetValueError, strict=True)
    def test_fail_getter(self) -> None:
        """Getter is not supported."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
        ]

        d = AliasDict(data)
        d.en  # noqa: B018

    @pytest.mark.xfail(raises=AttributeDoesNotSetValueError, strict=True)
    def test_fail_setter(self) -> None:
        """Setter is not supported."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
        ]

        d = AliasDict(data)
        d.en = "Some test"

    @pytest.mark.xfail(raises=AttributeCannotBeDeleteError, strict=True)
    def test_fail_deletter(self) -> None:
        """Deletter is not supported."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
        ]

        d = AliasDict(data)
        del d.en


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

        d.add({"alias name"}, "Hello world!")
        assert d.get("alias name") == "Hello world!"

        d.add({5}, 5)
        assert d.get(5) == 5

        d.add({5.1}, 5.1)
        assert d.get(5.1) == 5.1

        assert "alias name" in d.__dict__["all_alias_set"]
        assert 5 in d.__dict__["all_alias_set"]
        assert 5.1 in d.__dict__["all_alias_set"]

    def test_len(self) -> None:
        """Get the number of elements in the dictionary."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
        ]

        d = AliasDict(data)

        assert len(d) == 3

    def test_get_value(self) -> None:
        """Test get value by key."""
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

    def test_add_key_and_value_pair(self) -> None:
        """Test add a new key and value pair."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
        ]

        d = AliasDict(data)

        d.add({"Turkish", "tr"}, "libstemmer_tr")

        assert d.get("English") == "lemmatize_en_all"
        assert d.get("en") == "lemmatize_en_all"

        assert d.get("Russian") == "lemmatize_ru_all"
        assert d.get("ru") == "lemmatize_ru_all"

        assert d.get("German") == "lemmatize_de_all"
        assert d.get("de") == "lemmatize_de_all"

        assert d.get("Turkish") == "libstemmer_tr"
        assert d.get("tr") == "libstemmer_tr"

    def test_update_value(self) -> None:
        """Test update value by key."""
        data = [({"five", 5}, "Five it's me!")]

        d = AliasDict(data)

        assert d.get("five") == "Five it's me!"
        assert d.get(5) == "Five it's me!"

        d.update(5, "Hello world!")

        assert d.get("five") == "Hello world!"
        assert d.get(5) == "Hello world!"

    def test_delete_key_and_value(self) -> None:
        """Test delete key and value from dictionary."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
            ({"five", 5}, "Five it's me!"),
        ]

        d = AliasDict(data)

        assert d.get("five") == "Five it's me!"
        assert d.get(5) == "Five it's me!"

        d.delete(5)

        assert d.get("five") is None
        assert d.get(5) is None

    def test_add_new_alias(self) -> None:
        """Test add new alias to dictionary."""
        d = AliasDict()

        d.add({"Turkish"}, "libstemmer_tr")
        d.add_alias("Turkish", "tr")

        assert d.get("Turkish") == "libstemmer_tr"
        assert d.get("tr") == "libstemmer_tr"

    def test_delete_alias(self) -> None:
        """Test delete alias from dictionary."""
        d = AliasDict()

        d.add({"Turkish", "tr"}, "libstemmer_tr")

        assert d.get("Turkish") == "libstemmer_tr"
        assert d.get("tr") == "libstemmer_tr"

        d.delete_alias("tr")

        assert d.get("Turkish") == "libstemmer_tr"
        assert d.get("tr") is None
        assert "tr" not in d.__dict__["all_alias_set"]

    def test_has_key(self) -> None:
        """Check if the dictionary has an alias."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
            ({"five", 5}, "Five it's me!"),
        ]

        d = AliasDict(data)

        assert d.has_key("English")
        assert d.has_key("en")
        assert d.has_key("Russian")
        assert d.has_key("ru")
        assert d.has_key("German")
        assert d.has_key("de")
        assert d.has_key("five")
        assert d.has_key(5)

        assert not d.has_key("six")
        assert not d.has_key(6)

    def test_has_value(self) -> None:
        """Check if the dictionary has a value."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
            ({"five", 5}, "Five it's me!"),
        ]

        d = AliasDict(data)

        assert d.has_value("lemmatize_en_all")
        assert d.has_value("lemmatize_ru_all")
        assert d.has_value("lemmatize_de_all")
        assert d.has_value("Five it's me!")

        assert not d.has_value("Hello world!")
        assert not d.has_value(6)

    def test_items(self) -> None:
        """Test a `items` method."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
        ]

        data_for_check = {
            "English": "lemmatize_en_all",
            "Russian": "lemmatize_ru_all",
            "German": "lemmatize_de_all",
            "en": "lemmatize_en_all",
            "ru": "lemmatize_ru_all",
            "de": "lemmatize_de_all",
        }

        d = AliasDict(data)

        for key, value in d.items():
            assert value == data_for_check[key[0]]  # pyrefly: ignore[bad-typed-dict-key]

    def test_keys(self) -> None:
        """Test a `keys` method."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
        ]

        d = AliasDict(data)

        alias_list = d.keys()

        assert isinstance(alias_list, list)
        assert len(alias_list) == 6

    def test_values(self) -> None:
        """Test a `values` method."""
        data = [
            ({"English", "en"}, "lemmatize_en_all"),
            ({"Russian", "ru"}, "lemmatize_ru_all"),
            ({"German", "de"}, "lemmatize_de_all"),
        ]

        d = AliasDict(data)

        value_list = d.values()

        assert isinstance(value_list, list)
        assert len(value_list) == 3

        for item in value_list:
            assert item in [
                "lemmatize_en_all",
                "lemmatize_ru_all",
                "lemmatize_de_all",
            ]
