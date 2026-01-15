"""Test a `ItIs` module."""

from __future__ import annotations

import pytest

from xloft.itis import is_number, is_palindrome


def test_is_number() -> None:
    """Test a `is_number` method."""
    # Negative tests.
    for item in [
        "",
        " ",
        "123ayu456",
        "0x5",
        "0o5",
    ]:
        assert not is_number(item)
    # Positive tests.
    for item in [
        "-5.0",
        "+5.0",
        "5.0",
        ".5",
        "5.",
        "3.4E+38",
        "3.4E-38",
        "1.7E+308",
        "1.7E-308",
        "-1.7976931348623157e+308",
        "1.7976931348623157e+308",
        "255",
        "65535",
        "1677215",
        "4294967295",
        "281474976710655",
        "18446744073709551615",
        "79228162514264337593543950335",
        "340282366920938463463374607431768211455",
        "7809356576809509573609874689576897365487536545894358723468",
        "72028601076372765770200707816364342373431783018070841859646251155447849538676",
        "-255",
        "-65535",
        "-1677215",
        "-4294967295",
        "-281474976710655",
        "-18446744073709551615",
        "-79228162514264337593543950335",
        "-340282366920938463463374607431768211455",
        "-7809356576809509573609874689576897365487536545894358723468",
        "-72028601076372765770200707816364342373431783018070841859646251155447849538676",
    ]:
        assert is_number(item)


def test_is_palindrome() -> None:
    """Test a `is_palindrome` method."""
    with pytest.raises(TypeError):
        assert is_palindrome(123)
    with pytest.raises(ValueError, match=r"The string must not be empty!"):
        assert is_palindrome("")
    assert not is_palindrome("123")
    assert not is_palindrome("Gene")
    assert not is_palindrome("Даша")
    assert is_palindrome("22022022")
    assert is_palindrome("racecar")
    assert is_palindrome("Go hang a salami, I'm a lasagna hog")
    assert is_palindrome("топот")
    assert is_palindrome("А роза упала на лапу Азора")
