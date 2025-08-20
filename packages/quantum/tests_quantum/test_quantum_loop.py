"""Testing a `Quantum` module."""

from __future__ import annotations

from src import LoopMode, QuantumLoop


class TestQuantumLoop:
    """Testing a `QuantumLoop` class."""

    @staticmethod
    def task(item: int) -> int:
        """Test Quantum."""
        return item * item

    def test_process_pool(self) -> None:
        """Testing a `process_pool` method."""
        data = range(10)
        qloop = QuantumLoop(self.task, data)
        assert qloop.run() == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    def test_thread_pool(self) -> None:
        """Testing a `thread_pool` method."""
        data = range(10)
        qloop = QuantumLoop(self.task, data, mode=LoopMode.THREAD_POOL)
        assert qloop.run() == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
