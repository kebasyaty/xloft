"""Testing NamedTuple."""

import pytest

from xloft import NamedTuple
from xloft.errors import (
    AttributeCannotBeDelete,
    AttributeDoesNotSetValue,
)


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


@pytest.mark.xfail(raises=TypeError)
def test_forbidden_type_of_argument() -> None:
    """NamedTuple is not supported for arguments."""
    NamedTuple(x=10, y="Hello", z=NamedTuple(x=10, y="Hello"))
