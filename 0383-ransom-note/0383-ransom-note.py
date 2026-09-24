class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        need={}
        have={}

        for ch in ransomNote:
            need[ch]=need.get(ch,0)+1

        for ch in magazine:
            have[ch]=have.get(ch,0)+1

        for ch in need:
            if have.get(ch,0)<need[ch]:
                return False
        return True
        
        