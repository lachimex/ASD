from zad5ktesty import runtests

def garek ( T ):
    n = len(T)
    dp = [[(-1, -1)] * n for _ in range(n)]

    def f(T, a, b):
        if dp[a][b] != (-1, -1):
            return dp[a][b]

        if a == b:
            return T[a], 0

        if a + 1 == b or a == b - 1:
            return max(T[a], T[b]), min(T[a], T[b])

        x = f(T, a + 1, b)[1]
        y = f(T, a, b - 1)[1]

        if T[a] + x > T[b] + y:
            dp[a][b] = (T[a] + x, f(T, a + 1, b)[0])
        else:
            dp[a][b] = (T[b] + y, f(T, a, b - 1)[0])
        return dp[a][b]

    return f(T, 0, len(T) - 1)[0]

runtests ( garek )