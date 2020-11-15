"""A Python small statement."""
from typing import Iterator

from arborista.nodes.python.python_node import PythonNode


class SmallStatement(PythonNode):  # pylint: disable=too-few-public-methods
    """A Python small statement."""


SmallStatements = Iterator[SmallStatement]
