"""A deparser for Python import from statements."""
from arborista.deparser import Deparser
from arborista.deparsers.python.dotted_name_deparser import DottedNameDeparser
from arborista.deparsers.python.grouped_name_as_names_deparser import GroupedNameAsNamesDeparser
from arborista.deparsers.python.name_as_names_deparser import NameAsNamesDeparser
from arborista.deparsers.python.relative_dotted_name_deparser import RelativeDottedNameDeparser
from arborista.deparsers.python.star_deparser import StarDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.grouped_name_as_names import GroupedNameAsNames
from arborista.nodes.python.import_from import ImportFrom, Source, Target
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.relative_dotted_name import RelativeDottedName
from arborista.nodes.python.star import Star


class ImportFromDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python import statements."""
    @staticmethod
    def deparse_import_from(import_from: ImportFrom) -> str:
        """Deparser a Python import from stateemnt."""
        string: str

        source_string: str
        source: Source = import_from.source
        if isinstance(source, DottedName):
            dotted_name: DottedName = source
            source_string = DottedNameDeparser.deparse_dotted_name(dotted_name)
        else:
            relative_dotted_name: RelativeDottedName = source
            source_string = RelativeDottedNameDeparser.deparse_relative_dotted_name(
                relative_dotted_name)

        target_string: str
        target: Target = import_from.target
        if isinstance(target, Star):
            star: Star = target
            target_string = StarDeparser.deparse_star(star)
        elif isinstance(target, GroupedNameAsNames):
            grouped_name_as_names: GroupedNameAsNames = target
            target_string = GroupedNameAsNamesDeparser.deparse_grouped_name_as_names(
                grouped_name_as_names)
        else:
            name_as_names: NameAsNames = target
            target_string = NameAsNamesDeparser.deparse_name_as_names(name_as_names)

        string = f'from {source_string} import {target_string}'

        return string
