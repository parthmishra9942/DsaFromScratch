class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n=len(arr)
        low=0
        high=k-1
        
        sum_=0
        res=0
        
        for i in range(low,high+1):
            sum_+=arr[i]
            
        while high<n:
            res=max(res,sum_)
            high+=1
            low+=1
                
            if high ==n:
                break
                
            sum_=sum_- arr[low-1] + arr[high]
            
            
        return res
                