"""Test arborista.parsers.python.statement_parser."""
import libcst
import pytest

from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.statement import Statement, StatementList
from arborista.parser import Parser
from arborista.parsers.python.statement_parser import (LibcstStatement, LibcstStatements,
                                                       StatementParser)


def test_inheritance() -> None:
    """Test arborista.parsers.python.statement_parser.StatementParser inheritance."""
    assert issubclass(StatementParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_statement, expected_statement', [
    (libcst.SimpleStatementLine(body=[libcst.Return()]), SimpleStatement(small_statements=[ReturnStatement()])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_statement(libcst_statement: LibcstStatement, expected_statement: Statement) -> None:
    """Test arborista.parsers.python.statement_parser.StatementParser.parse_statements."""
    statement: Statement = StatementParser.parse_statement(libcst_statement)
    assert statement == expected_statement


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_statements, expected_statements', [
    ([libcst.SimpleStatementLine(body=[libcst.Return()])], [SimpleStatement(small_statements=[ReturnStatement()])]),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_statements(libcst_statements: LibcstStatements,
                          expected_statements: StatementList) -> None:
    """Test arborista.parsers.python.statement_parser.StatementParser.parse_statements."""
    statements: StatementList = StatementParser.parse_statements(libcst_statements)
    assert statements == expected_statements
