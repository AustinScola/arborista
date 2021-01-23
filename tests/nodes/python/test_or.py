"""Test arborista.nodes.python.or_."""
from typing import Any, Optional
from unittest.mock import MagicMock

import pytest

from arborista.nodes.python.boolean_operator import BooleanOperator
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.or_ import Or


def test_inheritance() -> None:
    """Test arborista.nodes.python.or_.Or inheritance."""
    assert issubclass(Or, BooleanOperator)


# yapf: disable
@pytest.mark.parametrize('parent, pass_parent', [
    (MagicMock(), MagicMock()),
])
# yapf: enable
def test_init(parent: Optional[Expression], pass_parent: bool) -> None:
    """Test arborista.nodes.python.or_.Or.__init__."""
    keyword_arguments = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    or_: Or = Or(**keyword_arguments)

    assert or_.parent is parent


# yapf: disable
@pytest.mark.parametrize('or_, other, expected_equality', [
    (Or(), 'foo', False),
    (Or(), Or(), True),
])
# yapf: enable
def test_eq(or_: Or, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.or_.Or.__eq__."""
    equality: bool = or_ == other

    assert equality == expected_equality
