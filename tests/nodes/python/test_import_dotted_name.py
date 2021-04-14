"""Test arborista.nodes.python.import_dotted_name."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.import_dotted_name import ImportDottedName
from arborista.nodes.python.import_statement import ImportStatement
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.nodes.python.import_dotted_name.ImportDottedName inheritance."""
    assert issubclass(ImportDottedName, ImportStatement)


# yapf: disable
@pytest.mark.parametrize('dotted_name_as_names, parent, pass_parent', [
    (DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), [])), []), None, False),
    (DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), [])), []), None, True),
    (DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), [])), []), MagicMock, True),
])
# yapf: enable
def test_init(dotted_name_as_names: DottedNameAsNames, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.import_dotted_name.ImportDottedName.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    import_dotted_name: ImportDottedName = ImportDottedName(dotted_name_as_names,
                                                            **keyword_arguments)

    assert import_dotted_name.dotted_name_as_names == dotted_name_as_names
    assert import_dotted_name.parent is parent
