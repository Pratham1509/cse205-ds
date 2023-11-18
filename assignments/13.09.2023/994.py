class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid) #row
        n=len(grid[0])#col
        que=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:#if rotten
                    que.append((i,j))
        que.append(None)
        time=0
        while len(que)>1:
            popped_ele = que.pop(0)
            if popped_ele== None:
                time+=1
                que.append(None)
                continue
            i=popped_ele[0]
            j=popped_ele[1]
            if (0 <= i+1 < m) and (grid[i+1][j]==1):
                que.append((i+1,j))
                grid[i+1][j]=2
            if (0 <= i-1 < m) and (grid[i-1][j]==1):
                que.append((i-1,j))
                grid[i-1][j]=2
            if (0 <= j+1 < n) and (grid[i][j+1]==1):
                que.append((i,j+1))
                grid[i][j+1]=2
            if (0 <= j-1 < n) and (grid[i][j-1]==1):
                que.append((i,j-1))
                grid[i][j-1]=2
            #if all oranges are fresh then just return -1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1 
        return time