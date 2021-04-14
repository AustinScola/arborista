"""Test arborista.nodes.nebnf.identifier."""
from typing import Any, Dict, List, Optional, Union
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.digit import Digit
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.identifier.Identifier inheritance."""
    assert issubclass(Identifier, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('first_character, rest_of_characters, parent, pass_parent', [
    (UppercaseLetter('F'), [], None, False),
    (UppercaseLetter('F'), [], MagicMock(), True),
    (UppercaseLetter('F'), [LowercaseLetter('o'), LowercaseLetter('o')], None, False),
    (UppercaseLetter('F'), [LowercaseLetter('o'), LowercaseLetter('o')], MagicMock(), True),
])
# yapf: enable
def test_init(first_character: UppercaseLetter,
              rest_of_characters: List[Union[LowercaseLetter, UppercaseLetter, Digit]],
              parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.identifier.Identifier.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    identifier: Identifier = Identifier(first_character, rest_of_characters, **keyword_arguments)

    assert identifier.first_character == first_character
    assert identifier.rest_of_characters == rest_of_characters
    assert identifier.parent is parent
