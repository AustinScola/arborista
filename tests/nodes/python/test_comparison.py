"""Test arborista.nodes.python.comparison."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.less_than import LessThan


def test_inheritance() -> None:
    """Test arborista.nodes.python.comparison.Comparison inheritance."""
    assert issubclass(Comparison, Expression)


# yapf: disable
@pytest.mark.parametrize('left, comparison_operator, right, parent, pass_parent', [
    (Integer(1), LessThan(), Integer(2), None, False),
    (Integer(1), LessThan(), Integer(2), None, True),
    (Integer(1), LessThan(), Integer(2), MagicMock(), True),
])
# yapf: enable
def test_init(left: Expression, comparison_operator: ComparisonOperator, right: Expression,
              parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.comparison.Comparison.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    comparison = Comparison(left, comparison_operator, right, **keyword_arguments)

    assert comparison.left == left
    assert comparison.comparison_operator == comparison_operator
    assert comparison.right == right
    assert comparison.parent is parent
