"""Test arborista.parsers.python.keyword_argument_parser."""
import libcst
import pytest

from arborista.nodes.python.integer import Integer
from arborista.nodes.python.keyword_argument import KeywordArgument
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.keyword_argument_parser import (KeywordArgumentParser,
                                                              LibcstKeywordArgument)


def test_libcst_keyword_argument() -> None:
    """Test arborista.parsers.python.keyword_argument_parser.LibcstKeywordArgument."""
    assert LibcstKeywordArgument == libcst.Arg


def test_inheritance() -> None:
    """Test arborista.parsers.python.keyword_argument_parser.KeywordArgumentParser inheritance."""
    assert issubclass(KeywordArgumentParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_keyword_argument, expected_keyword_argument', [
    (libcst.Arg(libcst.Integer('5'), libcst.Name('foo')), KeywordArgument(Name('foo'), Integer(5))),
])
# yapf: enable
def test_parse_keyword_argument(libcst_keyword_argument: LibcstKeywordArgument,
                                expected_keyword_argument: KeywordArgument) -> None:
    """Test arborista.parsers.python.keyword_argument_parser.KeywordArgumentParser.parse_keyword_argument."""  # pylint: disable=line-too-long, useless-suppression
    keyword_argument: KeywordArgument = KeywordArgumentParser.parse_keyword_argument(
        libcst_keyword_argument)

    assert keyword_argument == expected_keyword_argument
