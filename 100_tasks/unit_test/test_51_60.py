import unittest
from unittest.mock import Mock,patch
from probFiftyOneSixty import *


def mock_radius(r):
    return round((pi*r**2),2)

class TestRadius(unittest.TestCase):

    @patch('probFiftyOneSixty.Circle.area', side_effect=mock_radius)
    def test_radius(self,area):
        self.assertEqual(area(12),452.39)

if __name__  == '__main__':
    unittest.main()

