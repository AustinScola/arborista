"""Test arborista.deparsers.python.simple_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.simple_statement_deparser import SimpleStatementDeparser
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.simple_statement_deparser.SimpleStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(SimpleStatementDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('simple_statement, indent, expected_string', [
    (SimpleStatement([ReturnStatement()]), '', 'return\n'),
    (SimpleStatement([ReturnStatement()]), '    ', '    return\n'),
    (SimpleStatement([ReturnStatement()]), '\t', '\treturn\n'),
    (SimpleStatement([ReturnStatement(), ReturnStatement()]), '',  'return; return\n'),
    (SimpleStatement([ReturnStatement(), ReturnStatement()]), '    ', '    return; return\n'),
    (SimpleStatement([ReturnStatement(), ReturnStatement()]), '\t',  '\treturn; return\n'),
    (SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()]), '', 'return; return; return\n'),
    (SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()]), '    ', '    return; return; return\n'),
    (SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()]), '\t', '\treturn; return; return\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_simple_statement(simple_statement: SimpleStatement, indent: str,
                                  expected_string: str) -> None:
    """Test arborista.deparsers.python.simple_statement_deparser.SimpleStatementDeparser.deparse_simple_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = SimpleStatementDeparser.deparse_simple_statement(simple_statement, indent)
    assert string == expected_string
