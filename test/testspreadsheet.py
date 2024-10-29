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

    #If the cell "A1" contains "=1+3", the result of its evaluation is 4.
    def test_evaluate_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', '=1+3')
        self.assertEqual(4, spreadsheet.evaluate('A1'))

    #If the cell "A1" contains "=1+3.5", the result of its evaluation is "#Error".
    def test_evaluate_formula_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', '=1+3.5')
        self.assertEqual('#Error', spreadsheet.evaluate('A1'))

    #If the cell "A1" contains "=1/0", the result of its evaluation is "#Error".
    def test_evaluate_division_by_zero(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', '=1/0')
        self.assertEqual('#Error', spreadsheet.evaluate('A1'))

    #If the cell "A1" contains "=1+3*2", the result of its evaluation is 9.
    def test_evaluate_formula_with_precedence(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('A1', '=1+3*2')
        self.assertEqual(7, spreadsheet.evaluate('A1'))

    #If the cell "A1" contains "=1+B1" and the cell "B1" contains "3", the result of the evaluation of "A1" is 4.
    def test_evaluate_formula_with_cell_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('B1', '3')
        spreadsheet.set('A1', '=1+B1')
        self.assertEqual(4, spreadsheet.evaluate('A1'))

    #If the cell "A1" contains "=1+B1" and the cell "B1" contains "3.1", the result of the evaluation of "A1" is "#Error".
    def test_evaluate_formula_with_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('B1', '3.1')
        spreadsheet.set('A1', '=1+B1')
        self.assertEqual('#Error', spreadsheet.evaluate('A1'))

    #If the cell "A1" contains "=1+B1" and the cell "B1" contains "=A1", the result of the evaluation of "A1" is "#Circular".
    def test_evaluate_formula_with_circular_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set('B1', '=A1')
        spreadsheet.set('A1', '=1+B1')
        self.assertEqual('#Circular', spreadsheet.evaluate('A1'))