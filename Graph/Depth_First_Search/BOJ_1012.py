# BOJ No.1012
# 유기농 배추

import sys
sys.setrecursionlimit(10**8)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(y,x):
    if x<0 or y<0 or x>=m or y>=n:
        return False
    if graph[y][x]==1:
        graph[y][x]=0

        for i in range(4):
            dfs(y+dy[i],x+dx[i])
        return True
    return False

T=int(input())
for t in range(T):
    m,n,k=map(int,input().split())
    result=0
    graph=[[0]*m for i in range(n)]
    for i in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1
    for j in range(n):
        for p in range(m):
            if dfs(j,p)==True:
                result+=1
    print(result)

