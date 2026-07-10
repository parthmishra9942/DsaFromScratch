class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        s = set()

        for i in range(len(arr)):
            if arr[i] in s:
                return True

            s.add(arr[i])

            if i >= k:
                s.remove(arr[i - k])

        return False