class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            if i>0:
                ans.append(i)
        s=set(ans)
        if len(s)>0:
            return sum(s)
        return max(nums)