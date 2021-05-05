"""A Python positional parameter."""
from typing import Iterable, List, Optional

from arborista.node import Node, NodeIterator
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


class PositionalParameter(PythonNode):
    """A Python positional parameter."""
    def __init__(self,
                 name: Name,
                 annotation: Optional[Expression] = None,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name
        self.annotation: Optional[Expression] = annotation

    def iterate_children(self) -> NodeIterator:
        yield self.name


PositionalParameters = Iterable[PositionalParameter]
PositionalParameterList = List[PositionalParameter]
