class Solution:
    def removeDuplicates(self, s, k):
        st = []

        for ch in s:

            if not st:
                st.append([ch, 1])
                continue

            if st[-1][0] != ch:
                st.append([ch, 1])
                continue

            if st[-1][1] == k - 1:
                st.pop()
                continue

            st[-1][1] += 1

        res = ""

        while st:
            pair = st.pop()

            while pair[1] > 0:
                res += pair[0]
                pair[1] -= 1

        return res[::-1]