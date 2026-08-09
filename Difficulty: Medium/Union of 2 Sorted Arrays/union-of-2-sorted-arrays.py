class Solution:
    def findUnion(self, a, b):
        i = 0
        j = 0
        res = []

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1

            elif a[i] > b[j]:
                if not res or res[-1] != b[j]:
                    res.append(b[j])
                j += 1

            else:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1

        # Remaining elements of a
        while i < len(a):
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1

        # Remaining elements of b
        while j < len(b):
            if not res or res[-1] != b[j]:
                res.append(b[j])
            j += 1

        return res