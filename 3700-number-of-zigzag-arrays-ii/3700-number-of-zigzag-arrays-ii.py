class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD=10**9+7
        m=r-l+1
        k=m-1
        K=[[min(i+1,j+1)%MOD for j in range(k)] for i in range(k)]
        def mat_mul(A,B):
            n1,n2,n3=len(A),len(B),len(B[0])
            C=[[0]*n3 for _ in range(n1)]
            for i in range(n1):
                Ai=A[i]
                Ci=C[i]
                for t in range(n2):
                    a=Ai[t]
                    if a==0:
                        continue
                    Bt=B[t]
                    for j in range(n3):
                        Ci[j]=(Ci[j]+a*Bt[j])%MOD
            return C
        def mat_vec(A,v):
            res=[0]*len(A)
            for i,row in enumerate(A):
                s=0
                for a,b in zip(row,v):
                    s=(s+a*b)%MOD
                res[i]=s
            return res
        if n%2==0:
            exp=(n-2)//2
            vec=[i for i in range(1,k+1)]
        else:
            exp=(n-3)//2
            vec=[i*(2*m-i-1)//2 for i in range(1,k+1)]
        M=K
        while exp:
            if exp&1:
                vec=mat_vec(M,vec)
            M=mat_mul(M,M)
            exp>>=1
        return (2*sum(vec))%MOD