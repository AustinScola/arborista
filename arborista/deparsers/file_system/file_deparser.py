"""Deparser for a file."""
from arborista.deparser import Deparser
from arborista.nodes.file_system.file import File


class FileDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a file."""
    @staticmethod
    def deparse_file(file_: File) -> None:
        """Deparse a file."""
        with open(file_.path, 'w') as system_file:
            system_file.write(file_.contents)
