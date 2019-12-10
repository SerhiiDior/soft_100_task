import unittest
from unittest.mock import Mock,patch
from probFiftyOneSixty import *



def mock_radius(r):
    return round((pi*r**2),2)

class TestRadius(unittest.TestCase):

    @patch('probFiftyOneSixty.Circle.area', side_effect=mock_radius)
    def test_radius(self,area ):
        self.assertEqual(area(r),452.39)


class TestFifth(unittest.TestCase):

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError,divide_by_zero(),"Dividing a number by zero!")


    def test_valid_email(self):
        self.assertEqual(valid_email('test@google.com'), 'test')

    def test_email_from_email(self):
        self.assertEqual(email_from_email('John@google.com'), 'google')

    def test_output_digit(self):
        self.assertEqual(output_digit('4 cows 8 cats 2 mouse 9 dogs'), ['4', '8', '2', '9'])






if __name__  == '__main__':
    unittest.main()

