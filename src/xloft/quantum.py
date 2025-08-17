"""A set of tools for quantum calculations.

A qubit in a regular computer is some algorithm that is executed in
one iteration of a cycle in a separate processor thread.

The quantum state of such a qubit is the potential result of the executed algorithm.

The result of the qubit operation can be `True`, `False`, `None`, `int`, `float`, `str`, `Exception`, etc.

How to use the qubit result is up to you to decide based on your goals.
"""

import multiprocessing


def count_qubits() -> int:
    """Counting the number of qubits of your computer."""
    return multiprocessing.cpu_count()
