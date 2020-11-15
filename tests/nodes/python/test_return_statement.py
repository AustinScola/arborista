"""Test arborista.nodes.python.return_statement."""
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.small_statement import SmallStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.return_statement.ReturnStatement inheritance."""
    assert issubclass(ReturnStatement, SmallStatement)
