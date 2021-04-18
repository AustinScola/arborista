"""Test arborista.nodes.python.expression."""
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.expression.Expression inheritance."""
    assert issubclass(Expression, (Argument, PythonNode))
