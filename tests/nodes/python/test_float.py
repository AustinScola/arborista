"""Test arborista.nodes.python.float."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.nodes.python.float import Float
from arborista.nodes.python.number import Number
from testing_helpers.animal_nodes import Dog


def test_inheritance() -> None:
    """Test arborista.nodes.python.float.Float inheritance."""
    assert issubclass(Float, Number)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    (0.0, None, False),
    (0.0, None, True),
    (0.0, Dog(), True),
])
# yapf: enable
def test_init(value: int, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.float.Float.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    float_ = Float(value, **keyword_arguments)

    assert float_.value == value
    assert float_.parent is parent
