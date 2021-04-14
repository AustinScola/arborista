"""A Python parameter."""
from typing import Iterable, List, Optional

from arborista.node import Node, NodeIterator
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


class Parameter(PythonNode):
    """A Python parameter."""
    def __init__(self, name: Name, parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name

    def iterate_children(self) -> NodeIterator:
        yield self.name


Parameters = Iterable[Parameter]
ParameterList = List[Parameter]
