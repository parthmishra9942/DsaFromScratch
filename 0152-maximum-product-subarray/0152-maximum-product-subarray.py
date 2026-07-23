class Solution(object):
    def maxProduct(self, nums):
        maxx=nums[0]
        minn=nums[0]
        res=nums[0]


        for i in range(1,len(nums)):
            v1=nums[i]
            v2=maxx*nums[i]
            v3=minn*nums[i]

            maxx=max(v1,v2,v3)
            minn=min(v1,v2,v3)

            res=max(res,maxx)


        return res
       
        