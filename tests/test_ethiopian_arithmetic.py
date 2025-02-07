import unittest
from ethiomultlib import ethiopian_multiplication

class TestEthiopianMultiplication(unittest.TestCase):

    def test_valid_positive_integers(self):
        """Test with various valid positive integer inputs."""
        test_cases = [
            (45, 12, 540),
            (17, 34, 578),
            (5, 7, 35),
            (1, 100, 100),
            (100, 1, 100),
            (1234, 5678, 7006652),
            (2, 2, 4),
            (3, 3, 9),
            (10, 10, 100),
            (99, 101, 9999), # Near 100 boundary
            (100, 100, 10000), # Exactly 100 boundary
            (101, 99, 9999), # Just over 100 boundary
            (111111111, 111111111, 12345678987654321) # Just way over 100,000,000 boundary
        ]
        for num1, num2, expected in test_cases:
            with self.subTest(f"Testing {num1} * {num2}"): # Subtests for clarity
                self.assertEqual(ethiopian_multiplication(num1, num2), expected)

    def test_large_positive_integers(self):
        """Test with very large positive integers to check for overflow (within Python's limits)."""
        large_num1 = 10**15 + 7
        large_num2 = 10**12 - 3
        expected_large_product = large_num1 * large_num2
        self.assertEqual(ethiopian_multiplication(large_num1, large_num2), expected_large_product)

    def test_commutative_property(self):
        """Test commutativity: a * b should be equal to b * a."""
        num1 = 789
        num2 = 456
        self.assertEqual(ethiopian_multiplication(num1, num2), ethiopian_multiplication(num2, num1),
                         "Commutative property test failed")

    def test_input_type_errors(self):
        """Test that TypeError is raised for invalid input types (non-integers)."""
        invalid_inputs = [
            (3.14, 5),
            (5, 3.14),
            ("hello", 5),
            (5, "world"),
            ([1, 2], 5),
            (None, 5),
            (object(), 5)
        ]
        for input1, input2 in invalid_inputs:
            with self.subTest(f"Testing invalid types: {type(input1)}, {type(input2)}"):
                with self.assertRaises(TypeError):
                    ethiopian_multiplication(input1, input2)

    def test_input_value_errors(self):
        """Test that ValueError is raised for invalid input values (non-positive integers)."""
        invalid_values = [
            (-5, 10),
            (10, -5),
            (0, 10),
            (10, 0),
            (-1, -1)
        ]
        for input1, input2 in invalid_values:
            with self.subTest(f"Testing invalid values: {input1}, {input2}"):
                with self.assertRaises(ValueError):
                    ethiopian_multiplication(input1, input2)

    def test_zero_product_edge_case_indirectly(self):
        """
        Indirectly test edge case related to zero product possibility in broader context.
        (Note: function is designed for *positive* integers, so direct zero input is ValueError)
        This tests how it behaves with valid inputs that could lead to zero in a larger algorithm.
        For Ethiopian Multiplication itself, input 0 is invalid, but checking robustness is good.
        """
        # While 0 is not valid input for *this* function, in a larger system, you might
        # get a calculation that leads to zero as one of the arguments *passed* to this function.
        # For this specific function, we are testing the *valid positive integer* range.
        # Direct zero input is already tested by ValueError tests.
        pass # No specific test needed for *this* function for zero product, as input validation handles it.
             # The function correctly handles positive integers, which is its defined scope.

    def test_performance_reasonable(self):
        """Basic performance check - ensure it's reasonably fast for moderately large numbers."""
        import time
        start_time = time.time()
        ethiopian_multiplication(10**6, 10**6) # Multiply a million by a million
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.assertLess(elapsed_time, 0.1, "Performance is unexpectedly slow for moderately large numbers.") # Check if it's less than 0.1 seconds (adjust as needed)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Set verbosity to 2 for more detailed output