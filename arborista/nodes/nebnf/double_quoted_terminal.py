"""A double quoted terminal."""
from typing import List, Optional

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
