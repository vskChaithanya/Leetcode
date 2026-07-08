class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod=1000000007
        p=[]
        d=[]
        for i in range(len(s)):
            if s[i]!="0":
                p.append(i)
                d.append(ord(s[i])-48)
        n=len(d)
        pw=[1]*(n+1)
        for i in range(1,n+1):
            pw[i]=pw[i-1]*10%mod
        val=[0]*(n+1)
        sm=[0]*(n+1)
        for i in range(n):
            val[i+1]=(val[i]*10+d[i])%mod
            sm[i+1]=sm[i]+d[i]
        ans=[]
        for l,r in queries:
            a=0
            b=n
            while a<b:
                m=(a+b)//2
                if p[m]<l:
                    a=m+1
                else:
                    b=m
            left=a
            a=0
            b=n
            while a<b:
                m=(a+b)//2
                if p[m]<=r:
                    a=m+1
                else:
                    b=m
            right=a
            if left==right:
                ans.append(0)
            else:
                ln=right-left
                x=(val[right]-val[left]*pw[ln])%mod
                ans.append(x*(sm[right]-sm[left])%mod)
        return ans