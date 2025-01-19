import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-5, -5), 25)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertEqual(self.calc.divide(0, 5), 0)

        # Test division by zero
        self.assertIsNone(self.calc.divide(6, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_edge_cases(self):
        """Test edge cases for all operations."""
        self.assertEqual(self.calc.add(1e9, 1e9), 2e9)  # Large numbers
        self.assertEqual(self.calc.subtract(1e9, 1e9), 0)  # Large numbers
        self.assertEqual(self.calc.multiply(1e9, 0), 0)  # Multiplying by zero
        self.assertEqual(self.calc.divide(1e9, 1), 1e9)  # Large division


if __name__ == "__main__":
    unittest.main()
