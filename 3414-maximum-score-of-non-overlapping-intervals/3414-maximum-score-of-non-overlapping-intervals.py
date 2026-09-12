class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # start, end, weight, original index
        arr = []

        for i in range(n):
            l, r, w = intervals[i]
            arr.append((l, r, w, i))

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # Find first interval whose start > current end
        def find_next(end):
            lo = 0
            hi = n

            while lo < hi:
                mid = (lo + hi) // 2

                if starts[mid] > end:
                    hi = mid
                else:
                    lo = mid + 1

            return lo

        # next[i] = first non-overlapping interval after i
        nxt = [0] * n

        for i in range(n):
            nxt[i] = find_next(arr[i][1])

        # dp[i][k] = best answer from i onward
        # when we can still choose at most k intervals
        dp = [[None] * 5 for _ in range(n + 1)]

        # Base case:
        # From n onward, score is 0 regardless of how many
        # intervals we are allowed to choose.
        for k in range(5):
            dp[n][k] = (0, [])

        # Also, choosing at most 0 intervals always gives 0
        for i in range(n + 1):
            dp[i][0] = (0, [])

        # Fill DP backwards
        for i in range(n - 1, -1, -1):

            l, r, w, idx = arr[i]

            for k in range(1, 5):

                # 1. Skip current interval
                skip_score, skip_indices = dp[i + 1][k]

                # 2. Take current interval
                take_score, take_indices = dp[nxt[i]][k - 1]

                take_score += w
                take_indices = [idx] + take_indices

                # Result must be sorted by original indices
                take_indices.sort()

                # Pick higher score
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)

                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)

                # Same score -> lexicographically smaller indices
                else:
                    if take_indices < skip_indices:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (skip_score, skip_indices)

        return dp[0][4][1]