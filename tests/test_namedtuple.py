"""Testing NamedTuple."""

import pytest

from xloft import NamedTuple
from xloft.errors import (
    AttributeCannotBeDelete,
    AttributeDoesNotSetValue,
)


@pytest.mark.xfail(raises=AttributeDoesNotSetValue)
def test_fail_setter() -> None:
    """Setter is not supported."""
    nt = NamedTuple(x=10, y="Hello")
    nt.x = 20


@pytest.mark.xfail(raises=AttributeCannotBeDelete)
def test_fail_deletter() -> None:
    """Deletter is not supported."""
    nt = NamedTuple(x=10, y="Hello")
    del nt.x


@pytest.mark.xfail(raises=KeyError)
def test_fail_access_to_attribute() -> None:
    """An attempt to access the non-existent attribute."""
    nt = NamedTuple(x=10, y="Hello")
    nt.z


@pytest.mark.xfail(raises=AttributeDoesNotSetValue)
def test_fail_add_new_attribute() -> None:
    """It is forbidden to add new attributes."""
    nt = NamedTuple(x=10, y="Hello")
    nt.z = 20


@pytest.mark.xfail(raises=KeyError)
def test_fail_getitem() -> None:
    """Access by  name of key."""
    nt = NamedTuple(x=10, y="Hello")
    nt["z"]


def test_separate_arguments() -> None:
    """Create with separate arguments."""
    nt = NamedTuple(x=10, y="Hello")
    assert nt.x == 10
    assert nt.y == "Hello"


def test_kwargs_arguments() -> None:
    """Create with kwargs arguments."""
    d = {"x": 10, "y": "Hello"}
    nt = NamedTuple(**d)
    assert nt.x == 10
    assert nt.y == "Hello"


def test_getitem() -> None:
    """Access by  name of key."""
    nt = NamedTuple(x=10, y="Hello")
    assert nt["x"] == 10
    assert nt["y"] == "Hello"


def test_get_method() -> None:
    """Testing a `get` method."""
    d = {"x": 10, "y": "Hello"}
    nt = NamedTuple(**d)
    assert nt.get("x") == 10
    assert nt.get("y") == "Hello"
    assert nt.get("z") == None
    assert nt.get("z", [1, 2, 3]) == [1, 2, 3]


def test_update_method() -> None:
    """Testing a `update` method."""
    d = {"x": 10, "y": "Hello"}
    nt = NamedTuple(**d)
    assert nt.x == 10
    assert nt.y == "Hello"
    nt.update("x", 20)
    nt.update("y", "Hi")
    assert nt.x == 20
    assert nt.y == "Hi"


def test_convert_to_dict() -> None:
    """Convert to the dictionary."""
    nt = NamedTuple(x=10, y="Hello")
    d = nt.to_dict()
    assert isinstance(d, dict) == True
    assert d["x"] == 10
    assert d["y"] == "Hello"


def test_in_loop() -> None:
    """In the cycle `for`."""
    d = {"x": 10, "y": "Hello"}
    nt = NamedTuple(**d)
    for key, val in nt.to_dict().items():
        assert val == d[key]
