class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        i=0
        j=0
        n=len(start)
        start.sort()
        end.sort()
        res=0
        room=0
        
        while i<n and j<n:
            if start[i]<end[j]:
                i+=1
                room+=1
                res=max(res,room)
                
            else:
                j+=1
                room-=1
                
        return res
                
        
