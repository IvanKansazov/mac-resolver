import argparse
import re
import csv
from urllib.parse import quote, urljoin
from urllib.request import urlopen
from urllib.error import HTTPError


class InvalidMacAddress(Exception):
    pass


class MacCSVReader:
    def __init__(self, path: str):
        self.file = open(path)
        self.table = []

    def create_table_from_csv(self):
        reader = csv.reader(self.file)
        header = []
        for line in reader:
            if len(line) == 0:
                header = []
            elif header:
                self.table.append(dict(zip(header, line)))
            else:
                header = line
        return self.table

    def __del__(self):
        self.file.close()


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
        resolver.validate()
        resolver.resolve()
        return resolver.resolved


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Mac resolver',
        description='Resolve mac addresses'
    )
    parser.add_argument('-m', '--mac', type=str)
    parser.add_argument('-c', '--csv', type=str, help='Absolute path to CSV')
    parsed_args = parser.parse_args()
    try:
        print(main(parsed_args))
    except InvalidMacAddress:
        print(f'Invalid mac address {parsed_args.mac}')
    except HTTPError:
        print(f'Unknown mac address {parsed_args.mac}')
