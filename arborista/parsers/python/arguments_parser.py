"""A parser for Python arguments."""
from typing import Iterable, Sequence

import libcst

from arborista.nodes.python.argument import Argument
from arborista.nodes.python.arguments import Arguments
from arborista.parser import Parser
from arborista.parsers.python.argument_parser import ArgumentParser

LibcstArguments = Sequence[libcst.Arg]


class ArgumentsParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for Python arguments."""
    @staticmethod
    def parse_arguments(libcst_arguments: LibcstArguments) -> Arguments:
        """Parse Python arguments."""
        arguments: Iterable[Argument] = (ArgumentParser.parse_argument(libcst_argument)
                                         for libcst_argument in libcst_arguments)

        arguments_node: Arguments = Arguments(arguments)

        return arguments_node
