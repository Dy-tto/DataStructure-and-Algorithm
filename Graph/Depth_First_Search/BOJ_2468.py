# BOJ No.2468
# 안전 영역

import copy
import sys
sys.setrecursionlimit(100000)

def dfs(x,y,graph):
    if x<0 or y<0 or x>=n or y>=n:
        return False

    if graph[x][y]>0:
        graph[x][y]=0

        for i in range(4):
            dfs(x+dx[i],y+dy[i],graph)
        return True
    return False

n=int(sys.stdin.readline())
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
max_height=0
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    max_height=max(max_height,max(graph[i]))

# 잠긴 지역이 없을 수 있으므로 1부터 시작
result=1
# 높이별로 안전 영역 구하기
for h in range(1,max_height):
    cnt=0
    graph_copy=copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph_copy[i][j]<=h:
                graph_copy[i][j]=0

    for i in range(n):
        for j in range(n):
            if dfs(i,j,graph_copy)==True:
                cnt+=1
    result=max(result,cnt)
print(result)
