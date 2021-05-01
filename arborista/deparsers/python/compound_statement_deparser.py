"""Deparser for a Python compound statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.function_definition_deparser import FunctionDefinitionDeparser
from arborista.deparsers.python.if_statement_deparser import IfStatementDeparser
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.if_statement import IfStatement


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
        elif isinstance(compound_statement, IfStatement):
            if_statement: IfStatement = compound_statement
            if_statement_string: str = \
                IfStatementDeparser.deparse_if_statement(if_statement)
            string = if_statement_string
        else:
            raise NotImplementedError  # pragma: no cover
        return string
