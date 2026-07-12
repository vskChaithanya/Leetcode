class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans=sorted(nums)
        for i in range(0,len(ans),2):
                ans[i],ans[i+1]=ans[i+1],ans[i]
        return ans