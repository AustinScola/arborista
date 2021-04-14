"""A terminal."""
from typing import Optional, Union

from arborista.node import Node
from arborista.nodes.nebnf.double_quoted_terminal import DoubleQuotedTerminal
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.single_quoted_terminal import SingleQuotedTerminal

TerminalValue = Union[SingleQuotedTerminal, DoubleQuotedTerminal]


class Terminal(NEBNFNode):
    """A terminal."""
    def __init__(self, value: TerminalValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: TerminalValue = value
