class Solution(object):
    def subarraysDivByK(self, nums, k):
        n=len(nums)
        res=0
        sum_=0
        freq={0:1}

        for i in range(n):
            sum_+=nums[i]

            rem =sum_%k

            if k<0:
                rem+=k
            res+=freq.get(rem,0)
            freq[rem]=freq.get(rem,0)+1
        return res 