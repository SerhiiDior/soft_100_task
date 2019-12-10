import unittest
from probEightOneNinety import *


class TestNine(unittest.TestCase):

    def test_task_81(self):
        self.assertIn(task_81(), range(7,15))