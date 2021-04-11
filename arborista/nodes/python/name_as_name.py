"""A Python name to be imported as another name."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


class NameAsName(PythonNode):
    """A Python name to be imported as another name."""
    def __init__(self, name: Name, new_name: Optional[Name] = None, parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name
        self.new_name: Optional[Name] = new_name

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.name != other.name:
            return False

        if self.new_name != other.new_name:
            return False

        return True
