"""A parser for Python arguments."""
from typing import List, Sequence

import libcst

from arborista.nodes.python.argument import Argument
from arborista.nodes.python.arguments import Arguments
from arborista.parser import Parser
from arborista.parsers.python.argument_parser import ArgumentParser, LibcstArgument

LibcstArguments = Sequence[libcst.Arg]


class ArgumentsParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for Python arguments."""
    @staticmethod
    def parse_arguments(libcst_arguments: LibcstArguments) -> Arguments:
        """Parse Python arguments."""
        libcst_first: LibcstArgument = libcst_arguments[0]
        first: Argument = ArgumentParser.parse_argument(libcst_first)

        libcst_rest: LibcstArguments = libcst_arguments[1:]
        rest: List[Argument] = [
            ArgumentParser.parse_argument(libcst_argument) for libcst_argument in libcst_rest
        ]

        arguments: Arguments = Arguments(first, rest)
        return arguments
