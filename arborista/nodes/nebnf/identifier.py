"""An identifier."""
from typing import List, Optional, Union

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
