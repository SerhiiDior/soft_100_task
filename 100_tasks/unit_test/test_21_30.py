import unittest
from probTwentyOneThirty import *


class ThirdClassTest(unittest.TestCase):

    def test_move_robot(self):
        self.assertEqual(move_robot('UP 5 DOWN 3 LEFT 3 RIGHT 2'),2)
        self.assertEqual(move_robot( 'DOWN 3 RIGHT 2' ), 4)
        # self.assertEqual(move_robot( 'RIGHT 2' ), 4, 'error expected 2!!!')

    def test_count_freq(self):
        expected = [('2', 1), ('3', 1), ('3?', 1), ('New', 1), ('Python', 1), ('Read', 1), ('and', 1),\
                    ('between', 1), ('choosing', 1), ('or', 1), ('to', 1)]

        self.assertEqual(count_freq("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"),expected)


    def test_square_val(self):
        self.assertEqual(square_val(25),625.0)


    def test_doc_string(self):
        def print_doc(b):
            return b.__doc__
        self.assertEqual(doc_string(super), print_doc(super))

    def test_sum(self):
        self.assertEqual(sum(2,3),5)

    def test_toString(self):
        self.assertEqual((toString(5)),'5')


    def test_two_int_sum(self):
        self.assertEqual(two_int_sum('1 2'),3)
        #self.assertEqual(two_int_sum('1 2 3'),6, 'calculate only two integer')

    def test_union(self):
        self.assertEqual(union('hello','world'),'helloworld')


if __name__ == '__main__':
    unittest.main()