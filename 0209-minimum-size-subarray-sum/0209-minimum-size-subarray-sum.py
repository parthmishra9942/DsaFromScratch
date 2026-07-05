class Solution(object):
    def minSubArrayLen(self, target,arr):
        n=len(arr)
        high=0
        low=0
        sum_=0
        res=float('inf')

        while high<n:
            sum_+=arr[high]
            while sum_>=target:
                res=min(res,high-low+1)
                sum_ -=arr[low]
                low+=1
            high+=1
        return res if res!=float('inf') else 0
       
        