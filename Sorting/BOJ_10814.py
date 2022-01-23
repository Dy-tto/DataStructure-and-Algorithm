# BOJ No.10814
# 나이순 정렬

import sys

n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    age,name=sys.stdin.readline().split()
    age=int(age)
    lst.append((i,age,name))
lst.sort(key=lambda x: (x[1],x[0]))
for i in range(n):
    print(lst[i][1],lst[i][2],sep=' ')
