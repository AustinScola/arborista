"""A lowercase letter."""
from typing import Optional

from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

LowercaseLetterValue = Literal['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class LowercaseLetter(NEBNFNode):
    """A lowercase letter."""
    def __init__(self, value: LowercaseLetterValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: LowercaseLetterValue = value
