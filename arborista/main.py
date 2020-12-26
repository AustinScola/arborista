"""Main module."""
import argparse
import logging
from pathlib import Path
from typing import List

from arborista.nodes.file_system.path_node import PathNode
from arborista.transformation import TransformationSet
from arborista.transformations.file_system.deparsers.deparse_file import DeparseFile
from arborista.transformations.file_system.parsers.path_to_file import PathToFile
from arborista.transformations.python.deparsers.module_to_string import ModuleToString
from arborista.transformations.python.parsers.file_to_module import FileToModule
from arborista.transformations.python.trim_after_return import TrimAfterReturn
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

    argument_parser.add_argument('file', type=Path, help='file to process')

    return argument_parser


def _parse_arguments(argument_parser: argparse.ArgumentParser,
                     arguments: List[str]) -> argparse.Namespace:
    """Return parsed arguments."""
    parsed_arguments: argparse.Namespace = argument_parser.parse_args(arguments)
    return parsed_arguments


def _run_arborista(parsed_arguments: argparse.Namespace) -> None:
    """Run arborista."""
    tree: Tree = _parse(parsed_arguments)
    transformed_tree: Tree = _transform(tree)
    _deparse(transformed_tree)


def _parse(parsed_arguments: argparse.Namespace) -> Tree:
    """Parse the tree."""
    file_path: Path = parsed_arguments.file
    tree: Tree = Tree(root=PathNode(file_path))

    transformations: TransformationSet = {PathToFile(), FileToModule()}
    transformer: Transformer = Transformer(transformations)
    tree = transformer.run(tree)

    return tree


def _transform(tree: Tree) -> Tree:
    """Transform the tree."""
    transformations: TransformationSet = {TrimAfterReturn()}
    transformer = Transformer(transformations)
    transformed_tree: Tree = transformer.run(tree)
    return transformed_tree


def _deparse(tree: Tree) -> None:
    transformations: TransformationSet = {ModuleToString(), DeparseFile()}
    transformer = Transformer(transformations)
    transformer.run(tree)


def main(arguments: List[str]) -> int:
    """Main function."""
    argument_parser = _set_up_argument_parser()
    parsed_arguments: argparse.Namespace = _parse_arguments(argument_parser, arguments)
    _set_up_logging()
    _run_arborista(parsed_arguments)
    return 0
