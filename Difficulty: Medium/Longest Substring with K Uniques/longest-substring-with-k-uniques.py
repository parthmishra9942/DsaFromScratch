class Solution:
    def longestKSubstr(self, s, k):
        # code here
        n=len(s)
        high=0
        low=0
        freq={}
        res=-1
        
        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1
            
            while len(freq)>k:
                freq[s[low]]-=1
                
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
            if len(freq)==k:
                lenght=high-low+1
                res=max(res,lenght)
        return res
        