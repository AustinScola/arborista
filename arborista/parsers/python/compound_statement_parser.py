"""Parser for a Python compound statement."""
import libcst

from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.parser import Parser
from arborista.parsers.python.function_definition_parser import (FunctionDefinitionParser,
                                                                 LibcstFunctionDefinition)

LibcstCompoundStatement = libcst.BaseCompoundStatement


class CompoundStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python compound statement."""
    @staticmethod
    def parse_compound_statement(
            libcst_compound_statement: LibcstCompoundStatement) -> CompoundStatement:
        """Parse a compound statement."""
        if isinstance(libcst_compound_statement, LibcstFunctionDefinition):
            libcst_function_definition: LibcstFunctionDefinition = libcst_compound_statement
            function_definition = FunctionDefinitionParser.parse_function_definition(
                libcst_function_definition)
            compound_statement = function_definition
        else:
            raise NotImplementedError  # pragma: no cover
        return compound_statement
