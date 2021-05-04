"""Parser for a Python compound statement."""
import libcst

from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.if_statement import IfStatement
from arborista.parser import Parser
from arborista.parsers.python.class_definition_parser import (ClassDefinitionParser,
                                                              LibcstClassDefinition)
from arborista.parsers.python.function_definition_parser import (FunctionDefinitionParser,
                                                                 LibcstFunctionDefinition)
from arborista.parsers.python.if_statement_parser import IfStatementParser, LibcstIfStatement

LibcstCompoundStatement = libcst.BaseCompoundStatement


class CompoundStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python compound statement."""
    @staticmethod
    def parse_compound_statement(
            libcst_compound_statement: LibcstCompoundStatement) -> CompoundStatement:
        """Parse a compound statement."""
        compound_statement: CompoundStatement
        if isinstance(libcst_compound_statement, LibcstIfStatement):
            libcst_if_statement: LibcstIfStatement = libcst_compound_statement
            if_statement: IfStatement = IfStatementParser.parse_if_statement(libcst_if_statement)
            compound_statement = if_statement
        elif isinstance(libcst_compound_statement, LibcstFunctionDefinition):
            libcst_function_definition: LibcstFunctionDefinition = libcst_compound_statement
            function_definition = FunctionDefinitionParser.parse_function_definition(
                libcst_function_definition)
            compound_statement = function_definition
        elif isinstance(libcst_compound_statement, LibcstClassDefinition):
            libcst_class_definition: LibcstClassDefinition = libcst_compound_statement
            class_definition = ClassDefinitionParser.parse_class_definition(libcst_class_definition)
            compound_statement = class_definition
        else:
            raise NotImplementedError(f'Parsing of compound statements of type {type(libcst_compound_statement)} is not implemented yet.')  # pragma: no cover  # pylint: disable=line-too-long, useless-suppression

        return compound_statement
