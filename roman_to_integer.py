# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
#
# Input: s = "III"
# Output: 3
# Example 2:
#
# Input: s = "IV"
# Output: 4
# Example 3:
#
# Input: s = "IX"
# Output: 9
# Example 4:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
# Constraints:
#
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
def romanToInt(s: str) -> int:
    roman_to_int = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                    'V': 5, 'IV': 4, 'I': 1}

    result = 0
    while s:
        if len(s) >= 2 and s[:2:] in roman_to_int:
            result += roman_to_int[s[:2:]]
            s = s[2::]
            continue
        if len(s) >= 1 and s[0] in roman_to_int:
            result += roman_to_int[s[0]]
            s = s[1::]
    return result


num = 3
st = "III"
print(num, st, romanToInt(st))

num = 4
st = "IV"
print(num, st, romanToInt(st))

num = 9
st = "IX"
print(num, st, romanToInt(st))

num = 58
st = "LVIII"
print(num, st, romanToInt(st))

num = 1994
st = "MCMXCIV"
print(num, st, romanToInt(st))
