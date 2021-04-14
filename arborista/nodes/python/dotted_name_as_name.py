"""A Python dotted name as another name."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


class DottedNameAsName(PythonNode):
    """A Python dotted name as another name."""
    def __init__(self,
                 dotted_name: DottedName,
                 name: Optional[Name] = None,
                 parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.dotted_name: DottedName = dotted_name
        self.name: Optional[Name] = name
