# There are N coins, each showing euther heads or tails.
# We would like all the coins to form a sequence of alternationg heads and tails/
# What is the minimum number of coins that must be reversed to achieve this?


def solution(A):
    '''returns minimum number of coins 0, 1 to reverse'''
    count_from_one = 0
    count_from_zero = 0
    for i in range(0, len(A), 2):
        count_from_one += 1 - A[i]
        count_from_zero += A[i]
    for i in range(1, len(A), 2):
        count_from_one += A[i]
        count_from_zero += 1 - A[i]
    return min(count_from_one, count_from_zero)



A = [1, 0, 1, 0, 1, 1]
print(1, solution(A), A)
A = [1, 1, 0, 1, 1]
print(2, solution(A), A)
A = [0, 1, 0]
print(0, solution(A), A)
A = [0, 1, 1, 0]
print(2, solution(A), A)
A = [1, 1, 1]
print(1, solution(A), A)
A = []
print(0, solution(A), A)
A = [0]
print(0, solution(A), A)
A = [1, 0]
print(0, solution(A), A)
A = [0, 1]
print(0, solution(A), A)
A = [1, 1, 1, 1, 1, 1, 1, 1, 1]
print(4, solution(A), A)
A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(5, solution(A), A)
A = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print(4, solution(A), A)
A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(5, solution(A), A)
A = [1, 1]
print(1, solution(A), A)
A = [0, 0]
print(1, solution(A), A)
