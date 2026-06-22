class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if i<j and abs(nums[i]-nums[j])==k:
                    count+=1
        return count