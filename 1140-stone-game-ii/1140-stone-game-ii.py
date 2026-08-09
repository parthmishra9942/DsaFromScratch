class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, M):
            if i >= n:
                return 0

            if (i, M) in dp:
                return dp[(i, M)]

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            for X in range(1, 2 * M + 1):
                next_M = max(M, X)

                # Total remaining - opponent's best
                current = suffix[i] - solve(i + X, next_M)

                best = max(best, current)

            dp[(i, M)] = best
            return best

        return solve(0, 1)
        