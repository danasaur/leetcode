# O(n) time, tradeoff for taking more space for the hashmap

from collections import defaultdict

def binary_search(nums, target, left, right):
    print("--")
    # print("nums: {0}, target: {1}, left: {2}, right: {3}".format(nums, target, left, right))

    while left <= right:

        middle = left + (right - left)//2
        # print("left: {0}, right: {1}, middle: {2}".format(left, right, middle))
        # print("target: {0}, middle_value: {1}".format(target, nums[middle]))

        # Check if x is present at mid
        print(nums[middle], middle)
        if nums[middle] == target:
            return middle

        # If x is greater, ignore left half
        elif nums[middle] < target:
            left = middle + 1

        # If x is smaller, ignore right half
        else:
            right = middle - 1

    # If we reach here, then the element
    # was not present
    return None

def twoSum(nums, target):

    # print("nums: {0}".format(nums))

    for position, element in enumerate(nums):
        complement = target - element
        left = position + 1
        right = len(nums) - 1
        complement_position = binary_search(nums, complement, left, right)
        # print("complement_position: {0}".format(complement_position))
        if complement_position:
            break

    return [position+1, complement_position+1]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print("expected result: [1, 2], result: {0}".format(result))

    nums = [0,0,3,4]
    target = 0
    result = twoSum(nums, target)
    print("expected result: [1, 2], result: {0}".format(result))

    nums = [-5,-4,-3,-2,-1]
    target = -8
    result = twoSum(nums, target)
    print("expected result: [1, 3], result: {0}".format(result))

    nums = [-18, 0, 3, 12]
    target = -6
    result = twoSum(nums, target)
    print("expected result: [1, 4], result: {0}".format(result))

    nums = [5,25,75]
    target = 100
    result = twoSum(nums, target)
    print("expected result: [2, 3], result: {0}".format(result))

    nums = [1,2,3,4,4,9,56,90]
    target = 8
    result = twoSum(nums, target)
    print("expected result: [4, 5], result: {0}".format(result))


