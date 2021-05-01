"""Test arborista.deparsers.python.if_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.if_deparser import IfDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.if_ import If
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.if_deparser.IfDeparser inheritance."""
    assert issubclass(IfDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('if_, expected_string', [
    (If(Name('foo'), SimpleStatement([PassStatement()])), 'if foo:pass\n'),
    (If(Name('foo'), Block([SimpleStatement([PassStatement()])], '    ')), 'if foo:\n    pass\n'),
])
# yapf: enable
def test_deparse_if(if_: If, expected_string: str) -> None:
    """Test arborista.deparsers.python.if_deparser.IfDeparser.deparse_if."""
    string: str = IfDeparser.deparse_if(if_)

    assert string == expected_string
