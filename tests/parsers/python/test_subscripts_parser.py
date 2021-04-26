"""Test arborista.parsers.python.subscripts_parser."""
from typing import Sequence

import libcst
import pytest

from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.subscripts import Subscripts
from arborista.parser import Parser
from arborista.parsers.python.subscripts_parser import LibcstSubscripts, SubscriptsParser


def test_libcst_subscripts() -> None:
    """Test arborista.parsers.python.subscripts_parser.LibcstSubscripts."""
    assert isinstance(LibcstSubscripts, type(Sequence))
    assert LibcstSubscripts.__args__ == (libcst.SubscriptElement, )  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.parsers.python.subscripts_parser.SubscriptsParser inheritance."""
    assert issubclass(SubscriptsParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_subscripts, expected_subscripts', [
    ([libcst.SubscriptElement(libcst.Index(libcst.Integer('0')))], Subscripts(Index(Integer(0)), [])),
    ([libcst.SubscriptElement(libcst.Index(libcst.Integer('0'))), libcst.SubscriptElement(libcst.Index(libcst.Integer('1')))], Subscripts(Index(Integer(0)), [Index(Integer(1))])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_subscripts(libcst_subscripts: LibcstSubscripts,
                          expected_subscripts: Subscripts) -> None:
    """Test arborista.parsers.python.subscripts_parser.SubscriptsParser.parse_subscripts."""
    subscripts: Subscripts = SubscriptsParser.parse_subscripts(libcst_subscripts)

    assert subscripts == expected_subscripts
