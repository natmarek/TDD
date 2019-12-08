import unittest
import CalculatorFunctions


class KnownValues(unittest.TestCase):
    def test_calculateBMI_lowerBoundary(self):
        #capture the results of the functions
        result = CalculatorFunctions.calculateBMI(58, 19)
        expected = 19
        #check for expected output
        self.assertEqual(expected, result)         #      self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
