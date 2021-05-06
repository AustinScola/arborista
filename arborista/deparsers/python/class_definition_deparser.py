"""A deparser for Python class definitions."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.arguments_deparser import ArgumentsDeparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.deparsers.python.suite_deparser import SuiteDeparser
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.block import Block
from arborista.nodes.python.class_definition import ClassDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.suite import Suite


class ClassDefinitionDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python class definitions."""
    @staticmethod
    def deparse_class_definition(class_definition: ClassDefinition, indent: str) -> str:
        """Deparse a Python class definition."""
        string: str

        name: Name = class_definition.name
        name_string: str = NameDeparser.deparse_name(name)

        string = indent + 'class ' + name_string

        bases: Optional[Arguments] = class_definition.bases
        if bases is not None:
            bases_string: str = ArgumentsDeparser.deparse_arguments(bases)
            string += '(' + bases_string + ')'

        string += ':'

        body: Suite = class_definition.body
        if isinstance(body, Block):
            body_string = '\n' + SuiteDeparser.deparse_suite(body, indent)
        else:
            body_string = SuiteDeparser.deparse_suite(body, '')

        string += body_string

        return string
