class Solution(object):
    def maxSubarraySumCircular(self, nums):
        def max_kk(arr):
            best=curr=arr[0]

            for x in arr[1:]:
                curr=max(curr+x,x)
                best=max(curr,best)
            return best

        def min_k(arr):
            best=curr=arr[0]

            for x in arr[1:]:
                curr=min(curr+x,x)
                best=min(curr,best)

            return best

        total=sum(nums)
        case1=max_kk(nums)
        min_sum=min_k(nums)
        case2=total-min_sum


        if case1<0:
            return case1
        return max(case1,case2)


       
        