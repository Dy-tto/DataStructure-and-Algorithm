# BOJ No.1149
# RGB 거리

n=int(input())
d=[[0,0,0] for _ in range(n+1)]
houses=[]
for i in range(n):
    r,g,b=map(int,input().split())
    houses.append((r,g,b))
d[1][0],d[1][1],d[1][2]=houses[0]

for i in range(2,n+1):
    d[i][0]=min(d[i-1][1],d[i-1][2])+houses[i-1][0]
    d[i][1]=min(d[i-1][0],d[i-1][2])+houses[i-1][1]
    d[i][2]=min(d[i-1][0],d[i-1][1])+houses[i-1][2]

print(min(d[n]))
