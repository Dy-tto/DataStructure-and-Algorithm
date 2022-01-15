# BOJ No.2606
# 바이러스

def dfs(graph,v,visited):
    visited[v]=True
    global cnt

    for i in graph[v]:
        if visited[i]==False:
            cnt+=1
            dfs(graph,i,visited)

C=int(input())
N=int(input())
graph=[[] for _ in range(C+1)]
visited=[False]*(C+1)
cnt=0

for i in range(N):
    p,s=map(int,input().split())
    graph[p].append(s)
    graph[s].append(p)

dfs(graph,1,visited)
print(cnt)
