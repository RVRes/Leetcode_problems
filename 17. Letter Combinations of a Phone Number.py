# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
#
# 1: '', 2: 'abc', 3: 'def'
# 4: 'ghi', 5: 'jkl', 6: 'mno'
# 7: 'pqrs', 8:'tuv', 9: 'wxyz'
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List
from _tasks_runner import execute
from itertools import product


def letter_combinations_1(digits: str) -> List[str]:
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    return [] if not digits else list(map(''.join, product(*[mapping[digit] for digit in digits])))


def letter_combinations_2(digits: str) -> List[str]:
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    if not digits:
        return []
    letters = [mapping[digit] for digit in digits]
    result = ['']
    for letter in letters:
        result = [x + y for x in result for y in letter]
    return result


def letter_combinations_3(digits: str) -> List[str]:
    if not digits:
        return []

    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    ans = []

    def rec(index, prefix):
        if index >= len(digits):
            ans.append(''.join(prefix))
            return

        for c in d[digits[index]]:
            prefix.append(c)
            rec(index + 1, prefix)
            prefix.pop()

    rec(0, [])
    return ans


TESTS = [
    [('23',), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
    [('',), []],
    [('2',), ["a", "b", "c"]],
    [('456',), None],
    [('9847',), None]
]

for i, test in enumerate(TESTS):
    print(f'Test {i}: ')
    execute(letter_combinations_1, test[0], test[1], is_reference=True)
    execute(letter_combinations_2, test[0], test[1])
    execute(letter_combinations_3, test[0], test[1])
