from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_max = float('-inf')

            for start in range(0, n, k):
                end = start + k
                block = nums[start:end]

                # Blocks must be ordered relative to each other.
                if prev_max > min(block):
                    valid = False
                    break

                # A cyclically sorted block has at most one
                # strict descent, including the circular boundary.
                descents = 0

                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        descents += 1

                if descents > 1:
                    valid = False
                    break

                prev_max = max(block)

            if valid:
                ans += k

        return ans