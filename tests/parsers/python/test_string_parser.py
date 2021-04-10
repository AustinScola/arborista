"""Test arborista.parsers.python.string_parser."""
from typing import Union

import libcst
import pytest

from arborista.nodes.python.double_quoted_long_string import DoubleQuotedLongString
from arborista.nodes.python.double_quoted_short_string import DoubleQuotedShortString
from arborista.nodes.python.short_string import ShortString
from arborista.nodes.python.single_quoted_long_string import SingleQuotedLongString
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String
from arborista.parser import Parser
from arborista.parsers.python.string_parser import LibcstString, StringParser


def test_libcst_string() -> None:
    """Test arborista.parsers.python.string_parser.LibcstString"""
    assert isinstance(LibcstString, type(Union))
    assert LibcstString.__args__ == (  # type: ignore[attr-defined]
        libcst.SimpleString, libcst.FormattedString)


def test_inheritance() -> None:
    """Test arborista.parsers.python.string_parser.StringParser inheritance."""
    assert issubclass(StringParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_string, expected_string', [
    (libcst.SimpleString("'foo'"), String(None, SingleQuotedShortString('foo'))),
    (libcst.SimpleString('"foo"'), String(None, DoubleQuotedShortString('foo'))),
    (libcst.SimpleString("'''foo'''"), String(None, SingleQuotedLongString('foo'))),
    (libcst.SimpleString('"""foo"""'), String(None, DoubleQuotedLongString('foo'))),
])
# yapf: enable
def test_parse_string(libcst_string: LibcstString, expected_string: ShortString) -> None:
    """Test arborista.parsers.python.string_parser.StringParser.parse_string."""
    string: String = StringParser.parse_string(libcst_string)

    assert string == expected_string
