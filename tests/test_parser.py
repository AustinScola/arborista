"""Test arborista.parser."""
from abc import ABC

from arborista.parser import Parser


def test_inheritance() -> None:
    """Test arborista.parser.Parser inheritance."""
    assert issubclass(Parser, ABC)
