"""A Python statement."""
from typing import Iterable, List

from arborista.nodes.python.python_node import PythonNode


class Statement(PythonNode):  # pylint: disable=too-few-public-methods
    """A Python statement."""


Statements = Iterable[Statement]
StatementList = List[Statement]
