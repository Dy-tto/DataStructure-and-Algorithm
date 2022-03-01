# BOJ No.11279
# 최대 힙

import heapq
import sys
lst=[]
n=int(sys.stdin.readline())

for i in range(n):
    num=int(sys.stdin.readline())
    if num>0:
        heapq.heappush(lst,-num)
    else:
        if lst==[]:
            print(0)
        else:
            print(-heapq.heappop(lst))


