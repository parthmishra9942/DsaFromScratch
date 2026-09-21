class Solution(object):
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k

            new_dp = [0] * k

            # Start a new subarray with nums[i]
            new_dp[x] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * x) % k
                    new_dp[new_r] += dp[r]

            dp = new_dp

            # Add all subarrays ending here
            for r in range(k):
                ans[r] += dp[r]

        return ans