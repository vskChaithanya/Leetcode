class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans=cost[::-1]
        q=[]
        for i in range(len(ans)):
            if (i+1)%3!=0:
                q.append(ans[i])
        return sum(q)