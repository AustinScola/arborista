"""Test arborista.parsers.python.simple_whitespace_parser."""
import libcst
import pytest

from arborista.nodes.python.simple_whitespace import SimpleWhitespace
from arborista.parser import Parser
from arborista.parsers.python.simple_whitespace_parser import (LibcstSimpleWhitespace,
                                                               SimpleWhitespaceParser)


def test_libcst_simple_whitespace() -> None:
    """Test arborista.parsers.python.simple_whitespace_parser.LibcstSimpleWhitespace."""
    assert LibcstSimpleWhitespace == libcst.SimpleWhitespace


def test_inheritance() -> None:
    """Test arborista.parsers.python.simple_whitespace_parser.SimpleWhitespaceParser inheritance."""
    assert issubclass(SimpleWhitespaceParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_simple_whitespace, expected_simple_whitespace', [
    (libcst.SimpleWhitespace(' '), SimpleWhitespace(' ')),
    (libcst.SimpleWhitespace(' \t'), SimpleWhitespace(' \t')),
])
# yapf: enable
def test_parse_simple_whitespace(libcst_simple_whitespace: LibcstSimpleWhitespace,
                                 expected_simple_whitespace: SimpleWhitespace) -> None:
    """Test arborista.parsers.python.simple_whitespace_parser.SimpleWhitespaceParser.parse_simple_whitespace."""  # pylint: disable=line-too-long, useless-suppression
    simple_whitespace: SimpleWhitespace = SimpleWhitespaceParser.parse_simple_whitespace(
        libcst_simple_whitespace)

    assert simple_whitespace == expected_simple_whitespace
