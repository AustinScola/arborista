"""A string prefix."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type
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

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value

        return equality
