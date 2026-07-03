class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n=len(online)
        g=[[]for _ in range(n)]
        ind=[0]*n
        mx=0
        for u,v,c in edges:
            g[u].append((v,c))
            ind[v]+=1
            if c>mx:
                mx=c
        q=[]
        h=0
        for i in range(n):
            if ind[i]==0:
                q.append(i)
        topo=[]
        while h<len(q):
            u=q[h]
            h+=1
            topo.append(u)
            for v,c in g[u]:
                ind[v]-=1
                if ind[v]==0:
                    q.append(v)
        inf=10**30
        def ok(x):
            d=[inf]*n
            d[0]=0
            for u in topo:
                if u!=0 and u!=n-1 and not online[u]:
                    continue
                if d[u]==inf:
                    continue
                for v,c in g[u]:
                    if c<x:
                        continue
                    if v!=0 and v!=n-1 and not online[v]:
                        continue
                    nd=d[u]+c
                    if nd<d[v]:
                        d[v]=nd
            return d[n-1]<=k
        if not ok(0):
            return -1
        l=0
        r=mx
        while l<r:
            m=(l+r+1)//2
            if ok(m):
                l=m
            else:
                r=m-1
        return l