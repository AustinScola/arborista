"""Test arborista.parsers.python.expression_parser."""
import libcst
import pytest

from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.equals import Equals
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_call import FunctionCall
from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.name import Name
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String
from arborista.nodes.python.subscription import Subscription
from arborista.nodes.python.subscripts import Subscripts
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression


def test_libcst_expression() -> None:
    """Test arborista.parsers.python.expression_parser.LibcstExpression."""
    assert LibcstExpression == libcst.BaseExpression


def test_inheritance() -> None:
    """Test arborista.parsers.python.expression_parser.ExpressionParser inheritance."""
    assert issubclass(ExpressionParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_expression, expected_expression', [
    (libcst.Name('foo'), Name('foo')),
    (libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')), DottedName(Name('foo'), [Name('bar')])),
    (libcst.Integer('1'), Integer(1)),
    (libcst.SimpleString("'foo'"), String(None, SingleQuotedShortString('foo'))),
    (libcst.Comparison(libcst.Integer('1'), [libcst.ComparisonTarget(libcst.Equal(), libcst.Integer('2'))]), Comparison(Integer(1), Equals(), Integer(2))),
    (libcst.Call(libcst.Name('foo')), FunctionCall(Name('foo'), None)),
    (libcst.Subscript(libcst.Name('foo'), [libcst.SubscriptElement(libcst.Index(libcst.Integer('0')))]), Subscription(Name('foo'), Subscripts(Index(Integer(0)), []))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_expression(libcst_expression: LibcstExpression,
                          expected_expression: Expression) -> None:
    """Test arborista.parsers.python.expression_parser.ExpressionParser.parse_expression."""
    expression: Expression = ExpressionParser.parse_expression(libcst_expression)

    assert expression == expected_expression
