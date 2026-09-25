class Solution(object):
    def maxNumberOfBalloons(self, text):
        
        have = {}

        # Count characters in text
        for ch in text:
            have[ch] = have.get(ch, 0) + 1

        # Required characters
        need = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }

        res = float('inf')

        # Find how many balloons can be made
        for ch in need:
            if ch not in have:
                return 0

            times = have[ch] // need[ch]
            res = min(res, times)

        return res