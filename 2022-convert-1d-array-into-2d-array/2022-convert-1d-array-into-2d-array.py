class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=n*m:
            return []
        ans=[]
        for i in range(m):
            start=i*n
            end=start+n
            ans.append(original[start:end])
        return ans