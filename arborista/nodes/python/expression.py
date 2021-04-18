"""A Python expression."""
from typing import Iterable

from arborista.nodes.python.argument import Argument
from arborista.nodes.python.python_node import PythonNode


class Expression(Argument, PythonNode):
    """A Python expression."""


Expressions = Iterable[Expression]
