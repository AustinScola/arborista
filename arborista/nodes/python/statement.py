"""A Python statement."""
from typing import Iterable, List

from arborista.node import Node


class Statement(Node):  # pylint: disable=too-few-public-methods
    """A Python statement."""


Statements = Iterable[Statement]
StatementList = List[Statement]
