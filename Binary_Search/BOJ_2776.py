# BOJ No.2776
# 암기왕

import sys

def binary_search(lst,n):
    start=0
    end=len(lst)-1
    result=0
    while start<=end:
        mid=(start+end)//2
        if n>lst[mid]:
            start=mid+1
        elif n<lst[mid]:
            end=mid-1
        else:
            result=1
            break
    return result

t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())

    lst1=list(map(int,sys.stdin.readline().split()))
    lst1.sort()
    m=int(sys.stdin.readline())
    lst2=list(map(int,sys.stdin.readline().split()))
    for i in range(len(lst2)):
        print(binary_search(lst1,lst2[i]))
