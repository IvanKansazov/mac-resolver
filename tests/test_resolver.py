import unittest

from urllib.parse import quote, urljoin
import urllib.request
import urllib.error
from mac_lookup import MacAddressResolver
from time import sleep


class TestResolver(unittest.TestCase):
    def setUp(self) -> None:
        self.resolver = MacAddressResolver('50:ed:3c:1c:d9:86')

    def test_urllib_resolve_api_usage(self):
        sleep(1)
        mac_address = 'DC:9F:DB:12:DE:A3'
        _url = urljoin("https://api.macvendors.com/", quote(mac_address))
        with urllib.request.urlopen(_url) as response:
            response_text = response.read()
        self.assertTrue(len(response_text) > 0)

    def test_mac_resolve(self):
        sleep(1)
        self.resolver.resolve()
        self.assertTrue(len(self.resolver.resolved) > 0)

    def test_bad_mac_resolve(self):
        sleep(1)
        mac_address = 'asd'
        resolver = MacAddressResolver(mac_address)
        with self.assertRaises(urllib.error.HTTPError):
            resolver.resolve()
            self.assertTrue(len(resolver.resolved) > 0)
