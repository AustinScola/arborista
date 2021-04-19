"""A parser for a Python class definition."""
from typing import Optional

import libcst

from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.class_definition import ClassDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.suite import Suite
from arborista.parser import Parser
from arborista.parsers.python.arguments_parser import ArgumentsParser
from arborista.parsers.python.name_parser import LibcstName, NameParser
from arborista.parsers.python.suite_parser import LibcstSuite, SuiteParser

LibcstClassDefinition = libcst.ClassDef


class ClassDefinitionParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python class definition."""
    @staticmethod
    def parse_class_definition(libcst_class_definition: LibcstClassDefinition) -> ClassDefinition:
        """Parse a Python class definition."""
        libcst_name: LibcstName = libcst_class_definition.name
        name: Name = NameParser.parse_name(libcst_name)

        bases: Optional[Arguments]
        libcst_arguments = libcst_class_definition.bases
        if libcst_arguments:
            bases = ArgumentsParser.parse_arguments(libcst_arguments)
        else:
            bases = None

        libcst_suite: LibcstSuite = libcst_class_definition.body
        body: Suite = SuiteParser.parse_suite(libcst_suite)

        class_definition: ClassDefinition = ClassDefinition(name, bases, body)
        return class_definition
