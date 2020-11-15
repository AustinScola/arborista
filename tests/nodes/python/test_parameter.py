"""Test arborista.nodes.python.parameter."""
from arborista.nodes.python.parameter import Parameter
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.parameter.Parameter inheritance."""
    assert issubclass(Parameter, PythonNode)
