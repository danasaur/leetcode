import unittest
import roman_to_int

class TestRomanToIntMethod(unittest.TestCase):

    def test_simple_addition(self):
        x = 'III'
        result = roman_to_int.Solution().roman_to_int(x)
        expected_result = 3
        self.assertEqual(result, expected_result)

    def test_four(self):
        x = 'IV'
        result = roman_to_int.Solution().roman_to_int(x)
        expected_result = 4
        self.assertEqual(result, expected_result)

    def test_nine(self):
        x = 'IX'
        result = roman_to_int.Solution().roman_to_int(x)
        expected_result = 9
        self.assertEqual(result, expected_result)

    def test_longer_addition(self):
        x = 'LVIII'
        result = roman_to_int.Solution().roman_to_int(x)
        expected_result = 58
        self.assertEqual(result, expected_result)

    def test_multiple_negations(self):
        x = 'MCMXCIV'
        result = roman_to_int.Solution().roman_to_int(x)
        expected_result = 1994
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
