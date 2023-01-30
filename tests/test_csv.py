import csv
import unittest
from mac_lookup import MacCSVReader


class TestCSVReaders(unittest.TestCase):
    def setUp(self) -> None:
        self.file = open('test_csv.csv')
        self.csv_reader = MacCSVReader('test_csv.csv')

    def test_custom_dict_reader_table(self):
        expected_table = [
            {'No': '1', 'Mac': '36:0b:92:b8:42:c0', '': ''},
            {'No': '2', 'Mac': '50:ed:3c:1c:d9:86', '': ''},
            {'Station': '1', 'Mac': '36:0b:92:b8:42:c0', '': ''},
            {'Station': '2', 'Mac': '50:ed:3c:1c:d9:86', '': ''}
        ]
        table = []
        reader = csv.reader(self.file)
        header = []
        for line in reader:
            if len(line) == 0:
                header = []
            elif header:
                table.append(dict(zip(header, line)))
            else:
                header = line
        self.assertEqual(table, expected_table)

    def test_csv_to_list_table(self):
        expected_table = [
            {'No': '1', 'Mac': '36:0b:92:b8:42:c0', '': ''},
            {'No': '2', 'Mac': '50:ed:3c:1c:d9:86', '': ''},
            {'Station': '1', 'Mac': '36:0b:92:b8:42:c0', '': ''},
            {'Station': '2', 'Mac': '50:ed:3c:1c:d9:86', '': ''}
        ]
        table = self.csv_reader.create_table_from_csv()
        self.assertEqual(table, expected_table)

    def tearDown(self) -> None:
        self.file.close()
