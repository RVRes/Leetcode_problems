# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example
# 1:
#
# Input: x = 123
# Output: 321
# Example
# 2:
#
# Input: x = -123
# Output: -321
# Example
# 3:
#
# Input: x = 120
# Output: 21
# Example
# 4:
#
# Input: x = 0
# Output: 0
#
# Constraints:
#
# -231 <= x <= 231 - 1

def reverse(x: int) -> int:
    sx = '-' + str(x)[:0:-1] if x < 0 else str(x)[::-1]
    try:
        result = int(sx)
    except:
        result = 0
    return result if -2147483648 < result <= 2147483647 else 0



print(1534236469, reverse(1534236469))
print(-2, reverse(-2))
print(-23, reverse(-23))
print(-1234567890, reverse(-1234567890))
