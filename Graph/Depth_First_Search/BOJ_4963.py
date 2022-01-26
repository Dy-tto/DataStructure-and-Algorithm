# BOJ No.4963
# 섬의 개수

import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x<0 or y<0 or x>=h or y>=w:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        for i in range(8):
            dfs(x+dx[i],y+dy[i])
        return True
    return False
# 방향벡터
dx=[-1,1,0,0,1,1,-1,-1]
dy=[0,0,-1,1,1,-1,1,-1]

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    result=0
    graph=[]
    for i in range(h):
        graph.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==True:
                result+=1
    print(result)

