class Solution:
    def preGreaterEle(self, arr):
        n = len(arr)
        stack = []
        res = [-1] * n

        stack.append(arr[0])

        for i in range(1, n):
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if not stack:
                res[i] = -1
            else:
                res[i] = stack[-1]

            stack.append(arr[i])

        return res