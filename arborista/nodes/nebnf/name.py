"""A name for a part of an expression."""
from typing import Any, List, Optional, Union

from seligimus.python.decorators.operators.equality.equal_type import equal_type

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

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.first_character != other.first_character:
            return False

        if self.rest_of_characters != other.rest_of_characters:
            return False

        return True
