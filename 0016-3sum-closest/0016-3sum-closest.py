class Solution:
    def threeSumClosest(self, arr, target):
        arr.sort()
        n = len(arr)
        result_sum = arr[0] + arr[1] + arr[2]
        max_diff = float("inf")

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                diff = abs(current_sum - target)

                if diff < max_diff:
                    max_diff = diff
                    result_sum = current_sum

                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    return current_sum
        return result_sum
