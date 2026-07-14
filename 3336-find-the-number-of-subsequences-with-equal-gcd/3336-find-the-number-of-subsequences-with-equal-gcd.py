class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod=1000000007
        m=max(nums)
        dp=[[0]*(m+1)for _ in range(m+1)]
        dp[0][0]=1
        for x in nums:
            ndp=[r[:]for r in dp]
            for i in range(m+1):
                for j in range(m+1):
                    if dp[i][j]:
                        if i==0:
                            a=x
                        else:
                            a=i
                            b=x
                            while b:
                                a,b=b,a%b
                        ndp[a][j]=(ndp[a][j]+dp[i][j])%mod
                        if j==0:
                            c=x
                        else:
                            c=j
                            b=x
                            while b:
                                c,b=b,c%b
                        ndp[i][c]=(ndp[i][c]+dp[i][j])%mod
            dp=ndp
        ans=0
        for i in range(1,m+1):
            ans=(ans+dp[i][i])%mod
        return ans
        