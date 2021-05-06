"""Test arborista.parsers.python.class_definition_parser."""
import libcst
import pytest

from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.class_definition import ClassDefinition
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.parser import Parser
from arborista.parsers.python.class_definition_parser import (ClassDefinitionParser,
                                                              LibcstClassDefinition)


def test_libcst_class_definition() -> None:
    """Test arborista.parsers.python.class_definition_parser.LibcstClassDefinition."""
    assert LibcstClassDefinition == libcst.ClassDef


def test_inheritance() -> None:
    """Test arborista.parsers.python.class_definition_parser.ClassDefinitionParser inheritance."""
    assert issubclass(ClassDefinitionParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_class_definition, expected_class_definition', [
    (libcst.ClassDef(libcst.Name('Foo'), libcst.SimpleStatementSuite([libcst.Pass()]), lpar=libcst.MaybeSentinel.DEFAULT, rpar=libcst.MaybeSentinel.DEFAULT), ClassDefinition(Name('Foo'), None, SimpleStatement([PassStatement()]))),
    (libcst.ClassDef(libcst.Name('Foo'), libcst.SimpleStatementSuite([libcst.Pass()]), lpar=libcst.LeftParen(), rpar=libcst.RightParen()), ClassDefinition(Name('Foo'), Arguments(), SimpleStatement([PassStatement()]))),
    (libcst.ClassDef(libcst.Name('Foo'), libcst.SimpleStatementSuite([libcst.Pass()]), [libcst.Arg(libcst.Integer('5'))]), ClassDefinition(Name('Foo'), Arguments([Integer(5)]), SimpleStatement([PassStatement()]))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_class_definition(libcst_class_definition: LibcstClassDefinition,
                                expected_class_definition: ClassDefinition) -> None:
    """Test arborista.parsers.python.class_definition_parser.ClassDefinitionParser.parse_class_definition."""  # pylint: disable=line-too-long, useless-suppression
    class_definition: ClassDefinition = ClassDefinitionParser.parse_class_definition(
        libcst_class_definition)

    assert class_definition.bases == expected_class_definition.bases
    assert class_definition == expected_class_definition
