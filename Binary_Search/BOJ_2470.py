# BOJ No.2470
# 두 용액

n=int(input())
lst=list(map(int,input().split()))
lst.sort()

result=10**10
start=0
end=n-1
ans=[]
while start<end:
    left=lst[start]
    right=lst[end]

    total=left+right

    if abs(total)<result:
        result=abs(total)
        ans=[left,right]
    if total<0:
        start+=1
    else:
        end-=1
print(ans[0],ans[1])

