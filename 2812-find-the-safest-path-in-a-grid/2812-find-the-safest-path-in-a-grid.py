class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dist=[[-1]*n for _ in range(n)]
        q=[]
        front=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    dist[i][j]=0
                    q.append((i,j))
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        while front<len(q):
            x,y=q[front]
            front+=1
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
        def can(k):
            if dist[0][0]<k or dist[n-1][n-1]<k:
                return False
            vis=[[False]*n for _ in range(n)]
            q=[(0,0)]
            front=0
            vis[0][0]=True
            while front<len(q):
                x,y=q[front]
                front+=1
                if x==n-1 and y==n-1:
                    return True
                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<n and not vis[nx][ny] and dist[nx][ny]>=k:
                        vis[nx][ny]=True
                        q.append((nx,ny))
            return False
        lo=0
        hi=0
        for row in dist:
            for d in row:
                if d>hi:
                    hi=d
        ans=0
        while lo<=hi:
            mid=(lo+hi)//2
            if can(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans