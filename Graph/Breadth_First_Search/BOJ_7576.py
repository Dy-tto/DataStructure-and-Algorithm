# BOJ No.7576
# 토마토

from collections import deque

M,N=map(int,input().split())

graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
# 방향벡터
dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque()
# 1이 여러개 있을 때 동시에 출발하기 위해 queue에 다 저장
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            queue.append((i,j))
def bfs():
    while queue:
        x,y=queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            # 한 사이클 돌 때마다 값을 증가시켜서 일 수 계산
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
bfs()

result=0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    # 저장된 값 중 가장 큰 값이 걸린 일 수
    result=max(result,max(i))
# 시작 값이 1 이기 때문에 1 빼줌
print(result-1)

