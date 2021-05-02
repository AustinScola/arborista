"""Test arborista.deparsers.python.expression_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.expression_deparser import ExpressionDeparser
from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.equals import Equals
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_call import FunctionCall
from arborista.nodes.python.name import Name
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String


def test_inheritance() -> None:
    """Test arborista.deparsers.python.expression_deparser.ExpressionDeparser inheritance."""
    assert issubclass(ExpressionDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('expression, expected_string', [
    (String(None, SingleQuotedShortString('foo')), "'foo'"),
    (Name('foo'), 'foo'),
    (Comparison(Name('foo'), Equals(), Name('bar')), 'foo == bar'),
    (FunctionCall(Name('foo'), None), 'foo()'),
])
# yapf: enable
def test_deparse_expression(expression: Expression, expected_string: str) -> None:
    """Test arborista.deparsers.python.expression_deparser.ExpressionDeparser.deparse_expression."""
    string: str = ExpressionDeparser.deparse_expression(expression)

    assert string == expected_string
