
class Solution:
    def rearrange(self, arr):
        arr.sort()

        n = len(arr)
        left = 0
        right = n - 1
        max_elem = arr[-1] + 1

        for i in range(n):
            if i % 2 == 0:
                arr[i] += (arr[right] % max_elem) * max_elem
                right -= 1
            else:
                arr[i] += (arr[left] % max_elem) * max_elem
                left += 1

        # Decode the new values
        for i in range(n):
            arr[i] //= max_elem

