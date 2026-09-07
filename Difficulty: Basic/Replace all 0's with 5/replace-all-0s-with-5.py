class Solution:
    def convertFive(self, n):
        if n == 0:
            return 5

        result = 0
        place = 1

        while n > 0:
            digit = n % 10

            if digit == 0:
                digit = 5

            result += digit * place
            place *= 10
            n //= 10

        return result