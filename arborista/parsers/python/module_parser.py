"""Parser for a Python module."""
import libcst

from arborista.nodes.python.module import Module
from arborista.nodes.python.statement import StatementList
from arborista.parser import Parser
from arborista.parsers.python.statement_parser import LibcstStatements, StatementParser


class ModuleParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python module."""
    @staticmethod
    def parse_module(name: str, string: str) -> 'Module':
        """Return a module from a string."""
        libcst_module: libcst.Module = libcst.parse_module(string)
        libcst_module_body: LibcstStatements = libcst_module.body
        body: StatementList = StatementParser.parse_statements(libcst_module_body)

        module: Module = Module(name, body)
        return module
