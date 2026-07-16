from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix=[]
        maxi=0
        for i in nums:
            maxi=max(maxi,i)
            prefix.append(gcd(i,maxi))
        prefix.sort()
        ans=0
        n=len(prefix)
        for i in range(n//2):
            ans+=gcd(prefix[i],prefix[n-1-i])
        return ans