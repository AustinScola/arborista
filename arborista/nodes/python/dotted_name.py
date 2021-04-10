"""A Python dotted name."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.import_statement import ImportStatement
from arborista.nodes.python.name import Name, Names


class DottedName(ImportStatement):
    """A Python import dotted name."""
    def __init__(self, first_name: Name, rest_of_names: Names, parent: Optional[Node] = None):
        super().__init__(parent)

        self.first_name: Name = first_name
        self.rest_of_names: Names = rest_of_names

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.first_name != other.first_name:
            return False

        if self.rest_of_names != other.rest_of_names:
            return False

        return True
