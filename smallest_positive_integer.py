# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


def solution(A):
    if not A:
        return 1
    max_el = max(A)
    if max_el < 0:
        return 1
    res = {}
    for i in range(len(A)):
        res[A[i]] = 1
    for i in range(1, max(A)):
        if i not in res:
            return i
    return max_el + 1


def solution2(A):
    if not A:
        return 1
    max_el = max(A)
    if max_el < 0:
        return 1
    for i in range(1, max(A)):
        if i not in A:
            return i
    return max_el + 1


def solution3(nums: list) -> int:
    n = len(nums)
    for i in range(n):
        correctPos = nums[i] - 1  # number 3 goes to index 2
        while 1 <= nums[i] <= n and nums[i] != nums[correctPos]:
            nums[i], nums[correctPos] = nums[correctPos], nums[i]
            correctPos = nums[i] - 1  # now nums[i] has changed

    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1
    return n + 1


def solution4(nums: list) -> int:
    i = len(nums) - 2
    nums = list(sorted(set(nums)))
    try:
        nums = nums[nums.index(1)::]
    except:
        return 1

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1
    return i + 2


def solution5(nums: list) -> int:
    n = len(nums)
    # [1, n]
    for i, num in enumerate(nums):
        if num == i + 1:
            continue
        elif num > n or num <= 0:
            continue
        else:
            while 1 <= num <= n:
                t_pos = num - 1
                if nums[t_pos] == num:
                    break
                num, nums[t_pos] = nums[t_pos], num
    for i, num in enumerate(nums):
        if num != i + 1:
            return i + 1
    return len(nums) + 1


test_cases = {
    1: (5, [1, 3, 6, 4, 1, 2]),
    2: (4, [1, 2, 3]),
    3: (1, [-1, -3]),
    4: (1, [-1]),
    5: (1, [0]),
    6: (2, [1]),
    7: (4, [1, -1, -3, 0, 2, 3]),
    8: (3, [1, 2, 0]),
    9: (2, [1, 1000]),
    10: (2, [3, 4, -1, 1])
}
for test_num, arg in test_cases.items():
    print()
    print('TEST', test_num, arg[1])
    print(f'solution = {solution(arg[1])}, {arg[0]}, {"pass" if solution(arg[1]) == arg[0] else "ERROR"}')
    print(f'solution2 = {solution2(arg[1])}, {arg[0]}, {"pass" if solution(arg[1]) == arg[0] else "ERROR"}')
    print(f'solution3 = {solution3(arg[1])}, {arg[0]}, {"pass" if solution(arg[1]) == arg[0] else "ERROR"}')
    print(f'solution4 = {solution4(arg[1])}, {arg[0]}, {"pass" if solution(arg[1]) == arg[0] else "ERROR"}')
    print(f'solution5 = {solution5(arg[1])}, {arg[0]}, {"pass" if solution(arg[1]) == arg[0] else "ERROR"}')
