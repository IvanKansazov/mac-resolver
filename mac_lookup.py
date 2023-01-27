import argparse
import re
import sys
from urllib.parse import quote, urljoin
from urllib.request import urlopen
from urllib.error import HTTPError


class InvalidMacAddress(Exception):
    pass


class MacAddressResolver:
    def __init__(self, mac_address):
        self.mac_address = mac_address
        self.resolved = None

    def validate(self):
        if not re.fullmatch('(.{2}):(.{2}):(.{2}):(.{2}):(.{2}):(.{2})', self.mac_address):
            raise InvalidMacAddress

    def resolve(self):
        _url = urljoin("https://api.macvendors.com/", quote(self.mac_address))
        with urlopen(_url) as response:
            response_text = response.read()
        self.resolved = response_text


def main(args):
    if args.mac:
        resolver = MacAddressResolver(args.mac)
        try:
            resolver.validate()
            resolver.resolve()
            print(resolver.resolved)
        except InvalidMacAddress:
            print(f'Invalid mac address {args.mac}')
            sys.exit(1)
        except HTTPError:
            print(f'Unknown mac address {args.mac}')
            sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Mac resolver',
        description='Resolve mac addresses'
    )
    parser.add_argument('-m', '--mac', type=str)
    parsed_args = parser.parse_args()
    main(parsed_args)
