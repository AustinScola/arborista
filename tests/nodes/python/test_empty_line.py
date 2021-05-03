"""Test arborista.nodes.python.empty_line."""
from arborista.nodes.python.empty_line import EmptyLine
from arborista.nodes.python.statement import Statement


def test_inheritance() -> None:
    """Test arborista.nodes.python.empty_line.EmptyLine inheritance."""
    assert issubclass(EmptyLine, Statement)
