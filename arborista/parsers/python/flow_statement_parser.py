"""Parser for a Python flow statement."""
from arborista.nodes.python.break_statement import BreakStatement
from arborista.nodes.python.continue_statement import ContinueStatement
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.parser import Parser
from arborista.parsers.python.break_statement_parser import (BreakStatementParser,
                                                             LibcstBreakStatement)
from arborista.parsers.python.continue_statement_parser import (ContinueStatementParser,
                                                                LibcstContinueStatement)
from arborista.parsers.python.return_statement_parser import (LibcstReturnStatement,
                                                              ReturnStatementParser)

LibcstFlowStatement = LibcstReturnStatement


class FlowStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python flow statement."""
    @staticmethod
    def parse_flow_statement(libcst_flow_statement: LibcstFlowStatement) -> FlowStatement:
        """Parse a Python flow statement."""
        flow_statment: FlowStatement
        if isinstance(libcst_flow_statement, LibcstBreakStatement):
            libcst_break_statement: LibcstBreakStatement = libcst_flow_statement
            break_statement: BreakStatement = BreakStatementParser.parse_break_statement(
                libcst_break_statement)
            flow_statment = break_statement
            return flow_statment
        if isinstance(libcst_flow_statement, LibcstContinueStatement):
            libcst_continue_statement: LibcstContinueStatement = libcst_flow_statement
            continue_statement: ContinueStatement = \
                ContinueStatementParser.parse_continue_statement(libcst_continue_statement)
            flow_statment = continue_statement
            return flow_statment
        if isinstance(libcst_flow_statement, LibcstReturnStatement):
            libcst_return_statement: LibcstReturnStatement = libcst_flow_statement
            return_statement: ReturnStatement = ReturnStatementParser.parse_return_statement(
                libcst_return_statement)
            flow_statment = return_statement
            return flow_statment
        raise NotImplementedError
