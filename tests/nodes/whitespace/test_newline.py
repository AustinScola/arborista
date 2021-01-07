"""Test arborista.nodes.whitespace.newline."""
from arborista.nodes.whitespace.newline import Newline
from arborista.nodes.whitespace.whitespace import Whitespace


def test_inheritance() -> None:
    """Test arborista.nodes.whitespace.newline.Newline inheritance."""
    assert issubclass(Newline, Whitespace)
