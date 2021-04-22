"""Test arborista.nodes.python.slice."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.slice import Slice
from arborista.nodes.python.subscript import Subscript


def test_inheritance() -> None:
    """Test arborista.nodes.python.slice.Slice inheritance."""
    assert issubclass(Slice, Subscript)


# yapf: disable
@pytest.mark.parametrize('start, end, step, parent, pass_parent', [
    (None, None, None, None, False),
    (None, None, None, None, True),
    (Integer(1), Integer(2), Integer(3), MagicMock(), True),
])
# yapf: enable
def test_init(start: Optional[Expression], end: Optional[Expression], step: Optional[Expression],
              parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.slice."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    slice_: Slice = Slice(start, end, step, **keyword_arguments)

    assert slice_.start == start
    assert slice_.end == end
    assert slice_.step == step
    assert slice_.parent is parent
