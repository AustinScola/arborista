"""A Python function defintion."""
from typing import Optional

from arborista.node import Node, NodeIterator
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.decorator import DecoratorList, Decorators
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.suite import Suite


class FunctionDefinition(CompoundStatement):
    """A Python function defintion."""

    # pylint: disable=too-many-arguments
    def __init__(self,
                 name: Name,
                 parameters: Parameters,
                 body: Suite,
                 decorators: Optional[Decorators] = None,
                 returns: Optional[Expression] = None,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name
        self.parameters: Parameters = parameters
        self.body: Suite = body
        self.decorators: DecoratorList = [] if decorators is None else list(decorators)
        self.returns: Optional[Expression] = returns

    def iterate_children(self) -> NodeIterator:
        yield self.name
        yield self.parameters
        yield self.body
        yield from self.decorators
        if self.returns is not None:
            yield self.returns
