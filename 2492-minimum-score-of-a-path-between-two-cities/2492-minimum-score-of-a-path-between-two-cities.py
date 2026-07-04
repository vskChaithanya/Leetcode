class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=[[]for _ in range(n+1)]
        for u,v,d in roads:
            graph[u].append((v,d))
            graph[v].append((u,d))
        vis=[False]*(n+1)
        ans=10**9
        def dfs(x):
            nonlocal ans
            vis[x]=True
            for y,d in graph[x]:
                ans=min(ans,d)
                if not vis[y]:
                    dfs(y)
        dfs(1)
        return ans