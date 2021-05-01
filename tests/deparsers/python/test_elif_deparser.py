"""Test arborista.deparsers.python.elif_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.elif_deparser import ElifDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.elif_ import Elif
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.elif_deparser.ElifDeparser inheritance."""
    assert issubclass(ElifDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('elif_, expected_string', [
    (Elif(Name('foo'), SimpleStatement([PassStatement()])), 'elif foo:pass\n'),
    (Elif(Name('foo'), Block([SimpleStatement([PassStatement()])], '    ')), 'elif foo:\n    pass\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_elif(elif_: Elif, expected_string: str) -> None:
    """Test arborista.deparsers.python.elif_deparser.ElifDeparser.deparse_elif."""
    string: str = ElifDeparser.deparse_elif(elif_)

    assert string == expected_string
