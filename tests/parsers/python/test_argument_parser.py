"""Test arborista.parsers.python.argument_parser."""
import libcst
import pytest

from arborista.nodes.python.argument import Argument
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.keyword_argument import KeywordArgument
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.argument_parser import ArgumentParser, LibcstArgument


def test_libcst_argument() -> None:
    """Test arborista.parsers.python.argument_parser.LibcstArgument."""
    assert LibcstArgument == libcst.Arg


def test_inheritance() -> None:
    """Test arborista.parsers.python.argument_parser.ArgumentParser inheritance."""
    assert issubclass(ArgumentParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_argument, expected_argument', [
    (libcst.Arg(libcst.Integer('5')), Integer(5)),
    (libcst.Arg(libcst.Integer('5'), libcst.Name('foo')), KeywordArgument(Name('foo'), Integer(5))),
])
# yapf: enable
def test_parse_argument(libcst_argument: LibcstArgument, expected_argument: Argument) -> None:
    """Test arborista.parsers.python.argument_parser.ArgumentParser.parse_argument."""
    argument: Argument = ArgumentParser.parse_argument(libcst_argument)

    assert argument == expected_argument
