# BOJ No.11866
# 요세푸스 문제 0

from collections import deque

n,k=map(int,input().split())
queue=deque(list(range(1,n+1)))
lst=[]
cnt=0
while queue:
    p=queue.popleft()
    cnt+=1
    if cnt%k==0:
        lst.append(p)
    else:
        queue.append(p)
print('<',end='')
for i in range(len(lst)):
    print(lst[i],end='')
    if i==n-1:
        print('>')
    else:
        print(',',end=' ')

