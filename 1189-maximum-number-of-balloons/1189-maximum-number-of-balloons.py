class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        for i in text:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        target="balloon"
        freq1={}
        for i in target:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        ans=float('inf')
        for i in freq1:
            if i not in freq:
                return 0
            ans=min(ans,freq[i]//freq1[i])
        return ans