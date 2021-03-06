"""A character."""
from typing import Any, Optional, Union

from seligimus.python.decorators.operators.equality.equal_type import equal_type

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

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
