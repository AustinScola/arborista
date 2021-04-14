"""Test arborista.nodes.nebnf.name."""
from typing import Any, Dict, List, Optional, Union
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.digit import Digit
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter
from arborista.nodes.nebnf.name import Name
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.underscore import Underscore


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.name.Name inheritance."""
    assert issubclass(Name, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('first_character, rest_of_characters, parent, pass_parent', [
    (LowercaseLetter('f'), [], None, False),
    (LowercaseLetter('f'), [], MagicMock(), True),
    (LowercaseLetter('f'), [LowercaseLetter('o'), LowercaseLetter('o')], None, False),
    (LowercaseLetter('f'), [LowercaseLetter('o'), LowercaseLetter('o')], MagicMock(), True),
])
# yapf: enable
def test_init(first_character: LowercaseLetter, rest_of_characters: List[Union[LowercaseLetter,
                                                                               Digit, Underscore]],
              parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.name.Name.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    name: Name = Name(first_character, rest_of_characters, **keyword_arguments)

    assert name.first_character == first_character
    assert name.rest_of_characters == rest_of_characters
    assert name.parent is parent
