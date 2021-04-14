"""Test arborista.nodes.nebnf.terminal."""
from typing import Any, Dict, Optional, Union
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.character import Character
from arborista.nodes.nebnf.double_quoted_terminal import DoubleQuotedTerminal
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.single_quoted_terminal import SingleQuotedTerminal
from arborista.nodes.nebnf.terminal import Terminal, TerminalValue


def test_terminal_value() -> None:
    """Test arborista.nodes.nebnf.terminal.TerminalValue."""
    assert isinstance(TerminalValue, type(Union))
    assert TerminalValue.__args__ == (  # type: ignore[attr-defined]
        SingleQuotedTerminal, DoubleQuotedTerminal)


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.terminal.Terminal inheritance."""
    assert issubclass(Terminal, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    (SingleQuotedTerminal(Character('a'), []), None, False),
    (DoubleQuotedTerminal(Character('a'), []), None, False),
    (SingleQuotedTerminal(Character('a'), []), None, True),
    (SingleQuotedTerminal(Character('a'), []), None, False),
    (SingleQuotedTerminal(Character('a'), []), None, True),
    (SingleQuotedTerminal(Character('a'), []), MagicMock(Node), True),
    (SingleQuotedTerminal(Character('a'), []), MagicMock(Node), True),
])
# yapf: enable
def test_init(value: TerminalValue, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.terminal.Terminal.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    terminal: Terminal = Terminal(value, **keyword_arguments)

    assert terminal.value == value
    assert terminal.parent is parent
