#
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
#
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
#
# Example
# 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10 / 3 = truncate(3.33333..) = 3.
# Example
# 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7 / -3 = truncate(-2.33333..) = -2.
# Example
# 3:
#
# Input: dividend = 0, divisor = 1
# Output: 0
# Example
# 4:
#
# Input: dividend = 1, divisor = 1
# Output: 1

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 2 ** 31 - 1
        if abs(dividend) < abs(divisor):
            return 0
        sign = '' if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else '-'
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 1:
            return int(sign + str(dividend))
        if dividend < divisor + divisor:
            return int(sign + '1')
        sum_divisor = divisor
        result = 1
        while True:
            deltares = 1
            delta = divisor
            while True:
                if dividend < sum_divisor + delta:
                    break
                sum_divisor += delta
                delta += delta
                result += deltares
                deltares += deltares
                if sum_divisor + divisor > dividend or dividend == sum_divisor:
                    return int(sign + str(result)) if result < 2147483648 else 2147483647


s = Solution()
print(s.divide(2147483647, 1), 2147483647)
print(s.divide(10, 3), 3)
print(s.divide(10, 2), 5)
print(s.divide(100, 4), 25)
print(s.divide(1, 1), 1)
print(s.divide(0, 1), 0)
print(s.divide(0, 100), 0)
print(s.divide(7, 8), 0)
print(s.divide(-7, 8), 0)
print(s.divide(-10, 8), -1)
print(s.divide(-100, 10), -10)
print(s.divide(-100, 9), -11)