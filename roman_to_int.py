class Solution:

    def roman_to_int(self, x: str):
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        numbers = [roman_dict[roman] for roman in x]

        total = numbers[0]

        for i in range(1, len(numbers)):
                
            if numbers[i-1] < numbers[i]:
                total += numbers[i] - numbers[i-1]*2
            else:
                total += numbers[i]

        return total


if __name__ == '__main__':
    s = Solution()
    x = "MCMXCIV"
    print(s.roman_to_int(x))

    x = 'IX'
    print(s.roman_to_int(x))