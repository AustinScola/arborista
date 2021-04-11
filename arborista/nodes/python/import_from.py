"""A python import from statement."""
from typing import Any, Optional, Union

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.grouped_name_as_names import GroupedNameAsNames
from arborista.nodes.python.import_statement import ImportStatement
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.relative_dotted_name import RelativeDottedName
from arborista.nodes.python.star import Star

Source = Union[DottedName, RelativeDottedName]
Target = Union[Star, GroupedNameAsNames, NameAsNames]


class ImportFrom(ImportStatement):
    """A python import from statement."""
    def __init__(self, source: Source, target: Target, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.source: Source = source
        self.target: Target = target

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.source != other.source:
            return False

        if self.target != other.target:
            return False

        return True
