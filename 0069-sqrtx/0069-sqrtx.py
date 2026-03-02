class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        ans = 0 
        l = 1
        r = x//2
        while l<=r:
            m=(l+r)//2
            square = m*m
            if square == x:
                return m
            elif square<x:
                ans = m
                l=m+1
            else:
                r=m-1
        return ans  


        