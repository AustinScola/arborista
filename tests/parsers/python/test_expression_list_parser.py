"""Test arborista.parsers.python.expression_list_parser."""
from typing import Sequence

import libcst
import pytest

from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.integer import Integer
from arborista.parser import Parser
from arborista.parsers.python.expression_list_parser import (ExpressionListParser,
                                                             LibcstExpressionList)
from arborista.parsers.python.expression_parser import LibcstExpression


def test_libcst_expression_list() -> None:
    """Test arborista.parsers.python.expression_list_parser.LibcstExpressionList."""
    assert isinstance(LibcstExpressionList, type(Sequence))
    assert LibcstExpressionList.__args__ == (LibcstExpression, )  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.parsers.python.expression_list_parser.ExpressionListParser inheritance."""
    assert issubclass(ExpressionListParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_expression_list, expected_expression_list', [
    ([libcst.Integer('5')], ExpressionList(Integer(5), [])),
    ([libcst.Integer('5'), libcst.Integer('7')], ExpressionList(Integer(5), [Integer(7)])),
])
# yapf: enable
def test_parse_expression_list(libcst_expression_list: LibcstExpressionList,
                               expected_expression_list: ExpressionList) -> None:
    """Test arborista.parsers.python.expression_list_parser.ExpressionListParser.parse_expression_list."""  # pylint: disable=line-too-long, useless-suppression
    expression_list: ExpressionList = ExpressionListParser.parse_expression_list(
        libcst_expression_list)

    assert expression_list == expected_expression_list
