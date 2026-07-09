class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        ans=[0]*n
        cid=0
        for i in range(1,n):
            if nums[i]-nums[i-1]>maxDiff:
                cid+=1
            ans[i]=cid
        return [ans[u]==ans[v] for u, v in queries]