"""A parser for a Python else statement."""
import libcst

from arborista.nodes.python.else_ import Else
from arborista.nodes.python.suite import Suite
from arborista.parser import Parser
from arborista.parsers.python.suite_parser import LibcstSuite, SuiteParser

LibcstElse = libcst.Else


class ElseParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python else statement."""
    @staticmethod
    def parse_else(libcst_else: LibcstElse) -> Else:
        """Parse a Python else statement."""
        libcst_body: LibcstSuite = libcst_else.body
        body: Suite = SuiteParser.parse_suite(libcst_body)

        else_: Else = Else(body)
        return else_
