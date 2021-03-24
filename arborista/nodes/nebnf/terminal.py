"""A terminal."""
from typing import Any, Optional, Union

from seligimus.python.decorators.operators.equality.equal_type import equal_type

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

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
