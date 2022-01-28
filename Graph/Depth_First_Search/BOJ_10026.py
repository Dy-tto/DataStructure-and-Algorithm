# BOJ No.10026
# 적록 색약

import sys

sys.setrecursionlimit(10**6)

n=int(sys.stdin.readline())
graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y,color):
    if x<0 or y<0 or x>=n or y>=n:
        return False

    if visited[x][y]==False:
        if graph[x][y]==color:
            visited[x][y]=True
            for i in range(4):
                dfs(x+dx[i],y+dy[i],color)
            return True
    return False

result=0
for _ in range(n):
    graph.append(list(sys.stdin.readline()))
visited=[[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs(i,j,graph[i][j])==True:
            result+=1
result1=0

for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'
visited=[[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs(i,j,graph[i][j])==True:
            result1+=1
print(result, result1)
