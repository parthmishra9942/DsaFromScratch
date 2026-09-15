class Solution:
    def find(self, arr, x):
        n = len(arr)

        # Find first occurrence
        low = 0
        high = n - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == x:
                first = mid
                high = mid - 1       # search left
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        # Find last occurrence
        low = 0
        high = n - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == x:
                last = mid
                low = mid + 1        # search right
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]