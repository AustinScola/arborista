"""Test arborista.nodes.python.continue_statement."""
from arborista.nodes.python.continue_statement import ContinueStatement
from arborista.nodes.python.flow_statement import FlowStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.continue_statement.ContinueStatement inheritance."""
    assert issubclass(ContinueStatement, FlowStatement)
