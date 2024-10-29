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

    # test if cell "A1" contains "'Apple", the result of its evaluation is "#Error" because the string is not a valid string
    def test_evaluate_non_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', "'Apple")
        self.assertEqual('#Error', spreadsheet.evaluate('A1'))

    # test if cell "A1" contains "='Apple", the result of its evaluation is "Apple" because the string is a valid string
    #
    # test if cell "A1" contains "='1", the result of its evaluation is 1
    def test_evaluate_formula_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', "='1")
        self.assertEqual(1, spreadsheet.evaluate('A1'))

    # test if the cell "A1" contains "=B1" and "B1" contains "42", the result of the evaluation of "A1" is 42.
    def test_cell_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('B1', '42')
        spreadsheet.set('A1', '=B1')
        self.assertEqual(42, spreadsheet.evaluate('A1'))

    #If the cell "A1" contains "=B1" and "B1" contains "42.5", the result of the evaluation of "A1" is "#Error".
    def test_cell_reference_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('B1', '42.5')
        spreadsheet.set('A1', '=B1')
        self.assertEqual('#Error', spreadsheet.evaluate('A1'))

    #If the cell "A1" contains "=B1" and "B1" contains "=A1", the result of the evaluation of "A1" is "#Circular".
    def test_circular_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('B1', '=A1')
        spreadsheet.set('A1', '=B1')
        self.assertEqual('#Circular', spreadsheet.evaluate('A1'))