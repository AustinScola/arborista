"""Deparser for Python arguments."""
from typing import List

from arborista.deparser import Deparser
from arborista.deparsers.python.argument_deparser import ArgumentDeparser
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.arguments import Arguments


class ArgumentsDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for Python arguments."""
    @staticmethod
    def deparse_arguments(arguments: Arguments) -> str:
        """Deparse Python arguments."""
        string: str

        first: Argument = arguments.first
        first_string = ArgumentDeparser.deparse_argument(first)

        rest: List[Argument] = arguments.rest
        rest_strings = (ArgumentDeparser.deparse_argument(argument) for argument in rest)

        string = first_string + ''.join(', ' + argument_string for argument_string in rest_strings)

        return string
