"""Test arborista.parsers.python.arguments_parser."""
from typing import Sequence

import libcst
import pytest

from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.integer import Integer
from arborista.parser import Parser
from arborista.parsers.python.arguments_parser import ArgumentsParser, LibcstArguments


def test_libcst_arguments() -> None:
    """Test arborista.parsers.python.arguments_parser.LibcstArguments."""
    assert isinstance(LibcstArguments, type(Sequence))
    assert LibcstArguments.__args__ == (libcst.Arg, )  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.parsers.python.arguments_parser.ArgumentsParser inheritance."""
    assert issubclass(ArgumentsParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_arguments, expected_arguments', [
    ([], Arguments([])),
    ([libcst.Arg(libcst.Integer('5'))], Arguments([Integer(5)])),
    ([libcst.Arg(libcst.Integer('5')), libcst.Arg(libcst.Integer('7'))], Arguments([Integer(5), Integer(7)])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_arguments(libcst_arguments: LibcstArguments, expected_arguments: Arguments) -> None:
    """Test arborista.parsers.python.arguments_parser.ArgumentsParser.parse_arguments."""
    arguments: Arguments = ArgumentsParser.parse_arguments(libcst_arguments)

    assert arguments == expected_arguments
