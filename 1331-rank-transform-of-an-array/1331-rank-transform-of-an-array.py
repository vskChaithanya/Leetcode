class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        '''ans=sorted(set(arr))
        a=[]
        for i in arr:
            if i in ans:
                a.append(ans.index(i)+1)
        return a'''
        # Time Limit Exceeded
        ans=sorted(set(arr))
        index={}
        for i in range(len(ans)):
            index[ans[i]]=i+1
        a=[]
        for i in arr:
            a.append(index[i])
        return a