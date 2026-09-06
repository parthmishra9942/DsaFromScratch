class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(t)

        dp = [0] * (m + 1)
        dp[0] = 1

        for i in range(len(s)):
            for j in range(m, 0, -1):
                if s[i] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]
        