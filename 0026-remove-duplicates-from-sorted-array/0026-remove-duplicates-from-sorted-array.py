class Solution:
    def removeDuplicates(self,arr):
        n=len(arr)
        cm=1
        res=1
        officer=0

        while cm<n:
            if arr[cm] == arr[cm-1]:
                cm+=1
                continue
            officer+=1
            arr[officer]=arr[cm]
            res+=1
            cm+=1
        return res


        