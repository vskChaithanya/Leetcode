class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans=len(arr)//4
        for i in arr:
            if freq[i]>ans:
                return i