import unittest
import palindrome

class TestPalindromeMethod(unittest.TestCase):

    def test_true(self):
        x = 121
        result = palindrome.Solution().palindrome(x)
        expected_result = True
        self.assertEqual(result, expected_result)

    def test_negative(self):
        x = -121
        result = palindrome.Solution().palindrome(x)
        expected_result = False
        self.assertEqual(result, expected_result)

    def test_zero_at_end(self):
        x = 10
        result = palindrome.Solution().palindrome(x)
        expected_result = False
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
