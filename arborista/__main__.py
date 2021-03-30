"""Package main."""
import sys

from arborista.main import main


def package_main() -> None:
    """Run the Arborista package main method with the system arguments."""
    if __name__ == '__main__':
        sys.exit(main(sys.argv[1:]))


package_main()
