"""A letter."""
from typing import Optional, Union

from arborista.node import Node
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetterValue
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetterValue

LetterValue = Union[LowercaseLetterValue, UppercaseLetterValue]


class Letter(NEBNFNode):
    """A letter."""
    def __init__(self, value: LetterValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: LetterValue = value
