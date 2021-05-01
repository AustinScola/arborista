"""Test arborista.deparsers.python.comparison_operator_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.comparison_operator_deparser import ComparisonOperatorDeparser
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.equals import Equals
from arborista.nodes.python.greater_than import GreaterThan
from arborista.nodes.python.greater_than_or_equals import GreaterThanOrEquals
from arborista.nodes.python.in_ import In
from arborista.nodes.python.is_ import Is
from arborista.nodes.python.is_not import IsNot
from arborista.nodes.python.less_greater_than import LessGreaterThan
from arborista.nodes.python.less_than import LessThan
from arborista.nodes.python.less_than_or_equals import LessThanOrEquals
from arborista.nodes.python.not_equals import NotEquals
from arborista.nodes.python.not_in import NotIn


def test_inheritance() -> None:
    """Test arborista.deparsers.python.comparison_operator_deparser.ComparisonOperatorDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ComparisonOperatorDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('comparison_operator, expected_string', [
    (LessThan(), '<'),
    (GreaterThan(), '>'),
    (Equals(), '=='),
    (GreaterThanOrEquals(), '>='),
    (LessThanOrEquals(), '<='),
    (LessGreaterThan(), '<>'),
    (NotEquals(), '!='),
    (In(), 'in'),
    (NotIn(), 'not in'),
    (Is(), 'is'),
    (IsNot(), 'is not'),
])
# yapf: enable
def test_deparse_comparison_operator(comparison_operator: ComparisonOperator,
                                     expected_string: str) -> None:
    """Test arborista.deparsers.python.comparison_operator_deparser.ComparisonOperatorDeparser.deparse_comparison_operator."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ComparisonOperatorDeparser.deparse_comparison_operator(comparison_operator)

    assert string == expected_string
