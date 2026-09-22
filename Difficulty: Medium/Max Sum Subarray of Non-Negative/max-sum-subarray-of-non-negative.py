class Solution(object):
    def findSubarray(self, arr):
        max_sum = -1
        max_len = 0
        max_start = 0

        curr_sum = 0
        curr_start = 0

        for i in range(len(arr)):

            if arr[i] >= 0:
                curr_sum += arr[i]

                curr_len = i - curr_start + 1

                if (curr_sum > max_sum or
                    (curr_sum == max_sum and curr_len > max_len)):

                    max_sum = curr_sum
                    max_len = curr_len
                    max_start = curr_start

            else:
                curr_sum = 0
                curr_start = i + 1

        if max_sum == -1:
            return [-1]

        return arr[max_start:max_start + max_len]