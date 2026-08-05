class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        
        def count(k):
            left = 0
            curr_sum = 0
            ans = 0

            for right in range(len(arr)):
                curr_sum += arr[right]

                while curr_sum > k:
                    curr_sum -= arr[left]
                    left += 1

                ans += (right - left + 1)

            return ans

        return count(r) - count(l - 1)