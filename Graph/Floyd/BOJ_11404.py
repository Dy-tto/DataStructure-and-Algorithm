
import sys
def floyd(n, d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j]>d[i][k]+d[k][j] and i!=j:
                    d[i][j]=d[i][k]+d[k][j]
    for i in d:
        for j in i:
            if j==inf:
                print(0,end=' ')
            else:
                print(j,end=' ')
        print()


n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
inf=1000000000
graph=[[inf for i in range(n)] for j in range(n)]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if graph[a-1][b-1]>c:
        graph[a-1][b-1]=c

floyd(n,graph)


