import unittest
import argparse
from mac_lookup import main


class TestMacResolver(unittest.TestCase):

    def test_parser_arguments(self):
        # Test that the parser has the correct arguments
        parser = argparse.ArgumentParser(prog='Mac resolver',
                                         description='Resolve mac addresses')
        parser.add_argument('-m', '--mac', type=str)
        parser.add_argument('-c', '--csv', type=str, help='Absolute path to CSV')

        self.assertEqual(parser._actions[0].dest, 'help')
        self.assertEqual(parser._actions[1].dest, 'mac')
        self.assertEqual(parser._actions[2].dest, 'csv')
        self.assertEqual(parser._actions[2].help, 'Absolute path to CSV')

    def test_mac_main(self):
        parsed_args = argparse.Namespace(mac='00:11:22:33:44:55')
        output = main(parsed_args)
        self.assertEqual(output, b'CIMSYS Inc')
        # add assert statements to test the output of the main function


if __name__ == '__main__':
    unittest.main()
