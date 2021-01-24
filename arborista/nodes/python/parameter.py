"""A Python parameter."""
from typing import Any, Iterable, List, Optional

from arborista.decorators.equality.equal_type import equal_type
from arborista.node import Node, NodeIterator
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


class Parameter(PythonNode):
    """A Python parameter."""
    def __init__(self, name: Name, parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.name == other.name
        return equality

    def iterate_children(self) -> NodeIterator:
        yield self.name


Parameters = Iterable[Parameter]
ParameterList = List[Parameter]
