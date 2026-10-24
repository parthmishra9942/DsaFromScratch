from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_letters = Counter(c.lower() for c in licensePlate if c.isalpha())

        answer = ""

        for word in words:
            word_count = Counter(word)

            if all(word_count[c] >= license_letters[c] for c in license_letters):
                if answer == "" or len(word) < len(answer):
                    answer = word

        return answer