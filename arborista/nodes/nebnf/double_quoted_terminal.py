"""A double quoted terminal."""
from typing import Any, List, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.character import Character
from arborista.nodes.nebnf.nebnf_node import NEBNFNode


class DoubleQuotedTerminal(NEBNFNode):
    """A double quoted terminal."""
    def __init__(self,
                 first_character: Character,
                 rest_of_characters: List[Character],
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.first_character: Character = first_character
        self.rest_of_characters: List[Character] = rest_of_characters

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.first_character != other.first_character:
            return False

        if self.rest_of_characters != other.rest_of_characters:
            return False

        return True
