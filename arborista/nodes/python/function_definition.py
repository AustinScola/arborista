"""A Python function defintion."""
from typing import Any, Optional

from arborista.decorators.equality.equal_type import equal_type
from arborista.node import Node, NodeIterator
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import ParameterList, Parameters
from arborista.nodes.python.suite import Suite


class FunctionDefinition(CompoundStatement):
    """A Python function defintion."""
    def __init__(self,
                 name: Name,
                 parameters: Parameters,
                 body: Suite,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name
        self.parameters: ParameterList = list(parameters)
        self.body: Suite = body

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.name != other.name:
            return False

        if self.parameters != other.parameters:
            return False

        if self.body != other.body:
            return False

        return True

    def iterate_children(self) -> NodeIterator:
        yield self.name
        yield from self.parameters
        yield self.body
