"""Test arborista.nodes.nebnf.double_quoted_terminal."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.character import Character
from arborista.nodes.nebnf.double_quoted_terminal import DoubleQuotedTerminal
from arborista.nodes.nebnf.nebnf_node import NEBNFNode


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.double_quoted_terminal.DoubleQuotedTerminal inheritance."""
    assert issubclass(DoubleQuotedTerminal, NEBNFNode)


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
    """Test arborista.nodes.nebnf.double_quoted_terminal.DoubleQuotedTerminal.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    double_quoted_terminal: DoubleQuotedTerminal = DoubleQuotedTerminal(
        first_character, rest_of_characters, **keyword_arguments)

    assert double_quoted_terminal.first_character == first_character
    assert double_quoted_terminal.rest_of_characters == rest_of_characters
    assert double_quoted_terminal.parent is parent
