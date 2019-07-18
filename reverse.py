class Solution:

    def reverse(self, x: int):

        reversed_x = []
        for num in x:
            if self.is_thirty_two_bit(num) == False:
                return 0
            else:
                reversed_x = [num] + reversed_x

        return reversed_x

    def is_thirty_two_bit(self, x: int):
        if abs(x) <= 0xffffffff:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 3]
    s.reverse(x)
