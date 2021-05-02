"""Test arborista.deparsers.python.argument_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.argument_deparser import ArgumentDeparser
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.argument_deparser.ArgumentDeparser inheritance."""
    assert issubclass(ArgumentDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('argument, expected_string', [
    (Name('foo'), 'foo'),
])
# yapf: enable
def test_deparse_argument(argument: Argument, expected_string: str) -> None:
    """Test arborista.deparsers.python.argument_deparser.ArgumentDeparser.deparse_argument."""
    string: str = ArgumentDeparser.deparse_argument(argument)

    assert string == expected_string
