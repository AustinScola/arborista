"""Test arborista.nodes.python.subscript."""
from abc import ABC

from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.subscript import Subscript


def test_inheritance() -> None:
    """Test arborista.nodes.python.subscript.Subscript inheritance."""
    assert issubclass(Subscript, PythonNode)
    assert ABC in PythonNode.__bases__
