"""Test arborista.nodes.nebnf.symbol."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest
from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.symbol import Symbol, SymbolValue


def test_symbol_value() -> None:
    """Test arborista.nodes.nebnf.symbol.SymbolValue."""
    assert isinstance(SymbolValue, type(Literal))
    assert SymbolValue.__values__ == (  # type: ignore[attr-defined]
        '[', ']', '{', '}', '(', '}', '<', '>', "'", '"', '=', '|', '.', ';')


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.symbol.Symbol inheritance."""
    assert issubclass(Symbol, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    ('[', None, False),
    ('[', None, True),
    ('[', MagicMock(Node), True),
])
# yapf: enable
def test_init(value: SymbolValue, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.symbol.Symbol.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    symbol: Symbol = Symbol(value, **keyword_arguments)

    assert symbol.value == value
    assert symbol.parent is parent


# yapf: disable
@pytest.mark.parametrize('lowercase_symbol, other, expected_equality', [
    (Symbol('['), 1, False),
    (Symbol('['), '[', False),
    (Symbol('['), Symbol(']'), False),
    (Symbol('['), Symbol('['), True),
])
# yapf: enable
def test_eq(lowercase_symbol: Symbol, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.symbol.Symbol.__eq__."""
    equality: bool = lowercase_symbol == other

    assert equality == expected_equality
