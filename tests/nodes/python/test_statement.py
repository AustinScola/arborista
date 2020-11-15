"""Test arborista.nodes.python.statement."""
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.statement import Statement  # pylint: disable=unused-import


def test_inheritance() -> None:
    """Test arborista.nodes.python.statement.Statement inheritance."""
    assert issubclass(Statement, PythonNode)
