"""Test arborista.exceptions.cannot_find_child_exception."""
from arborista.exception import ArboristaException
from arborista.exceptions.cannot_find_child_exception import CannotFindChildException


def test_inheritance() -> None:
    """Test arborista.exceptions.cannot_find_child_exception.CannotFindChildException inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(CannotFindChildException, ArboristaException)
