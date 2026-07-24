class Solution(object):
    def maximumSum(self, arr):
        n=len(arr)
        onedelete=float('-inf')
        nodelete=arr[0]
        res=arr[0]

        for i in range(1,n):
            prevnd=nodelete
            prevod=onedelete


            nodelete=max(arr[i],prevnd+arr[i])
            onedelete=max(prevnd,prevod+arr[i])

            res=max(nodelete,res,onedelete)
        return res
        