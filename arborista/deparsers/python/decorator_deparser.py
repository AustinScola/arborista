"""Deparser for Python decorators."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.arguments_deparser import ArgumentsDeparser
from arborista.deparsers.python.dotted_name_deparser import DottedNameDeparser
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.decorator import Decorator, Decorators
from arborista.nodes.python.dotted_name import DottedName


class DecoratorDeparser(Deparser):
    """Deparser for Python decorators."""
    @staticmethod
    def deparse_decorator(decorator: Decorator, indent: str) -> str:
        """Deparse a Python decorator."""
        string: str

        name: DottedName = decorator.name
        name_string = DottedNameDeparser.deparse_dotted_name(name)

        string = indent + "@" + name_string

        arguments: Optional[Arguments] = decorator.arguments
        if arguments is not None:
            arguments_string = ArgumentsDeparser.deparse_arguments(arguments)
            string += "(" + arguments_string + ")"

        string += '\n'

        return string

    @staticmethod
    def deparse_decorators(decorators: Decorators, indent: str) -> str:
        """Deparse Python decorators."""
        decorator_strings = (DecoratorDeparser.deparse_decorator(decorator, indent)
                             for decorator in decorators)

        return ''.join(decorator_strings)
