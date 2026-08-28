class Solution:
    def rearrange(self, arr):
        pos = []
        neg = []
    
        for x in arr:
            if x >= 0:
                pos.append(x)
            else:
                neg.append(x)
    
        i = 0
        j = 0
        k = 0
    
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]
            i += 1
            k += 1
    
            arr[k] = neg[j]
            j += 1
            k += 1
    
        while i < len(pos):
            arr[k] = pos[i]
            i += 1
            k += 1
    
        while j < len(neg):
            arr[k] = neg[j]
            j += 1
            k += 1