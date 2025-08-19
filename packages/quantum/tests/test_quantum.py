"""Testing a `Quantum` module."""

from __future__ import annotations

import multiprocessing

from src.quantum import LoopMode, QuantumLoop, count_qubits


def test_count_qubits() -> None:
    """Testing a count_qubits method."""
    assert count_qubits() == multiprocessing.cpu_count()


class TestQuantumLoop:
    """Testing a `QuantumLoop` class."""

    def quantum(self, item):
        """Test task."""
        return item * item

    def test_process_pool(self) -> None:
        """Testing a `process_pool` method."""
        data = range(10)
        qloop = QuantumLoop(self.quantum, data)
        assert qloop.run() == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    def test_thread_pool(self) -> None:
        """Testing a `thread_pool` method."""
        data = range(10)
        qloop = QuantumLoop(self.quantum, data, mode=LoopMode.THREAD_POOL)
        assert qloop.run() == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
