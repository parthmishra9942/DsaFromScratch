class Solution:
    def longestSubarray(self, arr, k):
        prefix = {}
        curr_sum = 0
        ans = 0

        for i in range(len(arr)):
            curr_sum += arr[i]

            if curr_sum == k:
                ans = i + 1

            if (curr_sum - k) in prefix:
                ans = max(ans, i - prefix[curr_sum - k])

            if curr_sum not in prefix:
                prefix[curr_sum] = i

        return ans