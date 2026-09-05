class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # right[i] = minimum value from i to n-1
        right = [0] * n
        curr_min = float('inf')

        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            right[i] = curr_min

        # curr_max = maximum value from 0 to i
        curr_max = float('-inf')

        for i in range(n):
            curr_max = max(curr_max, nums[i])

            if curr_max - right[i] <= k:
                return i

        return -1