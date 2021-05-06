"""Deparser for Python arguments."""
from arborista.deparser import Deparser
from arborista.deparsers.python.argument_deparser import ArgumentDeparser
from arborista.nodes.python.arguments import Arguments


class ArgumentsDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for Python arguments."""
    @staticmethod
    def deparse_arguments(arguments: Arguments) -> str:
        """Deparse Python arguments."""
        string: str

        argument_strings = (ArgumentDeparser.deparse_argument(argument)
                            for argument in arguments.arguments)

        string = ', '.join(argument_strings)

        return string
