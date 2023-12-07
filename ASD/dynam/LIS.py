#longest increasing subsequence

def LIS(nums):
    n = len(nums)
    F = [1] * n
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                F[i] = max(F[i], 1 + F[j])
    return max(F)


T = [10,9,2,5,3,7,101,18]
print(LIS(T))