"""A Python import dotted name statement."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.import_statement import ImportStatement


class ImportDottedName(ImportStatement):
    """A Python import dotted name statement."""
    def __init__(self, dotted_name_as_names: DottedNameAsNames, parent: Optional[Node] = None):
        super().__init__(parent)

        self.dotted_name_as_names: DottedNameAsNames = dotted_name_as_names

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.dotted_name_as_names != other.dotted_name_as_names:
            return False

        return True
