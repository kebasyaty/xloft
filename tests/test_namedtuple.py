"""Testing NamedTuple."""

import pytest

from xloft import NamedTuple
from xloft.errors import (
    AttributeCannotBeDelete,
    AttributeDoesNotSetValue,
)


class TestNegative:
    """Negative tests."""

    @pytest.mark.xfail(raises=AttributeDoesNotSetValue)
    def test_fail_setter(self) -> None:
        """Setter is not supported."""
        nt = NamedTuple(x=10, y="Hello")
        nt.x = 20

    @pytest.mark.xfail(raises=AttributeCannotBeDelete)
    def test_fail_deletter(self) -> None:
        """Deletter is not supported."""
        nt = NamedTuple(x=10, y="Hello")
        del nt.x

    @pytest.mark.xfail(raises=KeyError)
    def test_fail_access_to_attribute(self) -> None:
        """An attempt to access the non-existent attribute."""
        nt = NamedTuple(x=10, y="Hello")
        nt.z

    @pytest.mark.xfail(raises=AttributeDoesNotSetValue)
    def test_fail_add_new_attribute(self) -> None:
        """It is forbidden to add new attributes."""
        nt = NamedTuple(x=10, y="Hello")
        nt.z = 20

    @pytest.mark.xfail(raises=TypeError)
    def test_fail_getitem(self) -> None:
        """Access by  name of key."""
        nt = NamedTuple(x=10, y="Hello")
        nt["x"]

    @pytest.mark.xfail(raises=TypeError)
    def test_fail_setitem(self) -> None:
        """Fail Setter."""
        nt = NamedTuple(x=10, y="Hello")
        nt["x"] = 20

    @pytest.mark.xfail(raises=KeyError)
    def test_fail_update_method(self) -> None:
        """Testing a `update` method."""
        d = {"x": 10, "y": "Hello"}
        nt = NamedTuple(**d)
        nt.update("z", [1, 2, 3])


class TestPositive:
    """Positive tests."""

    def test_separate_arguments(self) -> None:
        """Create with separate arguments."""
        nt = NamedTuple(x=10, y="Hello", _id=123)
        assert nt.x == 10
        assert nt.y == "Hello"
        assert nt._id == 123

    def test_kwargs_arguments(self) -> None:
        """Create with kwargs arguments."""
        d = {"x": 10, "y": "Hello", "_id": 123}
        nt = NamedTuple(**d)
        assert nt.x == 10
        assert nt.y == "Hello"
        assert nt._id == 123

    def test_get_method(self) -> None:
        """Testing a `get` method."""
        d = {"x": 10, "y": "Hello"}
        nt = NamedTuple(**d)
        assert nt.get("x") == 10
        assert nt.get("y") == "Hello"
        assert nt.get("z") == None

    def test_update_method(self) -> None:
        """Testing a `update` method."""
        d = {"x": 10, "y": "Hello"}
        nt = NamedTuple(**d)
        assert nt.x == 10
        assert nt.y == "Hello"
        nt.update("x", 20)
        nt.update("y", "Hi")
        assert nt.x == 20
        assert nt.y == "Hi"

    def test_to_dict_method(self) -> None:
        """Convert to the dictionary."""
        nt = NamedTuple(x=10, y="Hello")
        d = nt.to_dict()
        assert isinstance(d, dict) == True
        assert d["x"] == 10
        assert d["y"] == "Hello"

    def test_items_method(self) -> None:
        """In the cycle `for`."""
        d = {"x": 10, "y": "Hello"}
        nt = NamedTuple(**d)
        for key, val in nt.items():
            assert val == d[key]

    def test_len_method(self) -> None:
        """Get the number of elements."""
        d = {"x": 10, "y": "Hello"}
        nt = NamedTuple(**d)
        assert len(nt) == 2

    def test_keys_method(self) -> None:
        """Get a list of keys."""
        d = {"x": 10, "y": "Hello"}
        nt = NamedTuple(**d)
        assert nt.keys() == ["x", "y"]

    def test_values_method(self) -> None:
        """Get a list of values."""
        d = {"x": 10, "y": "Hello"}
        nt = NamedTuple(**d)
        assert nt.values() == [10, "Hello"]

    def test_has_key(self) -> None:
        """Returns True if the key exists, otherwise False."""
        nt = NamedTuple(x=10, y="Hello")
        assert nt.has_key("x") == True
        assert nt.has_key("y") == True
        assert nt.has_key("z") == False

    def test_has_value(self) -> None:
        """Returns True if the value exists, otherwise False."""
        nt = NamedTuple(x=10, y="Hello")
        assert nt.has_value(10) == True
        assert nt.has_value("Hello") == True
        assert nt.has_value([1, 2, 3]) == False
