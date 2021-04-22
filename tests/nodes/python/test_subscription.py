"""Test arborista.nodes.python.subscription."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.name import Name
from arborista.nodes.python.subscription import Subscription
from arborista.nodes.python.subscripts import Subscripts


def test_inheritance() -> None:
    """Test arborista.nodes.python.subscription.Subscription inheritance."""
    assert issubclass(Subscription, Expression)


# yapf: disable
@pytest.mark.parametrize('value, subscripts, parent, pass_parent', [
    (Name('foo'), Subscripts(Index(Integer(1)), []), None, False),
    (Name('foo'), Subscripts(Index(Integer(1)), []), None, True),
    (Name('foo'), Subscripts(Index(Integer(1)), []), MagicMock(), True),
])
# yapf: enable
def test_init(value: Expression, subscripts: Subscripts, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.subscription.Subscription.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    subscription: Subscription = Subscription(value, subscripts, **keyword_arguments)

    assert subscription.value == value
    assert subscription.subscripts == subscripts
    assert subscription.parent is parent
