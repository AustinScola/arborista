"""Raised when a child node cannot be found in a parent node."""
from arborista.exception import ArboristaException


class CannotFindChildException(ArboristaException):
    """Raised when a child node cannot be found in a parent node."""
