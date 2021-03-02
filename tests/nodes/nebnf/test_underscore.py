"""Test arborista.nodes.nebnf.underscore."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest
from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.underscore import Underscore, UnderscoreValue


def test_underscore_value() -> None:
    """Test arborista.nodes.nebnf.underscore.UnderscoreValue."""
    assert isinstance(UnderscoreValue, type(Literal))
    assert UnderscoreValue.__values__ == ('_', )  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.underscore.Underscore inheritance."""
    assert issubclass(Underscore, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('parent, pass_parent', [
    (None, False),
    (None, True),
    (MagicMock(Node), True),
    (MagicMock(Node), True),
])
# yapf: enable
def test_init(parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.underscore.Underscore.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    underscore: Underscore = Underscore(**keyword_arguments)

    assert underscore.value == '_'
    assert underscore.parent is parent


# yapf: disable
@pytest.mark.parametrize('underscore, other, expected_equality', [
    (Underscore(), 1, False),
    (Underscore(), '_', False),
    (Underscore(), Underscore(), True),
])
# yapf: enable
def test_eq(underscore: Underscore, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.underscore.Underscore.__eq__."""
    equality: bool = underscore == other

    assert equality == expected_equality
