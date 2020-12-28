"""Parser for a Python small statement."""
from typing import Sequence

import libcst

from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.small_statement import SmallStatement, SmallStatementList
from arborista.parser import Parser
from arborista.parsers.python.flow_statement_parser import FlowStatementParser, LibcstFlowStatement
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
            return small_statement
        if isinstance(libcst_small_statement, LibcstPassStatement):
            libcst_pass_statment: LibcstPassStatement = libcst_small_statement
            pass_statement: PassStatement = PassStatementParser.parse_pass_statement(
                libcst_pass_statment)
            small_statement = pass_statement
            return small_statement
        raise NotImplementedError

    @staticmethod
    def parse_small_statements(
            libcst_small_statements: LibcstSmallStatements) -> SmallStatementList:
        """Parse Python small statements."""
        small_statements: SmallStatementList = [
            SmallStatementParser.parse_small_statement(libcst_small_statement)
            for libcst_small_statement in libcst_small_statements
        ]
        return small_statements
