class Solution(object):
    def isHappy(self, n):
        def fun(num):
            total=0
            while num>0:
                d=num%10
                num=num//10
                total+=d*d
            return total
        slow=n
        fast=n
        while(fast!=1):
            slow=fun(slow)
            fast=fun(fun(fast))

            if slow == fast and slow != 1:
                return False
        return True
       
        