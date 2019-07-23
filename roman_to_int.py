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

        romans = list(x)

        total = 0

        possible_negatives = {'I', 'X', 'C'}

        for position, element in enumerate(romans):

            if element in possible_negatives and position < len(romans) - 1:
                
                next_roman = romans[position+1]

                if element == "I":
                    if next_roman == 'V' or next_roman == 'X':
                        total += -1
                    else: 
                        total += 1

                if element == "X":
                    if next_roman == 'L' or next_roman == 'C':
                        total += -10
                    else: 
                        total += 10

                if element == "C":
                    if next_roman == 'D' or next_roman == 'M':
                        total += -100
                    else: 
                        total += 100

            else:
                total += roman_dict[element]

        return total


if __name__ == '__main__':
    s = Solution()
    x = "MCMXCIV"
    print(s.roman_to_int(x))