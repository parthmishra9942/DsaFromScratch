class Solution:
    def maxProduct(self, arr):
        max_prod = arr[0]
        min_prod = arr[0]
        ans = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]

            new_max = max(x, x * max_prod, x * min_prod)
            new_min = min(x, x * max_prod, x * min_prod)

            max_prod = new_max
            min_prod = new_min

            ans = max(ans, max_prod)

        return ans