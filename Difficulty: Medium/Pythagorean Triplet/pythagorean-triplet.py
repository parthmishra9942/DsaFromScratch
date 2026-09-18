class Solution:
    def pythagoreanTriplet(self, arr):
        freq = [0] * 1001

        for x in arr:
            freq[x] += 1

        for a in range(1, 1001):
            if freq[a] == 0:
                continue

            for b in range(a, 1001):
                if freq[b] == 0:
                    continue

                c2 = a * a + b * b
                c = int(c2 ** 0.5)

                if c <= 1000 and c * c == c2 and freq[c] > 0:

                    # a and b need different indexes
                    if a == b and freq[a] < 2:
                        continue

                    # c must have an index different from a/b
                    if c == a and freq[c] < 2:
                        continue

                    if c == b and freq[c] < 2:
                        continue

                    return True

        return False