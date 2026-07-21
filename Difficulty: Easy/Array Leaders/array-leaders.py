class Solution:
    def leaders(self, arr):
        ans = []
        max_right = float('-inf')

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= max_right:
                ans.append(arr[i])
                max_right = arr[i]

        return ans[::-1]