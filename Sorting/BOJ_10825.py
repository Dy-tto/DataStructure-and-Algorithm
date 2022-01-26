# BOJ No.10825
# 국영수

import sys

n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    name,language,english,mathematics=sys.stdin.readline().split()
    lst.append((name,language,english,mathematics))
lst.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x))
for j in lst:
    print(j[0])
