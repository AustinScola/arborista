"""Test arborista.parsers.python.function_definition_parser."""
import libcst
import pytest

from arborista.nodes.python.block import Block
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.parser import Parser
from arborista.parsers.python.function_definition_parser import (FunctionDefinitionParser,
                                                                 LibcstFunctionDefinition)
from testing_helpers.assert_parent_set_in_children import assert_parent_set_in_children


def test_inheritance() -> None:
    """Test arborista.parsers.python.function_definition_parser.FunctionDefinitionParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(FunctionDefinitionParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_function_definition, expected_function_definition', [
    (libcst.FunctionDef(name=libcst.Name(value='foo'), params=libcst.Parameters(), body=libcst.IndentedBlock([libcst.SimpleStatementLine([libcst.Return()])])), FunctionDefinition(name=Name('foo'), parameters=[], body=Block([SimpleStatement([ReturnStatement()])], '   '))),
    (libcst.FunctionDef(name=libcst.Name(value='foo'), params=libcst.Parameters([libcst.Param(libcst.Name('bar'))]), body=libcst.IndentedBlock([libcst.SimpleStatementLine([libcst.Return()])])), FunctionDefinition(name=Name('foo'), parameters=[Parameter(Name('bar'))], body=Block([SimpleStatement([ReturnStatement()])], '   '))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_function_definition(libcst_function_definition: LibcstFunctionDefinition,
                                   expected_function_definition: FunctionDefinition) -> None:
    """Test arborista.parsers.python.function_definition_parser.FunctionDefinitionParser.parse_function_definition."""  # pylint: disable=line-too-long, useless-suppression
    function_definition = FunctionDefinitionParser.parse_function_definition(
        libcst_function_definition)

    assert function_definition == expected_function_definition
    assert_parent_set_in_children(function_definition)
