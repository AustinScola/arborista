"""A digit."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type
from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

DigitValue = Literal['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class Digit(NEBNFNode):
    """A digit."""
    def __init__(self, value: DigitValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: DigitValue = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
