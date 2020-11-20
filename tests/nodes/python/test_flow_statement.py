"""Test arborista.nodes.python.flow_statement."""
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.small_statement import SmallStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.flow_statement.FlowStatement inheritance."""
    assert issubclass(FlowStatement, SmallStatement)
