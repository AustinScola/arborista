"""Test arborista.parsers.python.expression_parser."""
import libcst
import pytest

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression


def test_libcst_expression() -> None:
    """Test arborista.parsers.python.expression_parser.LibcstExpression."""
    assert LibcstExpression == libcst.BaseExpression


def test_inheritance() -> None:
    """Test arborista.parsers.python.expression_parser.ExpressionParser inheritance."""
    assert issubclass(ExpressionParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_expression, expected_expression', [
    (libcst.Integer('1'), Integer(1)),
    (libcst.SimpleString("'foo'"), String(None, SingleQuotedShortString('foo'))),
])
# yapf: enable
def test_parse_expression(libcst_expression: LibcstExpression,
                          expected_expression: Expression) -> None:
    """Test arborista.parsers.python.expression_parser.ExpressionParser.parse_expression."""
    expression: Expression = ExpressionParser.parse_expression(libcst_expression)

    assert expression == expected_expression
