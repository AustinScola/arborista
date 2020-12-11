"""Main module."""
import argparse
import logging
from pathlib import Path
from typing import List, cast

from arborista.deparsers.file_system.file_deparser import FileDeparser
from arborista.deparsers.python.module_deparser import ModuleDeparser
from arborista.nodes.file_system.file import File
from arborista.nodes.python.module import Module
from arborista.parsers.file_system.file_parser import FileParser
from arborista.parsers.python.module_parser import ModuleParser
from arborista.transformation import Transformations
from arborista.transformer import Transformer
from arborista.tree import Tree

LOGGER = logging.getLogger(__package__)


def _set_up_logging() -> None:
    """Set up logging."""
    LOGGER.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    LOGGER.addHandler(stream_handler)


def _set_up_argument_parser() -> argparse.ArgumentParser:
    """Set up a argument parser."""
    argument_parser = argparse.ArgumentParser(prog=f'python3 -m {__package__}',
                                              description='A tree transformation tool.')

    argument_parser.add_argument('file', help='file to process')

    return argument_parser


def _parse_arguments(argument_parser: argparse.ArgumentParser,
                     arguments: List[str]) -> argparse.Namespace:
    """Return parsed arguments."""
    parsed_arguments: argparse.Namespace = argument_parser.parse_args(arguments)
    return parsed_arguments


def _run_arborista(parsed_arguments: argparse.Namespace) -> None:
    """Run arborista."""
    file_path: Path = Path(parsed_arguments.file)
    file_: File = FileParser.parse_file(file_path)
    module: Module = ModuleParser.parse_module_from_file(file_)
    tree: Tree = Tree(module)

    transformations: Transformations = []
    transformer = Transformer(transformations)
    transformer.run(tree)

    module_after: Module = cast(Module, tree.root)
    transformed_contents: str = ModuleDeparser.deparse_module(module_after)
    file_.contents = transformed_contents
    FileDeparser.deparse_file(file_)


def main(arguments: List[str]) -> int:
    """Main function."""
    argument_parser = _set_up_argument_parser()
    parsed_arguments: argparse.Namespace = _parse_arguments(argument_parser, arguments)
    _set_up_logging()
    _run_arborista(parsed_arguments)
    return 0
