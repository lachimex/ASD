def coinChange(coins, amount):
    if amount == 0:
        return 0
    else:
        F = [amount + 2] * (amount + 1)
        F[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    F[i] = min(F[i], F[i - coin] + 1)
        return F[amount]

coins = [1, 2, 5]
print(coinChange(coins, 11))
