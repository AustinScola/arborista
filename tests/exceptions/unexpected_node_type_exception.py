"""Test arborista.exceptions.unexpected_node_type_exception."""
from arborista.exception import ArboristaException
from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException


def test_inheritance() -> None:
    """Test arborista.exceptions.unexpected_node_type_exception.UnexpectedNodeTypeException."""
    assert issubclass(UnexpectedNodeTypeException, ArboristaException)
