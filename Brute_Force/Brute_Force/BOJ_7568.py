# BOJ_7568
# 덩치

N=int(input())
people=[]
for n in range(N):
    x,y=map(int,input().split())
    people.append((x,y))

for p in people:
    rank=1
    for k in people:
        if p[0]<k[0] and p[1] <k[1]:
            rank+=1
    print(rank,end=' ')

