"""An identifier."""
from typing import Any, List, Optional, Union

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.digit import Digit
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


class Identifier(NEBNFNode):
    """An identifier."""
    def __init__(self,
                 first_character: UppercaseLetter,
                 rest_of_characters: List[Union[LowercaseLetter, UppercaseLetter, Digit]],
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.first_character: UppercaseLetter = first_character
        self.rest_of_characters: List[Union[LowercaseLetter, UppercaseLetter,
                                            Digit]] = rest_of_characters

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.first_character != other.first_character:
            return False

        if self.rest_of_characters != other.rest_of_characters:
            return False

        return True
