# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

s = "pwwkew"


def lengthOfLongestSubstring(s: str) -> int:
    max_subs_len = 0
    i = 0
    substring = ''
    len_s = len(s)
    while i < len_s:
        symbol = s[i]
        if symbol in substring:
            max_subs_len = max(max_subs_len, len(substring))
            i = s[:i:].rfind(symbol) + 1
            substring = ''
        else:
            substring += symbol
            i += 1
            if i == len_s:
                max_subs_len = max(max_subs_len, len(substring))
    return max_subs_len


def lengthOfLongestSubstring2(s: str) -> int:
    results = 0
    sub = ""
    for i in s:
        if i in sub:
            results = max(results, len(sub))
            sub =sub.split(i)[-1]
        sub += i
    return max(results, len(sub))

print(lengthOfLongestSubstring(s))
