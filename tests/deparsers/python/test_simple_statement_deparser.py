"""Test arborista.deparsers.python.simple_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.simple_statement_deparser import SimpleStatementDeparser
from arborista.nodes.python.comment import Comment
from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.nodes.python.newline import Newline
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.simple_whitespace import SimpleWhitespace
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace


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
    (SimpleStatement([ExpressionStatement(String(None, SingleQuotedShortString('foo')))]), '', "'foo'\n"),
    (SimpleStatement([ReturnStatement()], TrailingWhitespace(SimpleWhitespace(' '))), '', 'return \n'),
    (SimpleStatement([ReturnStatement()], TrailingWhitespace(newline=Newline('\r\n'))), '', 'return\r\n'),
    (SimpleStatement([ReturnStatement()], TrailingWhitespace(SimpleWhitespace(' '), Comment('# foo'))), '', 'return # foo\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_simple_statement(simple_statement: SimpleStatement, indent: str,
                                  expected_string: str) -> None:
    """Test arborista.deparsers.python.simple_statement_deparser.SimpleStatementDeparser.deparse_simple_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = SimpleStatementDeparser.deparse_simple_statement(simple_statement, indent)

    assert string == expected_string
