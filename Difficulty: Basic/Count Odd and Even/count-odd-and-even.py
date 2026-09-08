class Solution:
    def countOddEven(self, arr):
        odd = 0
        even = 0

        for x in arr:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1

        return [odd, even]