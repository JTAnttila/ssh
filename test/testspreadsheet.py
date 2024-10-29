from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', '1')
        self.assertEqual(1, spreadsheet.evaluate('A1'))

    def test_evaluate_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', '1.5')
        self.assertEqual('#Error', spreadsheet.evaluate('A1'))