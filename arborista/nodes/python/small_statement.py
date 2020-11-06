"""A Python small statement."""
from typing import Iterator

from arborista.nodes.python.statement import Statement


class SmallStatement(Statement):  # pylint: disable=too-few-public-methods
    """A Python small statement."""


SmallStatements = Iterator[SmallStatement]
