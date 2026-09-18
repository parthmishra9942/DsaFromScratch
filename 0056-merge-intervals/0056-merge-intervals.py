class Solution:
    def merge(self, intervals):
        res=[]
        n=len(intervals)
        intervals.sort()

        s1=intervals[0][0]
        e1=intervals[0][1]

        for i in range(1,n):
            s2=intervals[i][0]
            e2=intervals[i][1]

            if e1>=s2:
                e1=max(e1,e2)

            else:
                res.append([s1,e1])
                s1=s2
                e1=e2
        res.append([s1,e1])
        return res
        
