"""Test arborista.deparsers.python.for_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.for_statement_deparser import ForStatementDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.for_statement import ForStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.for_statement_deparser.ForStatementDeparser inheritance."""
    assert issubclass(ForStatementDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('for_statement, indent, expected_string', [
    (ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), None), '', 'for foo in bar:pass\n'),
    (ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), Else(SimpleStatement([PassStatement()]))), '', 'for foo in bar:pass\nelse:pass\n'),
    (ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), None), '    ', '    for foo in bar:pass\n'),
    (ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), Block([SimpleStatement([PassStatement()])], '    '), Else(Block([SimpleStatement([PassStatement()])], '    '))), '', 'for foo in bar:\n    pass\nelse:\n    pass\n'),
    (ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), Block([SimpleStatement([PassStatement()])], '    '), Else(Block([SimpleStatement([PassStatement()])], '    '))), '    ', '    for foo in bar:\n        pass\n    else:\n        pass\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_for_statement(for_statement: ForStatement, indent: str,
                               expected_string: str) -> None:
    """Test arborista.deparsers.python.for_statement_deparser.ForStatementDeparser.deparse_for_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ForStatementDeparser.deparse_for_statement(for_statement, indent)

    assert string == expected_string
