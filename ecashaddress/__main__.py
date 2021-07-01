import argparse
from typing import Sequence
import warnings

from .convert import Address, guess_prefix, KNOWN_PREFIXES
from . import version


def convert():
    """This function is the entry point defined in setup.py for the command
    line ecashconvert.
    """
    warnings.warn(
        "`ecashconvert` is deprecated, use `ecashaddress convert` instead",
        DeprecationWarning
    )
    parser = argparse.ArgumentParser(description='Convert eCash address formats.')
    parser.add_argument("input_addresses", help="Input addresses to be converted.", nargs="+")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--prefix", help="Output cashaddr prefix.", default="ecash")
    group.add_argument("--legacy", help="Convert to legacy BTC address.", action="store_true")

    args = parser.parse_args()
    _convert(args.input_addresses, args.prefix, args.legacy)


def _convert(input_addresses: Sequence[str], prefix: str, is_legacy: bool):
    for addr in input_addresses:
        if is_legacy:
            print(Address.from_string(addr).to_legacy_address())
        else:
            print(Address.from_string(addr).to_cash_address(prefix))


def main():
    """This function is the entry point defined in setup.py for the command
    line ecashaddress.
    """
    parser = argparse.ArgumentParser(
        description='Tools for working with cash addresses')
    parser.add_argument("-v", "--version", help="Print the version number",
                        action="store_true")
    subparsers = parser.add_subparsers(dest='command')

    convert_parser = subparsers.add_parser(
        'convert', help = "Convert eCash address formats")
    convert_parser.add_argument(
        "input_addresses", help="Input addresses to be converted.", nargs="+")
    group = convert_parser.add_mutually_exclusive_group()
    group.add_argument("--prefix", help="Output CashAddr prefix.",
                       default="ecash")
    group.add_argument("--legacy", help="Convert to legacy BTC address.",
                       action="store_true")

    guessprefix_parser = subparsers.add_parser(
        'guessprefix',
        help=f"Guess the prefix from a CashAddr address, by trying a list of"
             f" commonly used prefixes: {', '.join(KNOWN_PREFIXES)}.")
    guessprefix_parser.add_argument(
        "address", help="Input cash address without prefix.")

    args = parser.parse_args()
    if args.version:
        print(version)
        return

    if args.command == "convert":
        _convert(args.input_addresses, args.prefix, args.legacy)
    elif args.command == "guessprefix":
        print(guess_prefix(args.address))
    elif args.command is None:
        parser.print_help()


if __name__ == '__main__':
    # This is the entry point if the package is executed via the
    # `python -m ecashaddress` command
    main()
