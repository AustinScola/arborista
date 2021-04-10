"""A Python dotted names as other names."""
from typing import Any, Iterable, List, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.python_node import PythonNode


class DottedNameAsNames(PythonNode):
    """A Python dotted names as other names."""
    def __init__(self,
                 first_dotted_name_as_name: DottedNameAsName,
                 rest_of_dotted_name_as_names: Iterable[DottedNameAsName],
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.first_dotted_name_as_name: DottedNameAsName = first_dotted_name_as_name
        self.rest_of_dotted_name_as_names: List[DottedNameAsName] = list(
            rest_of_dotted_name_as_names)

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.first_dotted_name_as_name != other.first_dotted_name_as_name:
            return False

        if self.rest_of_dotted_name_as_names != other.rest_of_dotted_name_as_names:
            return False

        return True
