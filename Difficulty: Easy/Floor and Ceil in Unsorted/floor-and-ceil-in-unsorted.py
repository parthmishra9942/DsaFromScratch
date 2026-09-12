class Solution:
    def getFloorAndCeil(self, x, arr):
        floor = -1
        ceil = -1

        for num in arr:
            # Floor: largest number <= x
            if num <= x:
                floor = max(floor, num)

            # Ceil: smallest number >= x
            if num >= x:
                if ceil == -1:
                    ceil = num
                else:
                    ceil = min(ceil, num)

        return [floor, ceil]