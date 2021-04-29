"""A deparser for Python import statements."""
from arborista.deparser import Deparser
from arborista.deparsers.python.import_dotted_name_deparser import ImportDottedNameDeparser
from arborista.deparsers.python.import_from_deparser import ImportFromDeparser
from arborista.nodes.python.import_dotted_name import ImportDottedName
from arborista.nodes.python.import_from import ImportFrom
from arborista.nodes.python.import_statement import ImportStatement


class ImportStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python import statements."""
    @staticmethod
    def deparse_import_statement(import_statement: ImportStatement) -> str:
        """Deparser a Python import statement."""
        string: str
        if isinstance(import_statement, ImportDottedName):
            import_dotted_name: ImportDottedName = import_statement
            string = ImportDottedNameDeparser.deparse_import_dotted_name(import_dotted_name)
        elif isinstance(import_statement, ImportFrom):
            import_from: ImportFrom = import_statement
            string = ImportFromDeparser.deparse_import_from(import_from)
        else:
            raise NotImplementedError  # pragma: no cover

        return string
