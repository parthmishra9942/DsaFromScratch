
from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)

        odd = [ch for ch in freq if freq[ch] % 2]

        if len(odd) > 1:
            return ""

        mid = odd[0] if odd else ""
        half_count = Counter({ch: freq[ch] // 2 for ch in freq})
        m = len(s) // 2
        t = target[:m]

        def make_palindrome(half):
            return half + mid + half[::-1]

        # Check whether target's first half is possible
        remaining = half_count.copy()
        possible = True

        for ch in t:
            if remaining[ch] == 0:
                possible = False
                break
            remaining[ch] -= 1

        # If the first half matches, check the complete palindrome
        if possible:
            candidate = make_palindrome(t)
            if candidate > target:
                return candidate

        # Find the smallest half strictly greater than target's half
        for i in range(m - 1, -1, -1):
            remaining = half_count.copy()
            valid = True

            for ch in t[:i]:
                if remaining[ch] == 0:
                    valid = False
                    break
                remaining[ch] -= 1

            if not valid:
                continue

            # Increase the character at position i minimally
            for ch in sorted(remaining):
                if ch > t[i] and remaining[ch] > 0:
                    remaining[ch] -= 1

                    suffix = ''.join(
                        c * remaining[c] for c in sorted(remaining)
                    )

                    half = t[:i] + ch + suffix
                    return make_palindrome(half)

        return ""
