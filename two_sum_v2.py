# O(n) time, tradeoff for taking more space for the hashmap

from collections import defaultdict

def twoSum(nums, target):

    position_dict = {}
    for position, element in enumerate(nums):
        complement = target - element
        if complement in position_dict.keys() and position_dict[complement] != position:
            position_2 = position_dict[complement]
            break
        position_dict[element] = position

    return [position_2, position]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)

    nums = [0,4,3,0]
    target = 0
    result = twoSum(nums, target)
    print(result)

    nums = [-1,-2,-3,-4,-5]
    target = -8
    result = twoSum(nums, target)
    print(result)

    nums = [-18,12,3,0]
    target = -6
    result = twoSum(nums, target)
    print(result)

    nums = [3,2,4]
    target = 6
    result = twoSum(nums, target)
    print(result)


