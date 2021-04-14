"""A group of names to be imported as other names."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.python_node import PythonNode


class GroupedNameAsNames(PythonNode):
    """A group of names to be imported as other names."""
    def __init__(self, name_as_names: NameAsNames, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.name_as_names: NameAsNames = name_as_names
