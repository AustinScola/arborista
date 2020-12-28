"""Test arborista.deparsers.python.pass_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.pass_statement_deparser import PassStatementDeparser
from arborista.nodes.python.pass_statement import PassStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.pass_statement_deparser.PassStatementDeparser inheritance."""
    assert issubclass(PassStatementDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('pass_statement, expected_string', [
    (PassStatement(), 'pass'),
])
# yapf: enable
def test_deparse_pass_statement(pass_statement: PassStatement, expected_string: str) -> None:
    """Test arborista.deparsers.python.pass_statement_deparser.PassStatementDeparser.deparse_pass_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = PassStatementDeparser.deparse_pass_statement(pass_statement)

    assert string == expected_string
