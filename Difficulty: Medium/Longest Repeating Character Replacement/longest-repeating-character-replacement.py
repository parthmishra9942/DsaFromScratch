class Solution:
    def longestSubstr(self, s, k):
        # Code here
        n=len(s)
        high=0
        low=0
        freq={}
        max_count=0
        res=float('-inf')
        
        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1
            max_count=max(max_count,freq[s[high]])
            
            lenght=high-low+1
            diff=lenght-max_count
            
            while diff>k:
                freq[s[low]]-=1
                low+=1
                
                lenght=high-low+1
                diff=lenght-max_count
            
            lenght=high-low+1
            res=max(res,lenght)
        return res
            
            