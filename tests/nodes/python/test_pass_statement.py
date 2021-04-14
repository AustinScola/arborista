"""Test arborista.nodes.python.pass_statement."""
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.small_statement import SmallStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.pass_statement.PassStatement inheritance."""
    assert issubclass(PassStatement, SmallStatement)
