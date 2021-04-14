"""A name for a part of an expression."""
from typing import List, Optional, Union

from arborista.node import Node
from arborista.nodes.nebnf.digit import Digit
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.underscore import Underscore


class Name(NEBNFNode):
    """A name for a part of an expression."""
    def __init__(self,
                 first_character: LowercaseLetter,
                 rest_of_characters: List[Union[LowercaseLetter, Digit, Underscore]],
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.first_character: LowercaseLetter = first_character
        self.rest_of_characters: List[Union[LowercaseLetter, Digit,
                                            Underscore]] = rest_of_characters
