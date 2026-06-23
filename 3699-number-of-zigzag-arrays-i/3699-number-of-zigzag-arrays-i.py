class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD=10**9+7
        m=r-l+1
        up=[0]*(m+1)
        down=[0]*(m+1)
        for i in range(1,m+1):
            up[i]=i-1
            down[i]=m-i
        for _ in range(3,n+1):
            nu=[0]*(m+1)
            nd=[0]*(m+1)
            s=0
            for i in range(1,m+1):
                nu[i]=s
                s=(s+down[i])%MOD
            s=0
            for i in range(m,0,-1):
                nd[i]=s
                s=(s+up[i])%MOD
            up=nu
            down=nd
        return (sum(up)+sum(down))%MOD