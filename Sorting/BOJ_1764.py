# BOJ No.1764
# 듣보잡

import sys

n,m=map(int,sys.stdin.readline().split())
see=set()
listen=set()
for i in range(n):
    see.add(sys.stdin.readline().rstrip())
for i in range(m):
    listen.add(sys.stdin.readline().rstrip())
sl=sorted(list(see & listen))
print(len(sl))
for i in range(len(sl)):
    print(sl[i])
