from bisect import bisect_left, bisect_right

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        m = len(digits)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix hash and prefix digit sum
        prefHash = [0] * (m + 1)
        prefSum = [0] * (m + 1)

        for i in range(m):
            prefHash[i + 1] = (prefHash[i] * 10 + digits[i]) % MOD
            prefSum[i + 1] = prefSum[i] + digits[i]

        ans = []

        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r) - 1

            if L > R:
                ans.append(0)
                continue

            length = R - L + 1

            x = (prefHash[R + 1] - prefHash[L] * pow10[length]) % MOD
            x %= MOD

            sm = prefSum[R + 1] - prefSum[L]

            ans.append((x * sm) % MOD)

        return ans