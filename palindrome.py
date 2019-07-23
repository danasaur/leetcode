class Solution:

    def palindrome(self, x: int):
        x_elements = list(str(x))
        x_elements_reversed = x_elements[::-1]
        if x_elements == x_elements_reversed:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    x = 121
    print(s.palindrome(x))