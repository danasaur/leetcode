class Solution:

    def reverse(self, x: int):
        if self.is_thirty_two_bit(x) == False:
            return 0
        else:
            x = list(str(x))

            if x[0] == '-':
                Negative = True
                x = x[1:]
            else:
                Negative = False

            reversed_x = ''

            for num in x:
                reversed_x = str(num) + reversed_x
            reversed_x = int(reversed_x)

            if Negative:
                reversed_x = reversed_x*(-1)

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
