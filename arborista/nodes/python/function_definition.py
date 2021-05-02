"""A Python function defintion."""
from typing import Optional

from arborista.node import Node, NodeIterator
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import ParameterList, Parameters
from arborista.nodes.python.suite import Suite


class FunctionDefinition(CompoundStatement):
    """A Python function defintion."""

    # pylint: disable=too-many-arguments
    def __init__(self,
                 name: Name,
                 parameters: Parameters,
                 body: Suite,
                 returns: Optional[Expression] = None,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name
        self.parameters: ParameterList = list(parameters)
        self.body: Suite = body
        self.returns: Optional[Expression] = returns

    def iterate_children(self) -> NodeIterator:
        yield self.name
        yield from self.parameters
        yield self.body
        if self.returns is not None:
            yield self.returns
