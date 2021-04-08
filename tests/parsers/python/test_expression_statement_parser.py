"""Test arborista.parsers.python.expression_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.nodes.python.integer import Integer
from arborista.parser import Parser
from arborista.parsers.python.expression_statement_parser import (ExpressionStatementParser,
                                                                  LibcstExpressionStatement)


def test_libcst_expression_statement() -> None:
    """Test arborista.parsers.python.expression_statement_parser.LibcstExpressionStatement."""
    assert LibcstExpressionStatement == libcst.Expr


def test_inheritance() -> None:
    """Test arborista.parsers.python.expression_statement_parser.ExpressionStatementParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ExpressionStatementParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_expression_statement, expected_expression_statement', [
    (libcst.Expr(libcst.Integer('1')), ExpressionStatement(Integer(1))),
])
# yapf: enable
def test_parse_expression_statement(libcst_expression_statement: LibcstExpressionStatement,
                                    expected_expression_statement: ExpressionStatement) -> None:
    """Test arborista.parsers.python.expression_statement_parser.ExpressionStatementParser.parse_expression_statement."""  # pylint: disable=line-too-long
    expression_statement: ExpressionStatement = ExpressionStatementParser.parse_expression_statement(
        libcst_expression_statement)

    assert expression_statement == expected_expression_statement
