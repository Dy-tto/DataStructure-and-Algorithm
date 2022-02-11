# BOJ No.2343
# 기타 레슨

n,m=map(int,input().split())
lst=list(map(int,input().split()))

start=max(lst)
end=sum(lst)

result=end
while start<=end:
    mid=(start+end)//2
    total=0
    slice=0
    for i in lst:
        if slice+i>mid:
            total+=1
            slice=0
        slice+=i
    if slice!=0:
        total+=1
    if total>m:
        start=mid+1
    else:
        result=min(result,mid)
        end=mid-1
print(result)

