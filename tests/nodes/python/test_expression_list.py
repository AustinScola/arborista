"""Test arborista.nodes.python.expression_list."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.expression_list.ExpressionList inheritance."""
    assert issubclass(ExpressionList, PythonNode)


# yapf: disable
@pytest.mark.parametrize('first, rest, parent, pass_parent', [
    (Name('foo'), [], None, False),
    (Name('foo'), [], None, True),
    (Name('foo'), [], MagicMock, True),
    (Name('foo'), [Name('bar')], MagicMock, True),
    (Name('foo'), [Name('bar'), Name('baz')], MagicMock, True),
])
# yapf: enable
def test_init(first: Expression, rest: List[Expression], parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.expression_list.ExpressionList.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    expression_list: ExpressionList = ExpressionList(first, rest, **keyword_arguments)

    assert expression_list.first == first
    assert expression_list.rest == rest
    assert expression_list.parent is parent
