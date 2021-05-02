"""Test arborista.deparsers.python.function_definition_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.function_definition_deparser import FunctionDefinitionDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.function_definition_deparser.FunctionDefinitionDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(FunctionDefinitionDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('function_definition, indent, expected_string', [
    (FunctionDefinition(Name('foo'), parameters=[], body=SimpleStatement([ReturnStatement()])), '', 'def foo():return\n'),
    (FunctionDefinition(Name('foo'), parameters=[], body=SimpleStatement([ReturnStatement()]), returns=Name('Bar')), '', 'def foo() -> Bar:return\n'),
    (FunctionDefinition(Name('foo'), parameters=[], body=SimpleStatement([ReturnStatement()])), '    ', '    def foo():return\n'),
    (FunctionDefinition(Name('foo'), parameters=[], body=SimpleStatement([ReturnStatement()])), '\t', '\tdef foo():return\n'),
    (FunctionDefinition(Name('foo'), parameters=[], body=Block([SimpleStatement([ReturnStatement()])], '    ')), '', 'def foo():\n    return\n'),
    (FunctionDefinition(Name('foo'), parameters=[], body=Block([SimpleStatement([ReturnStatement()])], '    ')), '    ', '    def foo():\n        return\n'),
    (FunctionDefinition(Name('foo'), parameters=[], body=Block([SimpleStatement([ReturnStatement()])], '    ')), '\t', '\tdef foo():\n\t    return\n'),
    (FunctionDefinition(Name('foo'), parameters=[Parameter(Name('a'))], body=SimpleStatement([ReturnStatement()])), '    ', '    def foo(a):return\n'),
    (FunctionDefinition(Name('foo'), parameters=[Parameter(Name('a')), Parameter(Name('b'))], body=SimpleStatement([ReturnStatement()])), '    ', '    def foo(a,b):return\n'),
    (FunctionDefinition(Name('foo'), parameters=[Parameter(Name('a')), Parameter(Name('b')), Parameter(Name('c'))], body=SimpleStatement([ReturnStatement()])), '    ', '    def foo(a,b,c):return\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_function_definition(function_definition: FunctionDefinition, indent: str,
                                     expected_string: str) -> None:
    """Test arborista.deparsers.python.function_definition_deparser.FunctionDefinitionDeparser.deparse_function_definition."""  # pylint: disable=line-too-long, useless-suppression
    string: str = FunctionDefinitionDeparser.deparse_function_definition(
        function_definition, indent)

    assert string == expected_string
