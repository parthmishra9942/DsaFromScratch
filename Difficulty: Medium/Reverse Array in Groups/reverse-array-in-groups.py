class Solution:

    def reverseInGroups(self, arr, k):
        """code here"""
        n = len(arr)

        for i in range(0, n, k):
            l = i
            r = min(i + k - 1, n - 1)

            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
