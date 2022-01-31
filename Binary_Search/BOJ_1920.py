# BOJ No.1920
# 수 찾기

def binary_search(lst,target,start,end):
    while start<=end:
        mid=(start+end)//2

        if lst[mid]==target:
            return 1
        elif lst[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return 0

n=int(input())
lst=list(map(int,input().split()))

m=int(input())
arr=list(map(int,input().split()))

lst.sort()

for i in arr:
    print(binary_search(lst,i,0,len(lst)-1))
