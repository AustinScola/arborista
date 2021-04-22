"""Test arborista.nodes.python.subscripts."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.subscript import Subscript
from arborista.nodes.python.subscripts import Subscripts


def test_inheritance() -> None:
    """Test arborista.nodes.python.subscripts.Subscripts inheritance."""
    assert issubclass(Subscripts, PythonNode)


# yapf: disable
@pytest.mark.parametrize('first, rest, parent, pass_parent', [
    (Index(Integer(1)), [], None, False),
    (Index(Integer(1)), [], None, True),
    (Index(Integer(1)), [], MagicMock(), True),
    (Index(Integer(1)), [Index(Integer(2))], MagicMock(), True),
])
# yapf: enable
def test_init(first: Subscript, rest: List[Subscript], parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.subscripts.Subscripts.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    subscripts: Subscripts = Subscripts(first, rest, **keyword_arguments)

    assert subscripts.first == first
    assert subscripts.rest == rest
    assert subscripts.parent is parent
