"""Test arborista.nodes.nebnf.single_quoted_terminal."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.character import Character
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.single_quoted_terminal import SingleQuotedTerminal


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.single_quoted_terminal.SingleQuotedTerminal inheritance."""
    assert issubclass(SingleQuotedTerminal, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('first_character, rest_of_characters, parent, pass_parent', [
    (Character('f'), [], None, False),
    (Character('f'), [], MagicMock(), True),
    (Character('f'), [Character('o'), Character('o')], None, False),
    (Character('f'), [Character('o'), Character('o')], MagicMock(), True),
])
# yapf: enable
def test_init(first_character: Character, rest_of_characters: List[Character],
              parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.single_quoted_terminal.SingleQuotedTerminal.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    single_quoted_terminal: SingleQuotedTerminal = SingleQuotedTerminal(
        first_character, rest_of_characters, **keyword_arguments)

    assert single_quoted_terminal.first_character == first_character
    assert single_quoted_terminal.rest_of_characters == rest_of_characters
    assert single_quoted_terminal.parent is parent
