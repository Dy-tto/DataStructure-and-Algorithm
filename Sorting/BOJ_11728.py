# BOJ No.11728
# 배열 합치기

import sys

n,m=map(int,sys.stdin.readline().split())
lst=[]
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
for i in a:
    lst.append(i)
for j in b:
    lst.append(j)

lst.sort()
for i in lst:
    print(i,end=' ')
