class Solution(object):
    def insert(self, intervals, newInterval):
        res=[]
        n=len(intervals)

        s1=newInterval[0]
        e1=newInterval[1]

        for i in range(n):
            s2=intervals[i][0]
            e2=intervals[i][1]

            if s1>e2:
                res.append([s2,e2])
            elif s2>e1:
                res.append([s1,e1])
                res.extend(intervals[i:])
                return res
            else:
                s1=min(s1,s2)
                e1=max(e1,e2)
        res.append([s1,e1])
        return res
        