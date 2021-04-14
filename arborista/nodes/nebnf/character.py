"""A character."""
from typing import Optional, Union

from arborista.node import Node
from arborista.nodes.nebnf.digit import DigitValue
from arborista.nodes.nebnf.letter import LetterValue
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.symbol import SymbolValue
from arborista.nodes.nebnf.underscore import UnderscoreValue

CharacterValue = Union[LetterValue, DigitValue, SymbolValue, UnderscoreValue]


class Character(NEBNFNode):
    """A character."""
    def __init__(self, value: CharacterValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: CharacterValue = value
