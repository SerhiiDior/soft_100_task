import unittest
from probFourtyOneFifty import *


class FifthClassTest(unittest.TestCase):


    def test_tu(self):
        self.assertEqual(tu(10), (1, 4, 9, 16, 25, 36, 49, 64, 81, 100))

    def test_two_line_tuple(self):
        self.assertEqual(two_line_tuple(1,2,3,4,5,6,7,8,9,10), '(1, 2, 3, 4, 5)' + '\n' + '(6, 7, 8, 9, 10)' )

    # def test_even_tuple(self):
    #     self.assertEqual(even_tuple(),(2, 4, 6, 8, 10))


    def test_yes_no(self):
        self.assertEqual(yes_no('yes'),"Yes")
        self.assertEqual( yes_no( 'YES' ), "Yes" )
        self.assertEqual(yes_no(''),'No')

    def test_use_map_sq(self):
        input_data = use_map_sq([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(input_data,[1, 4, 9, 16, 25, 36, 49, 64, 81, 100])



if __name__ == '__main__':
    unittest.main()