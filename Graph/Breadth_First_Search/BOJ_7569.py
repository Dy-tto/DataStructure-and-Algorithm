# BOJ No.7569
# 토마토

from collections import deque

M,N,H=map(int,input().split())

graph=[[[0 for i in range(M)] for j in range(N)] for k in range(H)]
for i in range(H):
    for j in range(N):
        lst=list(input().split())
        for k in range(M):
            graph[i][j][k]=int(lst[k])

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
queue=deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k]==1:
                queue.append((i,j,k))
def bfs():
    while queue:
        z,x,y=queue.popleft()

        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=N or ny>=M or nz>=H:
                continue
            if graph[nz][nx][ny]==0:
                graph[nz][nx][ny]=graph[z][x][y]+1
                queue.append((nz,nx,ny))
bfs()
result=0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        for k in range(len(graph[i][j])):
            if graph[i][j][k]==0:
                print(-1)
                exit(0)
        result=max(result,max(graph[i][j]))
print(result-1)
