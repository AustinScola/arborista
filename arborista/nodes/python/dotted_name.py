"""A Python dotted name."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.name import Name, Names


class DottedName(Atom):
    """A Python dotted name."""
    def __init__(self, first_name: Name, rest_of_names: Names, parent: Optional[Node] = None):
        super().__init__(parent)

        self.first_name: Name = first_name
        self.rest_of_names: Names = rest_of_names
