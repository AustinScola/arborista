"""Test arborista.deparsers.python.class_definition_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.class_definition_deparser import ClassDefinitionDeparser
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.block import Block
from arborista.nodes.python.class_definition import ClassDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.class_definition_deparser.ClassDefinitionDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ClassDefinitionDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('class_definition, indent, expected_string', [
    (ClassDefinition(Name('Foo'), None, SimpleStatement([PassStatement()])), '', 'class Foo:pass\n'),
    (ClassDefinition(Name('Foo'), Arguments(), SimpleStatement([PassStatement()])), '', 'class Foo():pass\n'),
    (ClassDefinition(Name('Foo'), Arguments([Name('Bar')]), SimpleStatement([PassStatement()])), '', 'class Foo(Bar):pass\n'),
    (ClassDefinition(Name('Foo'), None, SimpleStatement([PassStatement()])), '    ', '    class Foo:pass\n'),
    (ClassDefinition(Name('Foo'), None, SimpleStatement([PassStatement()])), '    ', '    class Foo:pass\n'),
    (ClassDefinition(Name('Foo'), None, Block([SimpleStatement([PassStatement()])], '    ')), '    ', '    class Foo:\n        pass\n'),

])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_class_definition(class_definition: ClassDefinition, indent: str,
                                  expected_string: str) -> None:
    """Test arborista.deparsers.python.class_definition_deparser.ClassDefinitionDeparser.deparse_class_definition."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ClassDefinitionDeparser.deparse_class_definition(class_definition, indent)

    assert string == expected_string
