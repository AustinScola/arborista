"""Test arborista.deparsers.python.small_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.small_statement_deparser import SmallStatementDeparser
from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.small_statement import SmallStatement
from arborista.nodes.python.string import String


def test_inheritance() -> None:
    """Test arborista.deparsers.python.small_statement_deparser.SmallStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(SmallStatementDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('small_statement, expected_string', [
    (ExpressionStatement(String(None, SingleQuotedShortString('foo'))), "'foo'"),
    (ReturnStatement(), 'return'),
    (PassStatement(), 'pass'),
])
# yapf: enable
def test_deparser_small_statement(small_statement: SmallStatement, expected_string: str) -> None:
    """Test arborista.deparsers.python.small_statement_deparser.SmallStatementDeparser.deparse_small_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = SmallStatementDeparser.deparse_small_statement(small_statement)

    assert string == expected_string
