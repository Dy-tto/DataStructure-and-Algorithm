# BOJ No.1939
# 중량제한

import sys
from collections import deque

def bfs(target):
    queue=deque([island1])
    visited=[0 for _ in range(n+1)]
    visited[island1]=1
    while queue:
        v=queue.popleft()
        if v==island2:
            return True
        for b,c in graph[v]:
            if not visited[b] and c>=target:
                visited[b]=1
                queue.append(b)
    return False
def binary_search():
    start=0
    end=max_c
    while start<=end:
        mid=(start+end)//2
        if bfs(mid)==True:
            result=mid
            start=mid+1
        else:
            end=mid-1
    return result

n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
max_c=-1
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    max_c=max(c,max_c)
island1,island2=map(int,sys.stdin.readline().split())
weights=[]
print(binary_search())
