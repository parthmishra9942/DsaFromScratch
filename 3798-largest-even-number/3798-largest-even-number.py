class Solution:
    def largestEven(self, s):
        i = s.rfind('2')

        if i == -1:
            return ""

        return s[:i + 1]