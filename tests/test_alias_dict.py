"""Testing a `AliasDict` module."""

from __future__ import annotations

from xloft import AliasDict


class TestNegative:
    """Negative tests."""

    def test_stub(self) -> None:
        """Testing stub."""
        assert True


class TestPositive:
    """Positive tests."""

    def test_stub(self) -> None:
        """Testing stub."""
        d = [([1, 2, 3], "Hello!")]
        ad = AliasDict(d)
        store = ad.store
        assert store.get([1, 2, 3]) == "Hello!"
