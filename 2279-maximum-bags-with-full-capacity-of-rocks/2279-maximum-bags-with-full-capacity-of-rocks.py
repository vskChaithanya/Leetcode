class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ans=[]
        for i in range(len(capacity)):
            need=capacity[i]-rocks[i]
            ans.append(need)
        ans.sort()
        count=0
        for i in ans:
            if additionalRocks>=i:
                additionalRocks=additionalRocks-i
                count+=1
            else:
                break
        return count