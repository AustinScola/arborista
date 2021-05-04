"""Test arborista.deparsers.python.expression_list_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.expression_list_deparser import ExpressionListDeparser
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.expression_list_deparser.ExpressionListDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ExpressionListDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('expression_list, expected_string', [
    (ExpressionList(Name('foo'), []), 'foo'),
    (ExpressionList(Name('foo'), [Name('bar')]), 'foo, bar'),
    (ExpressionList(Name('foo'), [Name('bar'), Name('baz'),]), 'foo, bar, baz'),
])
# yapf: enable
def test_deparse_expression_list(expression_list: ExpressionList, expected_string: str) -> None:
    """Test arborista.deparsers.python.expression_list_deparser.ExpressionListDeparser.deparse_expression_list."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ExpressionListDeparser.deparse_expression_list(expression_list)

    assert string == expected_string
