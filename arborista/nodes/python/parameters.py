"""Python parameters."""
from typing import Optional

from arborista.node import Node, NodeIterator
from arborista.nodes.python.positional_parameter import (PositionalParameterList,
                                                         PositionalParameters)
from arborista.nodes.python.python_node import PythonNode


class Parameters(PythonNode):
    """Python parameters."""
    def __init__(self,
                 positional: Optional[PositionalParameters] = None,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.positional: PositionalParameterList = [] if positional is None else list(positional)

    def iterate_children(self) -> NodeIterator:
        yield from self.positional
