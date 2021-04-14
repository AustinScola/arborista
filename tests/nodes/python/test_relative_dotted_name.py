"""Test arborista.nodes.python.relative_dotted_name."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.relative_dotted_name import RelativeDottedName


def test_inheritance() -> None:
    """Test arborista.nodes.python.relative_dotted_name.RelativeDottedName inheritance."""
    assert issubclass(RelativeDottedName, PythonNode)


# yapf: disable
@pytest.mark.parametrize('dots, dotted_name, parent, pass_parent', [
    (1, None, None, False),
    (1, DottedName(Name('foo'), []), None, False),
    (1, DottedName(Name('foo'), []), None, True),
    (1, DottedName(Name('foo'), []), MagicMock(), True),
])
# yapf: enable
def test_init(dots: int, dotted_name: Optional[DottedName], parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.relative_dotted_name.RelativeDottedName.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    relative_dotted_name: RelativeDottedName = RelativeDottedName(dots, dotted_name,
                                                                  **keyword_arguments)

    assert relative_dotted_name.dots == dots
    assert relative_dotted_name.dotted_name == dotted_name
    assert relative_dotted_name.parent is parent
