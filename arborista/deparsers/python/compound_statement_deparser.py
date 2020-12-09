"""Deparser for a Python compound statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.function_definition_deparser import FunctionDefinitionDeparser
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.function_definition import FunctionDefinition


class CompoundStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python compound statement."""
    @staticmethod
    def deparse_compound_statement(compound_statement: CompoundStatement, indent: str) -> str:
        """Deparse a Python compound statement."""
        string: str
        if isinstance(compound_statement, FunctionDefinition):
            function_definition: FunctionDefinition = compound_statement
            function_definition_string: str = \
                FunctionDefinitionDeparser.deparse_function_definition(function_definition, indent)
            string = function_definition_string
        else:
            raise NotImplementedError
        return string
