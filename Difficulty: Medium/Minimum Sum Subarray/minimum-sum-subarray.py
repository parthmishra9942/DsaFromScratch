class Solution:
    def smallestSumSubarray(self, A, N):
        best = A[0]
        ans = A[0]

        for i in range(1, N):
            best = min(best + A[i], A[i])
            ans = min(ans, best)

        return ans