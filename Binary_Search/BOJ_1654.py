# BOJ No.1654
# 랜선 자르기

import sys

k,n=map(int,sys.stdin.readline().split())

lst=[]
for i in range(k):
    lst.append(int(input()))

start=1
end=max(lst)
result=0

while start<=end:
    total=0
    mid=(start+end)//2
    for i in lst:
        if i>=mid:
           total+=i//mid
    if total<n:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)
