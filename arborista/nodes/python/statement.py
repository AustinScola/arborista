"""A Python statement."""
from typing import Generator, Iterable, Iterator, List

from arborista.nodes.python.python_node import PythonNode


class Statement(PythonNode):
    """A Python statement."""


Statements = Iterable[Statement]
StatementList = List[Statement]
StatementGenerator = Generator[Statement, None, None]
StatementIterator = Iterator[Statement]
