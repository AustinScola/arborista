"""A uppercase letter."""
from typing import Optional

from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

UppercaseLetterValue = Literal['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class UppercaseLetter(NEBNFNode):
    """A uppercase letter."""
    def __init__(self, value: UppercaseLetterValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: UppercaseLetterValue = value
