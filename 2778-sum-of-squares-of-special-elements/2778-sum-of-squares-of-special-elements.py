class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[]
        for i in range(n):
            if n%(i+1)==0:
                a=nums[i]**2
                ans.append(a)
        return sum(ans)
