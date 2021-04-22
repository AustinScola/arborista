"""Test arborista.nodes.python.index."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.subscript import Subscript


def test_inheritance() -> None:
    """Test arborista.nodes.python.index.Index inheritance."""
    assert issubclass(Index, Subscript)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    (Integer(5), None, False),
    (Integer(5), None, True),
    (Integer(5), MagicMock(), True),
])
# yapf: enable
def test_init(value: Expression, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.index.Index.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    index: Index = Index(value, **keyword_arguments)

    assert index.value == value
    assert index.parent is parent
