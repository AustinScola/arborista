"""A Python class definition."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.suite import Suite


class ClassDefinition(CompoundStatement):
    """A Python class definition."""
    def __init__(self,
                 name: Name,
                 bases: Optional[Arguments],
                 body: Suite,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name
        self.bases: Optional[Arguments] = bases
        self.body: Suite = body
