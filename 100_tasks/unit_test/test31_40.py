import unittest
from probThirtyOneFourty import *
from unittest.mock import patch


class FourClassTest(unittest.TestCase):

    def test_compare(self):
        self.assertEqual(compare('12345first','1234'), '12345first')
        self.assertEqual(compare('1234','12345second'),'12345second')
        self.assertEqual(compare( '12345equal', '12345equal' ), '12345equal 12345equal' )

    def  test_even_number(self):
        self.assertEqual(even_number(2),"It is an even number")
        self.assertEqual(even_number(3), "It is an odd number")
        self.assertEqual(even_number(0), "It is an even number")

    def test_printdic(self):
        self.assertEqual(printdic(),{1: 1, 2: 4, 3: 9} )

    # def test_printkey(self):
    #    self.assertEqual(printkey(6), 'dict_keys([1, 2, 3, 4, 5, 6])')


    def test_dict_value2(self):
        self.assertEqual(dict_value_2(),[1, 4, 9, 16, 25, 36] )

    def test_dict_value_3(self):
        self.assertEqual(dict_value_3(),[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])








if __name__=='__main__':
    unittest.main()