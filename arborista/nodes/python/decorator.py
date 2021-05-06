"""A Python decorator."""
from typing import Iterable, List, Optional

from arborista.node import Node
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.python_node import PythonNode


class Decorator(PythonNode):
    """A Python decorator."""
    def __init__(self,
                 name: DottedName,
                 arguments: Optional[Arguments] = None,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: DottedName = name
        self.arguments: Optional[Arguments] = arguments


Decorators = Iterable[Decorator]
DecoratorList = List[Decorator]
