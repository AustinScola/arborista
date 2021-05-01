"""Test arborista.deparsers.python.else_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.else_deparser import ElseDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.else_deparser.ElseDeparser inheritance."""
    assert issubclass(ElseDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('else_, expected_string', [
    (Else(SimpleStatement([PassStatement()])), 'else:pass\n'),
    (Else(Block([SimpleStatement([PassStatement()])], '    ')), 'else:\n    pass\n'),
])
# yapf: enable
def test_deparse_else(else_: Else, expected_string: str) -> None:
    """Test arborista.deparsers.python.else_deparser.ElseDeparser.deparse_else."""
    string: str = ElseDeparser.deparse_else(else_)

    assert string == expected_string
