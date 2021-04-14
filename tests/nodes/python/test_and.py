"""Test arborista.nodes.python.and_."""
from typing import Optional
from unittest.mock import MagicMock

import pytest

from arborista.nodes.python.and_ import And
from arborista.nodes.python.boolean_operator import BooleanOperator
from arborista.nodes.python.expression import Expression


def test_inheritance() -> None:
    """Test arborista.nodes.python.and_.And inheritance."""
    assert issubclass(And, BooleanOperator)


# yapf: disable
@pytest.mark.parametrize('parent, pass_parent', [
    (MagicMock(), MagicMock()),
])
# yapf: enable
def test_init(parent: Optional[Expression], pass_parent: bool) -> None:
    """Test arborista.nodes.python.and_.And.__init__."""
    keyword_arguments = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    and_: And = And(**keyword_arguments)

    assert and_.parent is parent
