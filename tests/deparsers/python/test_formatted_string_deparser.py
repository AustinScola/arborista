"""Test arborista.deparsers.python.formatted_string_deparser."""
from arborista.deparser import Deparser
from arborista.deparsers.python.formatted_string_deparser import FormattedStringDeparser


def test_inheritance() -> None:
    """Test arborista.deparsers.python.formatted_string.FormattedStringDeparser inheritance."""
    assert issubclass(FormattedStringDeparser, Deparser)
