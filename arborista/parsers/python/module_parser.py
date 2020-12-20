"""Parser for a Python module."""
import libcst

from arborista.nodes.file_system.file import File
from arborista.nodes.python.module import Module
from arborista.nodes.python.statement import StatementList
from arborista.parser import Parser
from arborista.parsers.python.statement_parser import LibcstStatements, StatementParser


class ModuleParser(Parser):
    """Parser for a Python module."""
    @staticmethod
    def parse_module(name: str, string: str) -> 'Module':
        """Return a module from a string."""
        libcst_module: libcst.Module = libcst.parse_module(string)
        libcst_module_body: LibcstStatements = libcst_module.body
        body: StatementList = StatementParser.parse_statements(libcst_module_body)

        module: Module = Module(name, body)
        module.set_parent_in_children()

        return module

    @staticmethod
    def parse_module_from_file(file_: File) -> Module:
        """Return a module from a file."""
        name: str = file_.stem
        string: str = file_.contents
        module: Module = ModuleParser.parse_module(name, string)
        return module
