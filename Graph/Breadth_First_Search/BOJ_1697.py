# BOJ No.1697
# 숨바꼭질

from collections import deque

def bfs(x):
    queue=deque()
    queue.append(x)

    while queue:
        x=queue.popleft()
        if x==k:
            print(graph[x])
            break
        for nx in [x-1,x+1,x*2]:
            if nx<0 or nx>100000:
                continue
            elif not graph[nx]:
                graph[nx]=graph[x]+1
                queue.append(nx)


n,k=map(int,input().split())
graph=[0]*100001

bfs(n)
