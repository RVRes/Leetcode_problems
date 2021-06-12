# Given a string s, return the longest palindromic substring in s.
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
#
# Input: s = "a"
# Output: "a"
# Example 4:
#
# Input: s = "ac"
# Output: "a"
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),

def longestPalindrome(s: str) -> str:
    def get_polindrome(s: str, l: int, r: int) -> str:
        len_s = len(s)
        result = ''
        i = 0
        while l - i >= 0 and r + i < len_s and s[l - i] == s[r + i]:
            result = s[l - i:r + i + 1:]
            i += 1
        return result

    polindromes = []
    polindromes.append(s[0] if len(s) >= 1 else '')
    for l in range(len(s) - 1):
        polindromes.append(get_polindrome(s, l, l + 1))
        polindromes.append(get_polindrome(s, l, l + 2))
    return max(polindromes, key=lambda x: len(x))


def longestPalindrome2(s: str) -> str:
    len_s = len(s)
    poly_start = poly_end = 0
    for l, left_letter in enumerate(s):
        r = l + 1
        right_letter = s[r] if r < len_s else ''
        if left_letter == right_letter:
            i = 0
            while l - i >= 0 and r + i < len_s and s[l - i] == s[r + i]:
                if poly_end - poly_start < r - l + 2 * i:
                    poly_start, poly_end = l - i, r + i
                i += 1
        r = l + 2
        right_letter = s[r] if r < len_s else ''
        if left_letter == right_letter:
            i = 0
            while l - i >= 0 and r + i < len_s and s[l - i] == s[r + i]:
                if poly_end - poly_start < r - l + 2 * i:
                    poly_start, poly_end = l - i, r + i
                i += 1
    return s[poly_start:poly_end + 1:]


s = 'aaa'
print(longestPalindrome(s))
# print(longestPalindrome2(s))
