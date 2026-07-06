class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        high=0
        low=0
        freq={}
        res=0

        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1
            k=high-low+1

            while freq[s[high]]>1:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1

            lenght=high-low+1
            res=max(res,lenght)
        return res
            


    
        