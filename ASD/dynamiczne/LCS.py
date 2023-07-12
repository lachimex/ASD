#longest common substring

def LCS(s1, s2):
    n = len(s1)
    m = len(s2)
    F = [[-1] * (n + 1) for _ in range(m + 1)]
    for i in range(n+1):
        F[0][i] = 0
    for i in range(m+1):
        F[i][0] = 0
    for j in range(1, n+1):
        for i in range(1, m+1):
            if s1[j - 1] == s2[i - 1]:
                F[i][j] = 1 + F[i-1][j - 1]
            else:
                F[i][j] = max(F[i][j-1], F[i-1][j])
    return F[m][n]

print(LCS("oala", "koala"))