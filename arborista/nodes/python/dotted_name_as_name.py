"""A Python dotted name as another name."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

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

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.dotted_name != other.dotted_name:
            return False

        if self.name != other.name:
            return False

        return True
