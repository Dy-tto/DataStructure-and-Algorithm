# BOJ No.1260
# DFS와 BFS

from collections import deque

def dfs(graph,start,visited):
    visited[start]=True
    print(start,end=' ')

    for i in graph[start]:
        if visited[i]==False:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True

n, m, v = map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m): # 인접행렬을 그래프 형태로 저장
    p1,p2=map(int,input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
for i in range(1,n+1):
    graph[i].sort()

visited=[False]*(n+1)
visited2=[False]*(n+1)
dfs(graph,v,visited)
print()
bfs(graph,v,visited2)
