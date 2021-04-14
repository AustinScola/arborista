"""A string prefix."""
from typing import Optional

from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.python.python_node import PythonNode

StringPrefixValue = Literal['f', 'r', 'u', 'F', 'R', 'U', 'fr', 'Fr', 'fR', 'FR', 'rf', 'Rf', 'rF',
                            'RF']


class StringPrefix(PythonNode):
    """A string prefix."""
    def __init__(self, value: StringPrefixValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: StringPrefixValue = value
