def twoSum(nums, target):

    for position, element in enumerate(nums):
        for position_2, element_2 in enumerate(nums):
            if position_2 > position:
                print(position)
                print(position_2)
                summation = element + element_2
                if summation == target:
                    break
        if summation == target:
            break

    return [position, position_2]

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


