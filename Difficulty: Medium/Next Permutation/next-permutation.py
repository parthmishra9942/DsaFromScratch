class Solution:
    def nextPermutation(self, arr):
        n = len(arr)

        # 1. Find the first decreasing element from right
        i = n - 2

        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        # 2. If found, find the next greater element
        if i >= 0:
            j = n - 1

            while arr[j] <= arr[i]:
                j -= 1

            arr[i], arr[j] = arr[j], arr[i]

        # 3. Reverse the remaining part
        left = i + 1
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1