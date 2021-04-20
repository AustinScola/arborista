"""Test arborista.parsers.python.comparison_operator_parser."""
import libcst
import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.equals import Equals
from arborista.parser import Parser
from arborista.parsers.python.comparison_operator_parser import (ComparisonOperatorParser,
                                                                 LibcstComparisonOperator)


def test_libcst_comparison_operator() -> None:
    """Test arborista.parsers.python.comparison_operator_parser.LibcstComparisonOperator"""
    assert LibcstComparisonOperator == libcst.BaseCompOp


def test_inheritance() -> None:
    """Test arborista.parsers.python.comparison_operator_parser.ComparisonOperatorParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ComparisonOperatorParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_comparison_operator, expected_comparison_operator', [
    (libcst.Equal(), Equals()),
])
# yapf: enable
def test_parse_comparison_operator(libcst_comparison_operator: LibcstComparisonOperator,
                                   expected_comparison_operator: ComparisonOperator) -> None:
    """Test arborista.parsers.python.comparison_operator_parser.ComparisonOperatorParser.parse_comparison_operator."""  # pylint: disable=line-too-long, useless-suppression
    comparison_operator: ComparisonOperator = ComparisonOperatorParser.parse_comparison_operator(
        libcst_comparison_operator)

    assert comparison_operator == expected_comparison_operator
