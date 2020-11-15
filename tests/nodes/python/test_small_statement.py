"""Test arborista.nodes.python.small_statement."""
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.small_statement import SmallStatement  # pylint: disable=unused-import


def test_inheritance() -> None:
    """Test arborista.nodes.python.small_statement.SmallStatement inheritance."""
    assert issubclass(SmallStatement, PythonNode)
