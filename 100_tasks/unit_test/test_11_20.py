import unittest
from  probElevenTwenty import *


class SecondClassTest(unittest.TestCase):


    def test_four_digit_binary(self):
        expected = str(1010)
        input_data = four_digit_binary('0100,0011,1010,1001')
        self.assertEqual(input_data, expected)


    def test_even_1000_3000(self):
        self.assertIn(even_1000_3000()[0], [1000])
        self.assertIn(even_1000_3000()[-1], [3000])
        self.assertIn(even_1000_3000()[10], [1020])


    def test_letters_numbers(self):
        input_data = letters_numbers('hello world! 123')
        self.assertEqual(letters_numbers("hello world! 123"), "LETTERS " + '10' + '\n' + "DIGITS " + '3')

    def test_upper_lower(self):
        self.assertEqual(upper_lower( "Hello world!" ), "UPPER CASE " + '1' + '\n' + "LOWER CASE " + '9' )

    def test_upper_lower_empty(self):
        self.assertEqual(upper_lower( "" ), "UPPER CASE " + '0' + '\n' + "LOWER CASE " + '0', 'have not any args' )


    def test_compute_value(self):
        self.assertEqual(compute_value('9'),11106)

    def test_square_odd(self):
        self.assertEqual(square_odd([1,2,3,4,5,6,7,8,9]),[1, 3, 5, 7, 9])

    def test_sorted_name_age(self):
        self.assertEqual(sort_name_age('John,23,90'),[('John', '23', '90')])


if __name__ == '__main__':
    unittest.main()