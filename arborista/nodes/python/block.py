"""A Python block."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node, NodeIterator
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.statement import StatementList, Statements


class Block(PythonNode):
    """A Python block."""
    def __init__(self, body: Statements, indent: str, parent: Optional[Node] = None):
        super().__init__(parent)

        self.body: StatementList = list(body)
        self.indent: str = indent

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.body == other.body
        return equality

    def iterate_children(self) -> NodeIterator:
        yield from self.body
