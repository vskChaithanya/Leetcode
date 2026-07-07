class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ans=[]
        sum=0
        while n>0:
            digit=n%10
            if digit!=0:
                ans.append(digit)
                sum+=digit
            n=n//10
        x=0
        for i in ans[::-1]:
            x=x*10+i
        return x * sum
