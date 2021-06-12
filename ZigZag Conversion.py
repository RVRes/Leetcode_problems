# ZigZag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);

# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
#
# Input: s = "A", numRows = 1
# Output: "A"

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

def convert(s: str, numRows: int) -> str:
    if numRows < 2:
        return s
    len_s = len(s)
    step = numRows * 2 - 2
    print(step)
    print([i for i in range(0, len_s, step)])
    result = ''.join([s[i] for i in range(0, len_s, step)])
    for j in range(1, step // 2):
        result = result + ''.join([(s[i - 2 * j] if 0 <= i - 2 * j < len_s else '')
                                   + (s[i] if i < len_s else '') for i in range(j, len_s + step, step)])
    result = result + ''.join([s[i] for i in range(numRows - 1, len_s, step)])
    return result


def convert2(s: str, numRows: int) -> str:
    if numRows == 1: return s
    ans = ["" for _ in range(numRows)]
    n = len(s)
    for i in range(n):
        m = i % (2 * numRows - 2)
        if m < numRows:
            ans[m] += s[i]
        else:
            ans[numRows - m - 2] += s[i]
    return ''.join(ans)


s = "PAYPALISHIRING"
numRows = 3
print(s)
print(convert(s, numRows))
print("PAHNAPLSIIGYIR")
print('')

s = "PAYPALISHIRING"
numRows = 4
print(s)
print(convert(s, numRows))
print("PINALSIGYAHRPI")
print('')

s = "ABCDEFGH"
numRows = 2
print('')
print(s)
print(convert(s, numRows))
print('ACEGBDFH')
print('')

s = "ABCDEFGH"
numRows = 3
print('')
print(s)
print(convert(s, numRows))
print('AEBDFHCG')
print('')

s = "ABCDEFGHIJKLMNO"
numRows = 4
print('')
print(s)
print(convert(s, numRows))
print('AGMBFHLNCEIKODJ')
print('')

s = "ABCDEFGHIJKLMNO"
numRows = 4
print('')
print(s)
print(convert2(s, numRows))
print('AGMBFHLNCEIKODJ')
print('')