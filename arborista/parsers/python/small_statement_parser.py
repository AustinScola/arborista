"""Parser for a Python small statement."""
from typing import Sequence

import libcst

from arborista.nodes.python.assignment_statement import AssignmentStatement
from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.import_statement import ImportStatement
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.small_statement import SmallStatement, SmallStatementList
from arborista.parser import Parser
from arborista.parsers.python.assignment_statement_parser import (AssignmentStatementParser,
                                                                  LibcstAssignmentStatement)
from arborista.parsers.python.expression_statement_parser import (ExpressionStatementParser,
                                                                  LibcstExpressionStatement)
from arborista.parsers.python.flow_statement_parser import FlowStatementParser, LibcstFlowStatement
from arborista.parsers.python.import_statement_parser import (ImportStatementParser,
                                                              LibcstImportStatement)
from arborista.parsers.python.pass_statement_parser import LibcstPassStatement, PassStatementParser

LibcstSmallStatement = libcst.BaseSmallStatement
LibcstSmallStatements = Sequence[LibcstSmallStatement]


class SmallStatementParser(Parser):
    """Parser for a Python small statement."""
    @staticmethod
    def parse_small_statement(libcst_small_statement: LibcstSmallStatement) -> SmallStatement:
        """Parse a Python small statement."""
        small_statement: SmallStatement
        if isinstance(libcst_small_statement, LibcstFlowStatement):
            libcst_flow_statment: LibcstFlowStatement = libcst_small_statement
            flow_statement: FlowStatement = FlowStatementParser.parse_flow_statement(
                libcst_flow_statment)
            small_statement = flow_statement
        elif isinstance(libcst_small_statement, LibcstPassStatement):
            libcst_pass_statment: LibcstPassStatement = libcst_small_statement
            pass_statement: PassStatement = PassStatementParser.parse_pass_statement(
                libcst_pass_statment)
            small_statement = pass_statement
        elif isinstance(libcst_small_statement, LibcstExpressionStatement):
            libcst_expression_statement: LibcstExpressionStatement = libcst_small_statement
            expression_statement: ExpressionStatement = \
                ExpressionStatementParser.parse_expression_statement(libcst_expression_statement)
            small_statement = expression_statement
        elif isinstance(libcst_small_statement, (libcst.Import, libcst.ImportFrom)):
            libcst_import_statement: LibcstImportStatement = libcst_small_statement
            import_statement: ImportStatement = \
                ImportStatementParser.parse_import_statement(libcst_import_statement)
            small_statement = import_statement
        elif isinstance(libcst_small_statement, LibcstAssignmentStatement):
            libcst_assignment_statement: LibcstAssignmentStatement = libcst_small_statement
            assignment_statement: AssignmentStatement = \
                AssignmentStatementParser.parse_assignment_statement(libcst_assignment_statement)
            small_statement = assignment_statement
        else:
            raise NotImplementedError  # pragma: no cover
        return small_statement

    @staticmethod
    def parse_small_statements(
            libcst_small_statements: LibcstSmallStatements) -> SmallStatementList:
        """Parse Python small statements."""
        small_statements: SmallStatementList = [
            SmallStatementParser.parse_small_statement(libcst_small_statement)
            for libcst_small_statement in libcst_small_statements
        ]
        return small_statements
