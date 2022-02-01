# BOJ No.2110
# 공유기 설치
import sys

n,c=map(int,sys.stdin.readline().split())
lst=[]
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()
start=1
end=max(lst)-min(lst)

result=0

while start<=end:
    mid=(start+end)//2
    cnt=1
    current=lst[0]
    # 현재 값 + 간격 <= 다음 값 이면 공유기 설치
    for i in lst:
        if i>=mid+current:
            cnt+=1
            current=i
    if cnt<c:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)
