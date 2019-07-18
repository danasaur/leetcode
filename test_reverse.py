import unittest
import reverse

class TestReverseMethod(unittest.TestCase):

    def test_reverse(self):
        x = 123
        result = reverse.Solution().reverse(x)
        expected_result = 321
        self.assertEqual(result, expected_result)

    def test_not_thirty_two_bit(self):
        x = 2**32
        result = reverse.Solution().reverse(x)
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_negative_not_thirty_two_bit(self):
        x = -2**32
        result = reverse.Solution().reverse(x)
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_negative(self):
        x = -123
        result = reverse.Solution().reverse(x)
        expected_result = -321
        self.assertEqual(result, expected_result)

    def test_negative_with_zero(self):
        x = -120
        result = reverse.Solution().reverse(x)
        expected_result = -21
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
