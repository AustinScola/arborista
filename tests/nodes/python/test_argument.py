"""Test arborista.nodes.python.argument."""
from abc import ABC

from arborista.nodes.python.argument import Argument
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.argument.Argument inheritance."""
    assert issubclass(Argument, PythonNode)
    assert ABC in PythonNode.__bases__
