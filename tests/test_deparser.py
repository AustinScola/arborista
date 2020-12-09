"""Test arborista.deparser."""
from abc import ABC

from arborista.deparser import Deparser


def test_inheritance() -> None:
    """Test arborista.deparser.Deparser inheritance."""
    assert issubclass(Deparser, ABC)
