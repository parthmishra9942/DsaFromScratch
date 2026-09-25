class Solution(object):
    def longestPalindrome(self, s):
        freq = {}

        # Count frequency of every character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        odd = False
        res = 0

        # Use pairs of characters
        for ch in freq:
            val = freq[ch]

            if val % 2 == 0:
                res += val
            else:
                odd = True
                res += val - 1

        # One odd character can be placed in the middle
        if odd:
            res += 1

        return res