"""Test arborista.parsers.python.else_parser."""
import libcst
import pytest

from arborista.nodes.python.else_ import Else
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.parser import Parser
from arborista.parsers.python.else_parser import ElseParser, LibcstElse


def test_libcst_else() -> None:
    """Test arborista.parsers.python.else_parser.LibcstElse."""
    assert LibcstElse == libcst.Else


def test_inheritance() -> None:
    """Test arborista.parsers.python.else_parser.ElseParser inheritance."""
    assert issubclass(ElseParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_else, expected_else', [
    (libcst.Else(libcst.SimpleStatementSuite([libcst.Pass()])), Else(SimpleStatement([PassStatement()]))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_libcst_else(libcst_else: LibcstElse, expected_else: Else) -> None:
    """Test arborista.parsers.python.else_parser.ElseParser.parse_else."""
    else_: Else = ElseParser.parse_else(libcst_else)

    assert else_ == expected_else
