"""Test arborista.parsers.python.small_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.small_statement import SmallStatement, SmallStatementList
from arborista.parser import Parser
from arborista.parsers.python.small_statement_parser import (LibcstSmallStatement,
                                                             LibcstSmallStatements,
                                                             SmallStatementParser)


def test_inheritance() -> None:
    """Test arborista.parsers.python.small_statement_parser.SmallStatementParser inheritance."""
    assert issubclass(SmallStatementParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_small_statement, expected_small_statement', [
    (libcst.Return(), ReturnStatement()),
])
# yapf: enable
def test_parse_small_statement(libcst_small_statement: LibcstSmallStatement,
                               expected_small_statement: SmallStatement) -> None:
    """Test arborista.parsers.python.small_statement_parser.SmallStatementParser.parse_small_statement."""  # pylint: disable=line-too-long, useless-suppression
    small_statement: SmallStatement = SmallStatementParser.parse_small_statement(
        libcst_small_statement)
    assert small_statement == expected_small_statement


# yapf: disable
@pytest.mark.parametrize('libcst_small_statements, expected_small_statements', [
    ([libcst.Return()], [ReturnStatement()]),
])
# yapf: enable
def test_parse_small_statements(libcst_small_statements: LibcstSmallStatements,
                                expected_small_statements: SmallStatementList) -> None:
    """Test arborista.parsers.python.small_statement_parser.SmallStatementParser.parse_small_statements."""  # pylint: disable=line-too-long, useless-suppression
    small_statements: SmallStatementList = SmallStatementParser.parse_small_statements(
        libcst_small_statements)
    assert small_statements == expected_small_statements
