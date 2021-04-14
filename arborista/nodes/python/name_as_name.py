"""A Python name to be imported as another name."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


class NameAsName(PythonNode):
    """A Python name to be imported as another name."""
    def __init__(self, name: Name, new_name: Optional[Name] = None, parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name
        self.new_name: Optional[Name] = new_name
