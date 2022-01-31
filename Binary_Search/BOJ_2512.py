# BOJ No.2512
# 예산

n=int(input())
lst=list(map(int,input().split()))
m=int(input())

start=0
end=max(lst)
result=0

while start<=end:
    mid=(start+end)//2
    total=0

    for i in lst:
        if i<=mid:
            total+=i
        elif i>mid:
            total+=mid
    if total>m:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)
