"""A Python import dotted name statement."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.import_statement import ImportStatement


class ImportDottedName(ImportStatement):
    """A Python import dotted name statement."""
    def __init__(self, dotted_name_as_names: DottedNameAsNames, parent: Optional[Node] = None):
        super().__init__(parent)

        self.dotted_name_as_names: DottedNameAsNames = dotted_name_as_names
