def minCoins(amount, coins=[1, 3, 5]):
    """function calculates minimum number of coins required to arrive at the total."""
    INF = 999999
    table = [0 if i == 0 else INF for i in range(amount + 1)]
    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if sub_res != INF and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1
    return table[amount] if table[amount] != INF else False


# coins = [1, 3, 5]
# m = len(coins)
# V = 11
print("Minimum coins required is ",
      minCoins(20))

print("Minimum coins required is ",
      minCoins(11))
print("Minimum coins required is ",
      minCoins(4))
print("Minimum coins required is ",
      minCoins(5))


# ==============
B = [1, 50, 90]
S = 100
inf = 10 ** 6
F = [0] + [inf] * S
Prev = [-1] * (S + 1)
for i in range(1, S + 1):
    for j in range(len(B)):
        if i - B[j] >= 0 and F[i - B[j]] < F[i]:
            F[i] = F[i - B[j]]
            Prev[i] = B[j]
    F[i] += 1
Ans = []
while S > 0:
    Ans.append(Prev[S])
    S -= Prev[S]
print(Ans)
