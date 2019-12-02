import unittest
from  probOneTen import *



class FirstClassTest(unittest.TestCase):
    def test_range_2000_3001(self):
        self.assertIn(range_2000_3001()[0],[2002])
        self.assertIn( range_2000_3001()[-1],[2996])

    def test_factorial(self):
        self.assertEqual(factor(8),40320)

    def test_generate_dict(self):
        self.assertDictEqual(generate_dict(8),{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64})



    def test_accept_seq(self):
        expected = ['34', '67', '55', '33', '12', '98'],('34','67','55','33','12','98')
        self.assertEqual(accept_seq('34,67,55,33,12,98'), expected)


    def test_array_digit(self):
        expected = print([[0, 0, 0, 0, 0][0, 1, 2, 3, 4][0, 2, 4, 6, 8]])
        self.assertEqual( accept_seq( 3,5), expected )







if __name__ == '__main__':
    unittest.main()

