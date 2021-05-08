"""Test arborista.deparsers.python.keyword_argument_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.keyword_argument_deparser import KeywordArgumentDeparser
from arborista.nodes.python.keyword_argument import KeywordArgument
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.keyword_argument_deparser.KeywordArgumentDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(KeywordArgumentDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('keyword_argument, expected_string', [
    (KeywordArgument(Name('foo'), Name('bar')), 'foo=bar'),
])
# yapf: enable
def test_deparse_keyword_argument(keyword_argument: KeywordArgument, expected_string: str) -> None:
    """Test arborista.deparsers.python.keyword_argument_deparser.KeywordArgumentDeparser.deparse_keyword_argument."""  # pylint: disable=line-too-long, useless-suppression
    string: str = KeywordArgumentDeparser.deparse_keyword_argument(keyword_argument)

    assert string == expected_string
