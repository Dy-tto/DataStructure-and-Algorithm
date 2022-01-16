# BOJ No.13305
# 주유소

N=int(input())
length=list(map(int,input().split()))
cities=list(map(int,input().split()))

price=0
m=cities[0]
for i in range(N-1):
    if cities[i]<m:
        m=cities[i]
    price+=m*length[i]
print(price)
