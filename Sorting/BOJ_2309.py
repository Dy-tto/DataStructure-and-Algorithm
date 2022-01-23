# BOJ No.2309
# 일곱 난쟁이

import sys
from itertools import combinations as cb
lst=[]
for _ in range(9):
    num=int(sys.stdin.readline())
    lst.append(num)
com=cb(lst,7)
for i in com:
    if sum(i)==100:
        lst=list(i)
        break
lst.sort()
for i in lst:
    print(i)
