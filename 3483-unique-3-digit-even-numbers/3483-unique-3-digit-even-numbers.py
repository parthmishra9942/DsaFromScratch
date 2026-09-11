class Solution:
    def totalNumbers(self, digits):
        count = 0

        for i in range(100, 1000):

            # number must be even
            if i % 2 != 0:
                continue

            temp = list(digits)
            possible = True

            for d in str(i):
                if int(d) in temp:
                    temp.remove(int(d))
                else:
                    possible = False
                    break

            if possible:
                count += 1

        return count