import unittest
from math_quiz import random_integer, random_operator, result


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random integers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_int = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_int <= max_val)

    def test_random_operator(self):
         # Test if the operator generated is one of '+', '-', or '*'
        for _ in range(1000):  
            operator = random_operator()
            self.assertIn(operator, ['+', '-', '*'])

    def test_result(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), # addition
                (5, 2, '-', '5 - 2', 3),  # subtraction
                (5, 2, '*', '5 * 2', 10),  # multiplication
                (5, 0, '*', '5 * 0', 0),  # multiplication with zero
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, calculated_result = result(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(calculated_result, expected_answer)

if __name__ == "__main__":
    unittest.main()
