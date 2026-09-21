class Solution(object):
    def removeDuplicates(self, s):
        st = []

        for i in range(len(s)):
            if len(st) != 0 and st[-1] == s[i]:
                st.pop()
                continue

            st.append(s[i])

        return "".join(st)