class Solution(object):
    def maxAbsoluteSum(self, nums):
        maxs = 0
        mins = 0
        res = 0

        for x in nums:
            maxs = max(maxs + x, x)
            mins = min(mins + x, x)

            res = max(res, abs(maxs), abs(mins))

        return res
