"""Test arborista.nodes.python.import_statement."""
from arborista.nodes.python.import_statement import ImportStatement
from arborista.nodes.python.small_statement import SmallStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.import_statement.ImportStatement inheritance."""
    assert issubclass(ImportStatement, SmallStatement)
