"""Testing a `Quantum` module."""

from __future__ import annotations

import multiprocessing

from xloft.quantum import count_qubits


def test_count_qubits() -> None:
    """Testing a count_qubits method."""
    assert count_qubits() == multiprocessing.cpu_count()
