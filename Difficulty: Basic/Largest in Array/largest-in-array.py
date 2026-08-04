class Solution:
    def largest(self, arr):
        # code here
        n=len(arr)
        larg=arr[0]
        
        for x in arr:
            if x>larg:
                larg=x
                
        return larg
