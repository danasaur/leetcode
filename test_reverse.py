import unittest
import reverse

class TestReverseMethod(unittest.TestCase):

    def test_reverse(self):
        x = [1, 2, 3]
        result = reverse.Solution().reverse(x)
        expected_result = [3, 2, 1]
        self.assertEqual(result, expected_result)

    def test_not_thirty_two_bit(self):
        x = [2**32, 2, 3]
        result = reverse.Solution().reverse(x)
        expected_result = 0
        self.assertEqual(result, expected_result)
"""
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
"""
if __name__ == '__main__':
    unittest.main()
