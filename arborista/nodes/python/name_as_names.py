"""Python names to be imported as other names."""
from typing import Any, List, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.python_node import PythonNode


class NameAsNames(PythonNode):
    """Python names to be imported as other names."""
    def __init__(self, first: NameAsName, rest: List[NameAsName], parent: Optional[Node] = None):
        super().__init__(parent)

        self.first: NameAsName = first
        self.rest: List[NameAsName] = rest

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.first != other.first:
            return False

        if self.rest != other.rest:
            return False

        return True
