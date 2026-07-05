class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n=len(board)
        mod=1000000007
        neg=-10**9
        s=[[neg]*n for _ in range(n)]
        w=[[0]*n for _ in range(n)]
        s[n-1][n-1]=0
        w[n-1][n-1]=1
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if board[i][j]=="X"or(i==n-1 and j==n-1):
                    continue
                b=neg
                c=0
                for x,y in((i+1,j),(i,j+1),(i+1,j+1)):
                    if x<n and y<n:
                        if s[x][y]>b:
                            b=s[x][y]
                            c=w[x][y]
                        elif s[x][y]==b and b!=neg:
                            c=(c+w[x][y])%mod
                if b==neg:
                    continue
                a=0
                if board[i][j].isdigit():
                    a=int(board[i][j])
                s[i][j]=b+a
                w[i][j]=c
        if w[0][0]==0:
            return[0,0]
        return[s[0][0],w[0][0]]