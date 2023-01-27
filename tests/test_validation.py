import unittest
from mac_lookup import MacAddressResolver, InvalidMacAddress


class TestMacValidation(unittest.TestCase):
    def test_validation_on_invalid_mac(self):
        resolver = MacAddressResolver('asd')
        with self.assertRaises(InvalidMacAddress):
            resolver.validate()

    def test_validation_on_valid_mac(self):
        resolver = MacAddressResolver('DC:9F:DB:12:DE:A3')
        self.assertTrue(resolver.validate() is None)
