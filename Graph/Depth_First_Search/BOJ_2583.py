# BOJ No.2583
# 영역 구하기

import sys
sys.setrecursionlimit(10**6)

m, n, k=map(int,sys.stdin.readline().split())
graph=[[1 for _ in range(n)] for _ in range(m)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
def dfs(y,x):
    global cnt
    if x<0 or y<0 or x>=n or y>=m:
        return False
    if graph[y][x]==1:
        graph[y][x]=0
        cnt+=1
        for i in range(4):
            dfs(y+dx[i],x+dy[i])
        return True
    return False

for _ in range(k):
    lowerX,lowerY,upperX,upperY=map(int,sys.stdin.readline().split())

    for col in range(lowerY,upperY):
        for row in range(lowerX,upperX):
            graph[col][row]=0

areas=[]
result=0
for i in range(m):
    for j in range(n):
        if dfs(i,j)==True:
            result+=1
            areas.append(cnt)
            cnt=0
areas.sort()
print(result)
for i in areas:
    print(i,end=' ')
