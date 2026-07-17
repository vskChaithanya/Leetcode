class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m=max(nums)
        f=[0]*(m+1)
        for x in nums:
            f[x]+=1
        c=[0]*(m+1)
        for i in range(1,m+1):
            if f[i]==0:
                continue
            d=1
            while d*d<=i:
                if i%d==0:
                    c[d]+=f[i]
                    if d!=i//d:
                        c[i//d]+=f[i]
                d+=1
        e=[0]*(m+1)
        for i in range(m,0,-1):
            p=c[i]*(c[i]-1)//2
            j=i*2
            while j<=m:
                p-=e[j]
                j+=i
            e[i]=p
        pre=[0]
        for i in range(1,m+1):
            pre.append(pre[-1]+e[i])
        ans=[]
        for q in queries:
            l=1
            r=m
            while l<=r:
                mid=(l+r)//2
                if pre[mid]>q:
                    r=mid-1
                else:
                    l=mid+1
            ans.append(l)
        return ans