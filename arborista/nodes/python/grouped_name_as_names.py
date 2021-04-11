"""A group of names to be imported as other names."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.python_node import PythonNode


class GroupedNameAsNames(PythonNode):
    """A group of names to be imported as other names."""
    def __init__(self, name_as_names: NameAsNames, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.name_as_names: NameAsNames = name_as_names

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.name_as_names != other.name_as_names:
            return False

        return True
