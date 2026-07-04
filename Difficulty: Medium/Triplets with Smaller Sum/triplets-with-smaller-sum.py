class Solution:
    def countTriplets(self,target, arr):
        #code here
        arr.sort()
        n=len(arr)
        ans=0
        
        for i in range (n-2):
            left=i+1
            right=n-1
            
            while left<right:
                s=arr[i]+arr[left]+arr[right]
                
                if s>=target:
                    right-=1
                else:
                    ans+=(right-left)
                    left+=1
        return ans