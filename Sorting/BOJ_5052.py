# BOJ No.5052
# 전화번호 목록

import sys

t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    lst=[]
    check=True
    for _ in range(n):
        lst.append(sys.stdin.readline().rstrip())
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i] in lst[i+1][:len(lst[i])]:
            check=False
            break
    if check==False:
        print('NO')
    else:
        print('YES')
