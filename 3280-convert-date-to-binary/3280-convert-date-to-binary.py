class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ans=[]
        for i in date.split("-"):
            ans.append(bin(int(i))[2:])
        return "-".join(ans)