"""Test arborista.nodes.python.return_statement."""
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.return_statement import ReturnStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.return_statement.ReturnStatement inheritance."""
    assert issubclass(ReturnStatement, FlowStatement)
