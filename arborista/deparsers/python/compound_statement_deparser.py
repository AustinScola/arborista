"""Deparser for a Python compound statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.class_definition_deparser import ClassDefinitionDeparser
from arborista.deparsers.python.for_statement_deparser import ForStatementDeparser
from arborista.deparsers.python.function_definition_deparser import FunctionDefinitionDeparser
from arborista.deparsers.python.if_statement_deparser import IfStatementDeparser
from arborista.nodes.python.class_definition import ClassDefinition
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.for_statement import ForStatement
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
        elif isinstance(compound_statement, ClassDefinition):
            class_definition: ClassDefinition = compound_statement
            class_definition_string: str = \
                ClassDefinitionDeparser.deparse_class_definition(class_definition, indent)
            string = class_definition_string
        elif isinstance(compound_statement, IfStatement):
            if_statement: IfStatement = compound_statement
            if_statement_string: str = \
                IfStatementDeparser.deparse_if_statement(if_statement, indent)
            string = if_statement_string
        elif isinstance(compound_statement, ForStatement):
            for_statement: ForStatement = compound_statement
            for_statement_string: str = \
                ForStatementDeparser.deparse_for_statement(for_statement, indent)
            string = for_statement_string
        else:
            raise NotImplementedError(f'Deparsing of compound statements of type {type(compound_statement)} is not implemented yet.')  # pragma: no cover  # pylint: disable=line-too-long, useless-suppression

        return string
