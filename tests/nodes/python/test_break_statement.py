"""Test arborista.nodes.python.break_statement."""
from arborista.nodes.python.break_statement import BreakStatement
from arborista.nodes.python.flow_statement import FlowStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.break_statement.BreakStatement inheritance."""
    assert issubclass(BreakStatement, FlowStatement)
