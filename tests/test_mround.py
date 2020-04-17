"""Test Case for the mround module"""
from __future__ import absolute_import
import unittest
from mround import round_down, round_up, round_half_up, round_half_even

class MroundTestCase(unittest.TestCase):
    """Test Case for the mround module"""
    def test_round_down(self):
        """Test the round_down function"""
        self.assertEqual(round_down(3.3), 3)
        self.assertEqual(round_down(3.6), 3)
        self.assertEqual(round_down(-3.3), -3)
        self.assertEqual(round_down(-3.6), -3)

    def test_round_up(self):
        """Test the round_up function"""
        self.assertEqual(round_up(3.3), 4)
        self.assertEqual(round_up(3.6), 4)
        self.assertEqual(round_up(-3.3), -4)
        self.assertEqual(round_up(-3.6), -4)

    def test_round_half_up(self):
        """Test the round_half_up function"""
        self.assertEqual(round_half_up(3.3), 3)
        self.assertEqual(round_half_up(3.5), 4)
        self.assertEqual(round_half_up(3.6), 4)
        self.assertEqual(round_half_up(4.5), 5)

        self.assertEqual(round_half_up(-3.3), -3)
        self.assertEqual(round_half_up(-3.5), -4)
        self.assertEqual(round_half_up(-3.6), -4)
        self.assertEqual(round_half_up(-4.5), -5)

    def test_round_half_even(self):
        """Test the round_half_even function"""
        self.assertEqual(round_half_even(3.3), 3)
        self.assertEqual(round_half_even(3.5), 4)
        self.assertEqual(round_half_even(3.6), 4)
        self.assertEqual(round_half_even(4.5), 4)

        self.assertEqual(round_half_even(-3.3), -3)
        self.assertEqual(round_half_even(-3.5), -4)
        self.assertEqual(round_half_even(-3.6), -4)
        self.assertEqual(round_half_even(-4.5), -4)

if __name__ == '__main__':
    unittest.main()
