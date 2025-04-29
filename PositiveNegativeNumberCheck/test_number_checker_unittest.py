import unittest
from number_checker import NumberChecker

class TestNumberChecker(unittest.TestCase):
    
    def test_positive_number(self):
        checker = NumberChecker(10)
        self.assertEqual(checker.check(), "The number is positive.")
        
    def test_negative_number(self):
        checker = NumberChecker(-1)
        self.assertEqual(checker.check(), "The number is negative.")
        
    def test_zero(self):
        checker = NumberChecker(0)
        self.assertEqual(checker.check(), "The number is zero.")
        
if __name__ == '__main__':
    unittest.main()