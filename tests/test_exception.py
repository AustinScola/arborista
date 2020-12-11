"""Test arborista.exception."""
from arborista.exception import ArboristaException


def test_inheritance() -> None:
    """Test arborista.exception.ArboristaException inheritance."""
    assert issubclass(ArboristaException, Exception)
