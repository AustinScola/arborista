"""Test arborista.deparsers.python.if_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.if_statement_deparser import IfStatementDeparser
from arborista.nodes.python.elif_ import Elif
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.if_ import If
from arborista.nodes.python.if_statement import IfStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.if_statement_deparser.IfStatementDeparser inheritance."""
    assert issubclass(IfStatementDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('if_statement, indent, expected_string', [
    (IfStatement(If(Name('foo'), SimpleStatement([PassStatement()])), [], None), '', 'if foo:pass\n'),
    (IfStatement(If(Name('foo'), SimpleStatement([PassStatement()])), [], None), '    ', '    if foo:pass\n'),
    (IfStatement(If(Name('foo'), SimpleStatement([PassStatement()])), [], Else(SimpleStatement([PassStatement()]))), '', 'if foo:pass\nelse:pass\n'),
    (IfStatement(If(Name('foo'), SimpleStatement([PassStatement()])), [], Else(SimpleStatement([PassStatement()]))), '    ', '    if foo:pass\n    else:pass\n'),
    (IfStatement(If(Name('foo'), SimpleStatement([PassStatement()])), [Elif(Name('bar'), SimpleStatement([PassStatement()]))], None), '', 'if foo:pass\nelif bar:pass\n'),
    (IfStatement(If(Name('foo'), SimpleStatement([PassStatement()])), [Elif(Name('bar'), SimpleStatement([PassStatement()]))], None), '    ', '    if foo:pass\n    elif bar:pass\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_if_statement(if_statement: IfStatement, indent: str, expected_string: str) -> None:
    """Test arborista.deparsers.python.if_statement_deparser.IfStatementDeparser.deparse_if_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = IfStatementDeparser.deparse_if_statement(if_statement, indent)

    assert string == expected_string
