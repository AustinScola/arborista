"""Test arborista.nodes.python.dotted_name_as_names."""
from typing import Any, Dict, Iterable, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.dotted_name_as_names.DottedNameAsNames inheritance."""
    assert issubclass(DottedNameAsNames, PythonNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('first_dotted_name_as_name, rest_of_dotted_name_as_names, parent, pass_parent', [
    (DottedNameAsName(DottedName(Name('foo'), [])), [], None, False),
    (DottedNameAsName(DottedName(Name('foo'), [])), [], None, True),
    (DottedNameAsName(DottedName(Name('foo'), [])), [], MagicMock(), True),
    (DottedNameAsName(DottedName(Name('foo'), [])), [DottedNameAsName(DottedName(Name('bar'), [])), DottedNameAsName(DottedName(Name('baz'), []))], None, True),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(first_dotted_name_as_name: DottedNameAsName,
              rest_of_dotted_name_as_names: Iterable[DottedNameAsName], parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.dotted_name_as_names.DottedNameAsNames.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    dotted_name_as_names: DottedNameAsNames = DottedNameAsNames(first_dotted_name_as_name,
                                                                rest_of_dotted_name_as_names,
                                                                **keyword_arguments)

    assert dotted_name_as_names.first_dotted_name_as_name == first_dotted_name_as_name
    assert dotted_name_as_names.rest_of_dotted_name_as_names == rest_of_dotted_name_as_names
    assert dotted_name_as_names.parent == parent
