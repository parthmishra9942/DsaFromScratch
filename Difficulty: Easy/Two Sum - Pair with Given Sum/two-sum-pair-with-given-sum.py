class Solution:
    def twoSum(self, arr, target):
        arr.sort()

        i = 0
        j = len(arr) - 1

        while i < j:
            curr_sum = arr[i] + arr[j]

            if curr_sum == target:
                return True
            elif curr_sum < target:
                i += 1
            else:
                j -= 1

        return False