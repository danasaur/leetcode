class Solution:

    def reverse(self, x: int):
        if abs(x) >= 2**31:
            return 0
        else:

            if x < 0:
                Negative = True
                x = abs(x)
            else:
                Negative = False

            x = str(x)

            reversed_x = int(x[::-1])

            if Negative:
                reversed_x = reversed_x*(-1)

            if abs(reversed_x) >= 2**31:
                return 0

            return reversed_x

if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 3]
    s.reverse(x)
