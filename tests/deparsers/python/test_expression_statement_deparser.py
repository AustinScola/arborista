"""Test arborista.deparsers.python.expression_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.expression_statement_deparser import ExpressionStatementDeparser
from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String


def test_inheritance() -> None:
    """Test arborista.deparsers.python.expression_statement_deparser.ExpressionStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ExpressionStatementDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('expression_statement, expected_string', [
    (ExpressionStatement(String(None, SingleQuotedShortString('foo'))), "'foo'"),
])
# yapf: enable
def test_deparse_expression_statement(expression_statement: ExpressionStatement,
                                      expected_string: str) -> None:
    """Test arborista.deparsers.python.expression_statement_deparser.ExpressionStatementDeparser.deparse_expression_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ExpressionStatementDeparser.deparse_expression_statement(expression_statement)

    assert string == expected_string
