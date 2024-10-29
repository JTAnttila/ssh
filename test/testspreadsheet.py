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

    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', "'Apple'")
        self.assertEqual('Apple', spreadsheet.evaluate('A1'))

    def test_evaluate_non_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', "'Apple")
        self.assertEqual('#Error', spreadsheet.evaluate('A1'))

    # test if cell "A1" contains "='Apple", the result of its evaluation is "Apple"
    def test_evaluate_formula_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', "='Apple")
        self.assertEqual('Apple', spreadsheet.evaluate('A1'))

    # test if cell "A1" contains "='1", the result of its evaluation is 1
    def test_evaluate_formula_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', "='1")
        self.assertEqual(1, spreadsheet.evaluate('A1'))