class Solution:
    def threeSum(self,arr):
        arr.sort()
        n=len(arr)
        result=[]

        for i in range (n-2):
            if i>0 and arr[i]==arr[i-1]:
                continue
            left=i+1
            right=n-1
            target=-arr[i]

            while(left<right):
                s=arr[left]+arr[right]
                if s==target:
                    result.append([arr[i],arr[left],arr[right]])
                    right-=1
                    left+=1

                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                    while left<right and arr[right]==arr[right+1]:
                        right-=1
                elif s>target:
                    right-=1
                else:
                    left+=1
        return result


        