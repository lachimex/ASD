#longest palindromic subsequence

def longestPalindrome(s):
    n = len(s)
    F = [[False] * (n) for _ in range(n)]
    for i in range(n):
        F[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            F[i][i + 1] = True
    index = 2
    for i in range(n - index):
        for j in range(n - index):
            F[i][j] = F[i+1][j-1] and s[i] == s[j]
        index += 1
    max_i = 0
    max_j = 0
    maxi = 0
    for i in range(n):
        for j in range(i + 1, n):
            if F[i][j]:
                if maxi < j - i:
                    maxi = j - i
                    max_i = i
                    max_j = j
    return s[max_i:max_j + 1]


print(longestPalindrome("aaaaa"))