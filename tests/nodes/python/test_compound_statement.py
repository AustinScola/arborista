"""Test arborista.nodes.python.compound_statement."""
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.statement import Statement


def test_inheritance() -> None:
    """Test arborista.nodes.python.compound_statement.CompoundStatement inheritance."""
    assert issubclass(CompoundStatement, Statement)
