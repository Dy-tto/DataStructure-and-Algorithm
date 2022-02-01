# BOJ No.16953
# A -> B

from collections import deque

def cal(a,b,cnt):
    queue=deque()
    queue.append((a,cnt))
    while queue:
        a,cnt=queue.popleft()
        if a>b:
           continue
        if a==b:
            print(cnt)
            break
        queue.append((10*a+1,cnt+1))
        queue.append((2*a,cnt+1))
    else:
        print(-1)

a,b=map(int,input().split())

cnt=1

cal(a,b,cnt)
