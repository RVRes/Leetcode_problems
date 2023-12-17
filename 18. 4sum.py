# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
#
# Example
# 1:
#
# Input: nums = [1, 0, -1, 0, -2, 2], target = 0
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
# Example
# 2:
#
# Input: nums = [2, 2, 2, 2, 2], target = 8
# Output: [[2, 2, 2, 2]]
#
# Constraints:
#
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

from random import randint
from _tasks_runner import execute


def four_sum_1(nums: list, target: int) -> list:
    """Two pointers  + set (instead of looping)"""
    len_nums = len(nums)
    if len_nums < 4:
        return []
    nums.sort()
    result = set()
    for a in range(len_nums - 3):
        if a > 0 and nums[a - 1] == nums[a]:
            continue
        for b in range(a + 1, len_nums - 2):
            if b > a + 1 and nums[b - 1] == nums[b]:
                continue
            to_target = target - nums[a] - nums[b]
            c, d = b + 1, len_nums - 1
            while c < d:
                if nums[c] + nums[d] < to_target:
                    c += 1
                elif nums[c] + nums[d] > to_target:
                    d -= 1
                else:
                    result.add((nums[a], nums[b], nums[c], nums[d]))
                    c += 1
                    d -= 1
    return list(result)


def four_sum_2(nums: list, target: int) -> list:
    """Two pointers"""
    len_nums = len(nums)
    if len_nums < 4:
        return []
    nums.sort()
    result = []
    for a in range(len_nums - 3):
        if a > 0 and nums[a - 1] == nums[a]:
            continue
        for b in range(a + 1, len_nums - 2):
            if b > a + 1 and nums[b - 1] == nums[b]:
                continue
            to_target = target - nums[a] - nums[b]
            c, d = b + 1, len_nums - 1
            while c < d:
                if nums[c] + nums[d] < to_target:
                    c += 1
                    while nums[c - 1] == nums[c] and c < d:
                        c += 1
                elif nums[c] + nums[d] > to_target:
                    d -= 1
                    while nums[d + 1] == nums[d] and c < d:
                        d -= 1
                else:
                    result.append([nums[a], nums[b], nums[c], nums[d]])
                    c += 1
                    while nums[c - 1] == nums[c] and c < d:
                        c += 1
                    d -= 1
                    while nums[d + 1] == nums[d] and c < d:
                        d -= 1
    return result


tests = [
    [([], 0), []],
    [([0], 8), []],
    [([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]],
    [([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]]],
    [([-3, -2, -1, 0, 0, 1, 2, 3], 0),
     [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2],
      [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]],
    [([randint(-99999, 99999) for _ in range(700)], 0), []],
]
for i, test in enumerate(tests):
    print(f'Test {i}, length {len(test[0][0])}:')
    execute(four_sum_1, test[0], test[1], is_reference=True)
    execute(four_sum_2, test[0], test[1])
