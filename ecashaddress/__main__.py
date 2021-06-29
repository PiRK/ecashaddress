import argparse

from .convert import Address


def main():
    """This function is the entry point defined in setup.py for the command
    line tools ecashconvert.
    """
    parser = argparse.ArgumentParser(description='Convert eCash address formats.')
    parser.add_argument("input_addresses", help="Input addresses to be converted.", nargs="+")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--prefix", help="Output cashaddr prefix.", default="ecash")
    group.add_argument("--legacy", help="Convert to legacy BTC address.", action="store_true")

    args = parser.parse_args()

    for addr in args.input_addresses:
        if args.legacy:
            print(Address.from_string(addr).legacy_address())
        else:
            print(Address.from_string(addr).cash_address(args.prefix))


if __name__ == '__main__':
    # This is the entry point if the package is executed via the
    # `python -m ecashaddress` command
    main()
