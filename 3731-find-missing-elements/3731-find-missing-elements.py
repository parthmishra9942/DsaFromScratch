class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)

        small = min(nums)
        large = max(nums)

        ans = []

        for i in range(small, large + 1):
            if i not in s:
                ans.append(i)

        return ans