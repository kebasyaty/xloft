"""Test a `NamedTuple` module."""

from __future__ import annotations

import pytest

from xloft import NamedTuple
from xloft.errors import (
    AttributeCannotBeDeleteError,
    AttributeDoesNotSetValueError,
)


@pytest.fixture
def init_namedtuple() -> NamedTuple:
    """Init NamedTuple."""
    return NamedTuple(x=10, y="Hello")


class TestNegative:
    """Negative tests."""

    @pytest.mark.xfail(raises=AttributeDoesNotSetValueError, strict=True)
    def test_fail_setter(self, init_namedtuple) -> None:
        """Setter is not supported."""
        nt = init_namedtuple
        nt.x = 20

    @pytest.mark.xfail(raises=AttributeCannotBeDeleteError, strict=True)
    def test_fail_deletter(self, init_namedtuple) -> None:
        """Deletter is not supported."""
        nt = init_namedtuple
        del nt.x

    @pytest.mark.xfail(raises=KeyError, strict=True)
    def test_fail_access_to_attribute(self, init_namedtuple) -> None:
        """An attempt to access the non-existent attribute."""
        nt = init_namedtuple
        nt.z  # noqa: B018

    @pytest.mark.xfail(raises=AttributeDoesNotSetValueError, strict=True)
    def test_fail_add_new_attribute(self, init_namedtuple) -> None:
        """It is forbidden to add new attributes."""
        nt = init_namedtuple
        nt.z = 20

    @pytest.mark.xfail(raises=TypeError, strict=True)
    def test_fail_getitem(self, init_namedtuple) -> None:
        """Access by  name of key."""
        nt = init_namedtuple
        nt["x"]

    @pytest.mark.xfail(raises=TypeError, strict=True)
    def test_fail_setitem(self, init_namedtuple) -> None:
        """Fail Setter."""
        nt = init_namedtuple
        nt["x"] = 20

    @pytest.mark.xfail(raises=KeyError, strict=True)
    def test_fail_update_method(self, init_namedtuple) -> None:
        """Test a `update` method."""
        nt = init_namedtuple
        nt.update("z", [1, 2, 3])


class TestPositive:
    """Positive tests."""

    def test_separate_arguments(self) -> None:
        """Create with separate arguments."""
        nt = NamedTuple(x=10, y="Hello", _id=123)
        assert nt.x == 10
        assert nt.y == "Hello"
        assert nt._id == 123
        x = nt.x
        x = 5
        assert nt.x != x

    def test_kwargs_arguments(self) -> None:
        """Create with kwargs arguments."""
        d = {"x": 10, "y": "Hello", "_id": 123}
        nt = NamedTuple(**d)
        assert nt.x == 10
        assert nt.y == "Hello"
        assert nt._id == 123
        y = nt.y
        y = "Hi"
        assert nt.y != y

    def test_get_method(self, init_namedtuple) -> None:
        """Test a `get` method."""
        nt = init_namedtuple
        assert nt.get("x") == 10
        assert nt.get("y") == "Hello"
        assert nt.get("z") is None
        x = nt.get("x")
        x = 5
        assert nt.get("x") != x

    def test_update_method(self, init_namedtuple) -> None:
        """Test a `update` method."""
        nt = init_namedtuple
        assert nt.x == 10
        assert nt.y == "Hello"
        nt.update("x", 20)
        nt.update("y", "Hi")
        assert nt.x == 20
        assert nt.y == "Hi"

    def test_to_dict_method(self, init_namedtuple) -> None:
        """Convert to the dictionary."""
        nt = init_namedtuple
        d = nt.to_dict()
        assert isinstance(d, dict)
        assert d["x"] == 10
        assert d["y"] == "Hello"
        d["x"] = 5
        assert nt.x != d["x"]

    def test_items_method(self, init_namedtuple) -> None:
        """In the cycle `for`."""
        d = {"x": 10, "y": "Hello"}
        nt = init_namedtuple
        for key, val in nt.items():
            assert d[key] == val

    def test_len_method(self, init_namedtuple) -> None:
        """Get the number of elements."""
        nt = init_namedtuple
        assert len(nt) == 2

    def test_keys_method(self, init_namedtuple) -> None:
        """Get a list of keys."""
        nt = init_namedtuple
        assert nt.keys() == ["x", "y"]
        keys = nt.keys()
        keys[0] = "x2"
        assert nt.keys()[0] != keys[0]

    def test_values_method(self, init_namedtuple) -> None:
        """Get a list of values."""
        nt = init_namedtuple
        assert nt.values() == [10, "Hello"]
        values = nt.values()
        values[0] = 5
        assert nt.values()[0] != values[0]

    def test_has_key(self, init_namedtuple) -> None:
        """Returns True if the key exists, otherwise False."""
        nt = init_namedtuple
        assert nt.has_key("x")
        assert nt.has_key("y")
        assert not nt.has_key("z")

    def test_has_value(self, init_namedtuple) -> None:
        """Returns True if the value exists, otherwise False."""
        nt = init_namedtuple
        assert nt.has_value(10)
        assert nt.has_value("Hello")
        assert not nt.has_value([1, 2, 3])
