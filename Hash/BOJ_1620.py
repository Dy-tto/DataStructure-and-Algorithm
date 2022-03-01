# BOJ No.1620
# 나는야 포켓몬 마스터 이다솜

import sys

n,m=map(int,sys.stdin.readline().split())

lst={}
for i in range(n):
    lst[i]=(sys.stdin.readline().rstrip())
    lst[lst[i]]=i

for j in range(m):
    prob=sys.stdin.readline().rstrip()
    if prob.isdigit():
        print(lst[int(prob)-1])
    else:
        print(lst[prob]+1)
