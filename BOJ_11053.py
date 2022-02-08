# BOJ No.11053
# 가장 긴 증가하는 부분 수열

n=int(input())

d=[1]*1001
lst=list(map(int,input().split()))

for i in range(n):
    for j in range(i):
        if lst[j]<lst[i]:
            d[i+1]=max(d[j+1]+1,d[i+1])
print(max(d))
