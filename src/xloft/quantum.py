"""A set of tools for quantum calculations."""

import concurrent.futures
import multiprocessing
from enum import Enum
from typing import Any, Callable, Iterable, Never, assert_never


def count_qubits() -> int:
    """Counting the number of qubits of your computer.

    A qubit in a regular computer is some algorithm that is executed in
    one iteration of a cycle in a separate processor thread.

    Returns:
        The number of qubits.
    """
    return multiprocessing.cpu_count()


class LoopMode(Enum):
    """Quantum loop mode."""

    PROCESS_POOL = 1
    THREAD_POOL = 2


class QuantumLoop:
    """Divide the cycle into quantums."""

    def __init__(  # noqa: D107
        self,
        quantum: Callable,
        data: Iterable[Any],
        timeout: float | None = None,
        chunksize: int = 1,
        mode: LoopMode = LoopMode.PROCESS_POOL,
    ) -> None:
        self.quantum = quantum
        self.data = data
        self.timeout = timeout
        self.chunksize = chunksize
        self.mode = mode

    def process_pool(self) -> list[Any]:
        """Better suitable for operations for which large processor resources are required."""
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(
                executor.map(
                    self.quantum,
                    self.data,
                    timeout=self.timeout,
                    chunksize=self.chunksize,
                ),
            )
        return results

    def thread_pool(self) -> list[Any]:
        """More suitable for tasks related to input-output
        (for example, network queries, file operations),
        where GIL is freed during input-output operations."""  # noqa: D205, D209
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(
                executor.map(
                    self.quantum,
                    self.data,
                    timeout=self.timeout,
                    chunksize=self.chunksize,
                ),
            )
        return results

    def run(self) -> list[Any]:
        """Run the quantum loop."""
        results: list[Any] = []
        match self.mode.value:
            case 1:
                results = self.process_pool()
            case 2:
                results = self.thread_pool()
            case _ as unreachable:
                assert_never(Never(unreachable))
        return results
