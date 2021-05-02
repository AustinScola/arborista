"""Test arborista.deparsers.python.arguments_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.arguments_deparser import ArgumentsDeparser
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.arguments_deparser.ArgumentsDeparser inheritance."""
    assert issubclass(ArgumentsDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('arguments, expected_string', [
    (Arguments(Name('foo'), []), 'foo'),
    (Arguments(Name('foo'), [Name('bar')]), 'foo, bar'),
    (Arguments(Name('foo'), [Name('bar'), Name('baz'),]), 'foo, bar, baz'),
])
# yapf: enable
def test_deparse_arguments(arguments: Arguments, expected_string: str) -> None:
    """Test arborista.deparsers.python.arguments_deparser.ArgumentsDeparser.deparse_arguments."""
    string: str = ArgumentsDeparser.deparse_arguments(arguments)

    assert string == expected_string
