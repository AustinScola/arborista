"""Test arborista.parsers.python.formatted_string_parser."""
from arborista.parser import Parser
from arborista.parsers.python.formatted_string_parser import FormattedStringParser


def test_inheritance() -> None:
    """Test arborista.parsers.python.formatted_string_parser.FormattedStringParser inheritance."""
    assert issubclass(FormattedStringParser, Parser)
