"""Testing NamedTuple."""

import pytest

from xloft import NamedTuple
from xloft.errors import NotSettingValueError


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


@pytest.mark.xfail(raises=NotSettingValueError)
def test_fail_setter() -> None:
    """Setter is not supported."""
    nt = NamedTuple(x=10)
    nt.x = 20


# @pytest.mark.xfail(raises=AttributeError)
# def test_fail_access_to_field() -> None:
#     """An attempt to access the non-existent field."""
#     nt = NamedTuple(x=10, y="Hello")
#     nt.z
