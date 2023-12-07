def wordBreak(s, wordDict):
    n = len(s)
    F = [False] * (n + 1)
    start = 0
    F[0] = True
    while start < n:
        for word in wordDict:
            if F[start] and start + len(word) <= n and word == s[start:start + len(word)]:
                F[start + len(word)] = True
        start += 1
    return F[n]


s = "leetcode"
wordDict = ["leet","code"]

print(wordBreak(s, wordDict))