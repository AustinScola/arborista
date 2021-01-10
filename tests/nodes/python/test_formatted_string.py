"""Test arborista.nodes.python.formatted_string."""
from arborista.nodes.python.formatted_string import FormattedString
from arborista.nodes.python.string import String


def test_inheritance() -> None:
    """Test arborista.nodes.python.formatted_string.FormattedString inheritance."""
    assert issubclass(FormattedString, String)
