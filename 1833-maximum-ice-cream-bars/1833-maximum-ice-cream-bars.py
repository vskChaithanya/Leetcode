class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost=max(costs)
        freq=[0]*(max_cost+1)
        for cost in costs:
            freq[cost]+=1
        bars=0
        for i in range(1,max_cost+1):
            while freq[i]>0 and coins>=i:
                coins-=i
                bars+=1
                freq[i]-=1
        return bars