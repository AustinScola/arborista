"""A Python small statement."""
from typing import Iterable, List

from arborista.nodes.python.python_node import PythonNode


class SmallStatement(PythonNode):
    """A Python small statement."""


SmallStatements = Iterable[SmallStatement]
SmallStatementList = List[SmallStatement]
