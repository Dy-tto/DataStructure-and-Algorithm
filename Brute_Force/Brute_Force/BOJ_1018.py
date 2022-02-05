# BOJ No.1018
# 체스판 다시 칠하기

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input()))
result=[]

for nn in range(n-7):
    for mm in range(m-7):
        cnt1=0
        cnt2=0
        for i in range(nn,nn+8):
            for j in range(mm,mm+8):
                if (i+j)%2==0:
                    if graph[i][j] !='W':
                        cnt1+=1
                    if graph[i][j] !='B':
                        cnt2+=1
                else:
                    if graph[i][j] !='B':
                        cnt1+=1
                    if graph[i][j] !='W':
                        cnt2+=1
        result.append(cnt1)
        result.append(cnt2)
print(min(result))



