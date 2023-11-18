class Solution:
    def solve(self, b: List[List[str]]) -> None:
        m=len(b)
        n=len(b[0])
        def dfs(i,j):
            if b[i][j]=="O":
                b[i][j]="P"
                if i<m-1:
                    dfs(i+1,j)
                if i>0:
                    dfs(i-1,j)
                if j<n-1:
                    dfs(i,j+1)
                if j>0:
                    dfs(i,j-1)
        for i in [0,m-1]:
            for j in range(n):
                dfs(i,j)
        for j in [0,n-1]:
            for i in range(m):
                dfs(i,j)
        for i in range(m):
            for j in range(n):
                if b[i][j]=="O":
                    b[i][j]="X"
        for i in range(m):
            for j in range(n):
                if b[i][j]=="P":
                    b[i][j]="O"



            