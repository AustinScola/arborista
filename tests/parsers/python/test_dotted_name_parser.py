"""Test arborista.parsers.python.dotted_name_parser."""
import libcst
import pytest

from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.dotted_name_parser import DottedNameParser, LibcstDottedName


def test_libcst_dotted_name() -> None:
    """Test arborista.parsers.python.dotted_name_parser.LibcstDottedName."""
    assert LibcstDottedName == libcst.Attribute


def test_inheritance() -> None:
    """Test arborista.parsers.python.dotted_name_parser.DottedNameParser inheritance."""
    assert issubclass(DottedNameParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_dotted_name, expected_dotted_name', [
    (libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')), DottedName(Name('foo'), [Name('bar')])),
    (libcst.Attribute(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')), libcst.Name('baz')), DottedName(Name('foo'), [Name('bar'), Name('baz')])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_dotted_name(libcst_dotted_name: LibcstDottedName,
                           expected_dotted_name: DottedName) -> None:
    """Test arborista.parsers.python.dotted_name_parser.DottedNameParser.parse_dotted_name."""
    dotted_name: DottedName = DottedNameParser.parse_dotted_name(libcst_dotted_name)

    assert dotted_name == expected_dotted_name
