# Find All Combination of Numbers Sum to Target / Shopping Options
# Alternative Question: Find All Combination of Numbers Sum to Target
#
# Given a positive integer, target, print all possible combinations
# of positive integers that sum up to the target number.
# For example, if we are given input ‘5’, these are the possible sum combinations.
#
# 1, 4
# 2, 3
# 1, 1, 3
# 1, 2, 2
# 1, 1, 1, 2
# 1, 1, 1, 1, 1
# The output will be in the form a list of lists or an array of arrays.
# Each element in the list will be another list containing a possible sum combination.
#
# Hint: Recursion, Two lists

from _tasks_runner import execute
import copy


def find_all_combinations_to_sum_1(target: int) -> list:
    if target <= 1:
        return []
    result = [[target - 1, 1]]
    for item in result:
        for idx, element in enumerate(item):
            for i in range(1, element):
                new_item = sorted((*item[:idx], element - i, i,
                                   *(item[idx + 1:] if idx <= len(item) + 1 else ())), reverse=True)
                if new_item not in result:
                    result.append(new_item)
                if idx < len(item) - 1:
                    new_item = sorted((*item[:idx], element - i, item[idx + 1] + i,
                                       *(item[idx + 2:] if idx <= len(item) + 2 else ())), reverse=True)
                    if new_item not in result:
                        result.append(new_item)
    return result


def find_all_combinations_to_sum_2(target):
    def print_all_sum_rec(target, current_sum, start, output, result):
        if current_sum == target:
            output.append(copy.copy(result))
        for i in range(start, target):
            temp_sum = current_sum + i
            if temp_sum <= target:
                result.append(i)
                print_all_sum_rec(target, temp_sum, i, output, result)
                result.pop()
            else:
                return

    output = []
    result = []
    print_all_sum_rec(target, 0, 1, output, result)
    return output


# [(args for solution function): tuple | list, reference value: Any | None]
TESTS = [
    [(5,), [[1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]],
    [(1,), []],
    [(2,), [[1, 1]]],
    [(3,), [[1, 2], [1, 1, 1]]],
    [(4,), [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]],
    [(28,), None],
    [(31,), None],
    [(60,), None],
]

for i, test in enumerate(TESTS):
    print(f'Test {i}, splitting:{(test[0][0])}:')
    execute(find_all_combinations_to_sum_2, test[0], test[1], is_reference=True)
    execute(find_all_combinations_to_sum_1, test[0], test[1], include_func=lambda x: x[0] < 33)
