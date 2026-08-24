class Solution:
    def segregateElements(self, arr):
        temp = []
    
        # Positive elements
        for x in arr:
            if x >= 0:
                temp.append(x)
    
        # Negative elements
        for x in arr:
            if x < 0:
                temp.append(x)
    
        # Copy back into original array
        for i in range(len(arr)):
            arr[i] = temp[i]