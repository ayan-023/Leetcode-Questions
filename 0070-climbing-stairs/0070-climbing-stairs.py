class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        prev0=1
        prev1=2

        for i in range(3,n+1):
            dp = prev0+prev1
            prev0=prev1
            prev1=dp
        
        return dp