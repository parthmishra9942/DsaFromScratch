class Solution:
    def isPalinArray(self, arr):
        for x in arr:
            if str(x) != str(x)[::-1]:
                return False
        return True
         # code here
         