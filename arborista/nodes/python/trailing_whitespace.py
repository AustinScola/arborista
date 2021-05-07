"""Python trailing whitespace."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.comment import Comment
from arborista.nodes.python.newline import Newline
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.simple_whitespace import SimpleWhitespace


class TrailingWhitespace(PythonNode):
    """Python trailing whitespace."""
    def __init__(self,
                 whitespace: Optional[SimpleWhitespace] = None,
                 comment: Optional[Comment] = None,
                 newline: Optional[Newline] = None,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.whitespace: Optional[SimpleWhitespace] = whitespace
        self.comment: Optional[Comment] = comment
        self.newline: Newline = Newline() if newline is None else newline
