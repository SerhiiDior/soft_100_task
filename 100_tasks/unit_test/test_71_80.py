import unittest
import numpy
from probSeventyOneEighty import *


class TestEight(unittest.TestCase):

    def test_calculator(self):
        self.assertEqual(calculator('2+2'),4)

    def test_task_74(self):
        self.assertIn(round((task_74())),range(10,100))

    def test_task_75(self):
        self.assertIn(round(task_75()), range(5,95))

    def test_task_79(self):
        self.assertTrue([x for x in task_79()], range(100,200,2))
        self.assertTrue(len(task_79()), 5)


if __name__ == '__main__':
    unittest.main()