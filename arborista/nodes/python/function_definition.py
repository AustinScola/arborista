"""A Python function defintion."""
from typing import Optional

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

    def iterate_children(self) -> NodeIterator:
        yield self.name
        yield from self.parameters
        yield self.body
