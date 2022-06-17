# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
# •	2 <= nums.length <= 104
# •	-109 <= nums[i] <= 109
# •	-109 <= target <= 109
# •	Only one valid answer exists.
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

from itertools import combinations


def two_sum(nums: list, target: int):
    addnums = [target - num for num in nums]
    addnum_index = [ind for ind, addnum in enumerate(addnums) if addnum in nums and ind != nums.index(addnum)][0]
    return nums.index(addnums[addnum_index]), addnum_index


def two_sum2(nums: list, target: int) -> list:
    '''hash_map'''
    hash_map = {}
    for k, v in enumerate(nums):
        diff = target - v
        if diff in hash_map:
            return [hash_map[diff], k]
        hash_map[v] = k


def two_sum3(nums: list, target: int):
    hash_map = {}
    for key, value in enumerate(nums):
        diff = target - value
        if value in hash_map:
            return hash_map[value], key
        hash_map[diff] = key
    return False


def get_all_combinations(arr, qty, tgt):
    return [tuple(arr.index(num) for num in nums) for nums in filter(lambda x: sum(x) == tgt, combinations(arr, qty))]


tests = [
    [1, 3, -2, 5, 0, 2, 7, 10],
    [2, 1],
]

numbers_qty_ = 2
target = 3

for test in tests:
    print(f'{test}, two_sum: {two_sum(test, target)}')
    print(f'{test}, two_sum2: {two_sum2(test, target)}')
    print(f'{test}, two_sum3: {two_sum3(test, target)}')
    print(f'{test}, get_all_combinations: {get_all_combinations(test, numbers_qty_, target)}')
    print()

