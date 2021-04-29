"""A deparser for Python import dotted name statements."""
from arborista.deparser import Deparser
from arborista.deparsers.python.dotted_name_as_names_deparser import DottedNameAsNamesDeparser
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.import_dotted_name import ImportDottedName


class ImportDottedNameDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python import dotted name statements."""
    @staticmethod
    def deparse_import_dotted_name(import_dotted_name: ImportDottedName) -> str:
        """Deparser a Python import dotted name stateemnt."""
        string: str

        dotted_name_as_names: DottedNameAsNames = import_dotted_name.dotted_name_as_names
        dotted_name_as_names_string: str = DottedNameAsNamesDeparser.deparse_dotted_name_as_names(
            dotted_name_as_names)

        string = f'import {dotted_name_as_names_string}'

        return string
