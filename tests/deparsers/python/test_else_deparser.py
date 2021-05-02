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


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('else_, indent, expected_string', [
    (Else(SimpleStatement([PassStatement()])), '', 'else:pass\n'),
    (Else(SimpleStatement([PassStatement()])), '    ', '    else:pass\n'),
    (Else(Block([SimpleStatement([PassStatement()])], '    ')), '', 'else:\n    pass\n'),
    (Else(Block([SimpleStatement([PassStatement()])], '    ')), '    ', '    else:\n        pass\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_else(else_: Else, indent: str, expected_string: str) -> None:
    """Test arborista.deparsers.python.else_deparser.ElseDeparser.deparse_else."""
    string: str = ElseDeparser.deparse_else(else_, indent)

    assert string == expected_string
