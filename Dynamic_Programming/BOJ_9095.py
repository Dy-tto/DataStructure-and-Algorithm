# BOJ No.9095
# 1,2,3 더하기

t=int(input())
cache=[0]*11
cache[1]=1
cache[2]=2
cache[3]=4
for i in range(4,11):
    cache[i]=sum(cache[i-3:i])
for _ in range(t):
    n=int(input())
    print(cache[n])
