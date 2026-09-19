class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        res=[]
        n=len(firstList)
        m=len(secondList)
        i=0
        j=0

        while i<n and j<m:
            s1=firstList[i][0]
            e1=firstList[i][1]
            s2=secondList[j][0]
            e2=secondList[j][1]

            s=max(s1,s2)
            e=min(e1,e2)

            if s<=e:
                res.append([s,e])
            if e1<=e2:
                i+=1
            else:
                j+=1
        return res



        