class Solution:
    def countAsterisks(self, s: str) -> int:
        asterisks=0
        line=0
        for i in s:
            if i=='|':
                line+=1
            elif i=='*':               
                if line%2==0:
                    asterisks+=1
        return asterisks