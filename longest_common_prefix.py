# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters

import os.path


def longestCommonPrefix(strs):
    i = 0
    min_len = min([len(stri) for stri in strs])
    while i < min_len:
        if all([stri[i] == strs[0][i] for stri in strs]):
            i += 1
        else:
            break
    return strs[0][:i]


def longestCommonPrefix2(strs: list) -> str:
    return os.path.commonprefix(strs)


def longestCommonPrefix3(strs: list) -> str:
    pref_letters = [''.join(i) for i in map(set, zip(*strs))]
    if not pref_letters or len(pref_letters[0]) > 1:
        return ''
    i = 1
    while i < len(pref_letters) and len(pref_letters[i]) == 1:
        i += 1
    return ''.join(pref_letters[:i:])
