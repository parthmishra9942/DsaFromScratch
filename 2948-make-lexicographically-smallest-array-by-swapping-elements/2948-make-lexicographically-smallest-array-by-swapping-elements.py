class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted((num, i) for i, num in enumerate(nums))
        ans = [0] * len(nums)

        i = 0
        while i < len(arr):
            j = i

            while j + 1 < len(arr) and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            group = sorted(arr[i:j + 1], key=lambda x: x[1])
            values = sorted(arr[i:j + 1])

            for k in range(len(group)):
                ans[group[k][1]] = values[k][0]

            i = j + 1

        return ans