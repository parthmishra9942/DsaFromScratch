class Solution:
    def maxLength(self, arr):
        prefix_sum = 0
        first = {}
        max_len = 0
    
        for i in range(len(arr)):
            prefix_sum += arr[i]
    
            if prefix_sum == 0:
                max_len = i + 1
    
            elif prefix_sum in first:
                max_len = max(max_len, i - first[prefix_sum])
    
            else:
                first[prefix_sum] = i
    
        return max_len