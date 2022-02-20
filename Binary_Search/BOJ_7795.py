# BOJ No.7795
# 먹을 것인가 먹힐 것인가

from bisect import bisect_right
import sys

def bisect_lst(nums,left,right):
    l=bisect_right(nums,left)
    r=bisect_right(nums,right)

    return r-l

t=int(sys.stdin.readline())

for _ in range(t):
    n,m=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    b=list(map(int,sys.stdin.readline().split()))
    a.sort()
    cnt=0
    for i in range(len(b)):
        cnt+=bisect_lst(a,b[i],a[-1])
    print(cnt)


