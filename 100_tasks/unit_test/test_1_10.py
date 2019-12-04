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
        expected = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
        self.assertEqual(array_digit(), expected )

    def test_seq_of_word(self):
        expected = 'bag,hello,without,world'
        self.assertEqual(seq_of_word('without,hello,bag,world'),expected)

    def test_capitalize_word(self):
        self.assertEqual(capitalize_word(),'HELLO WORLD')
        self.assertEqual(capitalize_word(), 'hello world', 'must be capitalize' )


    def test_seq_of_word(self):
        expected = 'again and hello makes perfect practice world'
        expected2 = 'Italy Spain USA Ukraine'
        input_data = split_comma('hello world and practice makes perfect and hello world again')
        input_data2 = split_comma('Ukraine USA Spain Italy Ukraine USA Spain Italy')
        self.assertEqual(input_data,expected)
        self.assertEqual(input_data2, expected2, )
        #self.assertEqual(input_data2, 'Ukraine USA Spain Italy', 'not alphabetical sequence')







if __name__ == '__main__':
    unittest.main()

