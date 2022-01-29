# BOJ No.7562
# 나이트의 이동

from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(len(moves)):
            nx=x+moves[i][0]
            ny=y+moves[i][1]
            if nx<0 or ny<0 or nx>=l or ny>=l:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                if (nx,ny)==(targetX,targetY):
                    return graph[nx][ny]
                queue.append((nx,ny))

t=int(input())
for _ in range(t):
    l=int(input())
    graph=[]

    for i in range(l):
        graph.append(list(map(int,'1'*l)))
    moves=[(-2, -1), (-2, 1),
            (2, -1), (2, 1),
            (-1, -2), (1, -2),
            (1, 2), (-1, 2)]
    x,y=map(int,input().split())
    targetX,targetY=map(int,input().split())
    if (x,y)==(targetX,targetY):
        print(0)
    else:
        print(bfs(x,y)-1)


