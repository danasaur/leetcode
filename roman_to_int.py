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

        roman_values = []

        possible_negatives = {'I', 'X', 'C'}

        for position, element in enumerate(romans):

            if element in possible_negatives and position < len(romans) - 1:
                
                next_roman = romans[position+1]

                if element == "I":
                    if next_roman == 'V' or next_roman == 'X':
                        roman_values.append(-1)
                    else: 
                        roman_values.append(1)

                if element == "X":
                    if next_roman == 'L' or next_roman == 'C':
                        roman_values.append(-10)
                    else: 
                        roman_values.append(10)

                if element == "C":
                    if next_roman == 'D' or next_roman == 'M':
                        roman_values.append(-100)
                    else: 
                        roman_values.append(100)

            else:
                roman_values.append(roman_dict[element])

        result = sum(roman_values)
        print(roman_values)

        return result




if __name__ == '__main__':
    s = Solution()
    x = "MCMXCIV"
    print(s.roman_to_int(x))