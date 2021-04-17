"""A parser for a Python import statement."""
from typing import Union

import libcst

from arborista.nodes.python.import_dotted_name import ImportDottedName
from arborista.nodes.python.import_statement import ImportStatement
from arborista.parser import Parser
from arborista.parsers.python.import_dotted_name_parser import (ImportDottedNameParser,
                                                                LibcstImportDottedName)

LibcstImportStatement = Union[libcst.Import, libcst.ImportFrom]


class ImportStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python import statement."""
    @staticmethod
    def parse_import_statement(libcst_import_statement: LibcstImportStatement) -> ImportStatement:
        """Parse a Python import statement."""
        import_statement: ImportStatement
        if isinstance(libcst_import_statement, libcst.Import):
            libcst_import_dotted_name: LibcstImportDottedName = libcst_import_statement
            import_dotted_name: ImportDottedName = ImportDottedNameParser.parse_import_dotted_name(
                libcst_import_dotted_name)
            import_statement = import_dotted_name
        else:
            raise NotImplementedError  # pragma: no cover

        return import_statement
