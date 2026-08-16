from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()
        ans = []

        for i in range(len(arr)):

            # Remove indices outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # Window size is k
            if i >= k - 1:
                ans.append(arr[dq[0]])

        return ans