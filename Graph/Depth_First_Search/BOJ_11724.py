# BOJ No.11724
# 연결 요소의 개수

import sys
sys.setrecursionlimit(10000)

N,M=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
cnt=0
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,start,visited):
    visited[start]=True
    for i in graph[start]:
        if visited[i]==False:
            dfs(graph,i,visited)

for i in range(1,len(visited)):
    if visited[i]==False:
        cnt+=1
        dfs(graph,i,visited)
print(cnt)
