class Solution:
    def nthRowOfPascalTriangle(self, n):
        ans = [1]

        for i in range(1, n):
            ans.append(ans[-1] * (n - i) // i)

        return ans