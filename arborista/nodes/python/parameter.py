"""A Python parameter."""
from typing import Any, Iterable, List, Optional

from arborista.node import Node
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


class Parameter(PythonNode):
    """A Python parameter."""
    def __init__(self, name: Name, parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Parameter):
            return False
        return self.name == other.name


Parameters = Iterable[Parameter]
ParameterList = List[Parameter]
