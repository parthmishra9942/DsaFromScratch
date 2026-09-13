class Solution:
    def minAnd2ndMin(self, arr):
        smallest = float('inf')
        second = float('inf')

        for x in arr:
            if x < smallest:
                second = smallest
                smallest = x
            elif smallest < x < second:
                second = x

        if second == float('inf'):
            return [-1]

        return [smallest, second]