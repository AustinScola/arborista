"""Python names to be imported as other names."""
from typing import List, Optional

from arborista.node import Node
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.python_node import PythonNode


class NameAsNames(PythonNode):
    """Python names to be imported as other names."""
    def __init__(self, first: NameAsName, rest: List[NameAsName], parent: Optional[Node] = None):
        super().__init__(parent)

        self.first: NameAsName = first
        self.rest: List[NameAsName] = rest
