# test_coinkey.py
"""
Tests for CoinKey module.
"""

import unittest
from coinkey import CoinKey

class TestCoinKey(unittest.TestCase):
    """Test cases for CoinKey class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinKey()
        self.assertIsInstance(instance, CoinKey)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinKey()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
