# BOJ No.2667
# 단지번호붙이기

def dfs(x,y):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        global cnt
        cnt+=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)

        return True
    return False
N=int(input())
graph=[]
result=0
cnts=[]
cnt=0
for _ in range(N):
    graph.append(list(map(int,input())))

for i in range(N):
    for j in range(N):
        if dfs(i,j)==True:
            result+=1
            cnts.append(cnt)
            cnt=0
print(result)
cnts.sort()
for i in range(len(cnts)):
    print(cnts[i])
