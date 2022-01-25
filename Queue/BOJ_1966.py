# BOJ No.1966
# 프린터 큐

from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    priority=deque(list(map(int,input().split())))
    idx_pri=deque(list(range(n)))
    cnt=0

    while priority:
        if priority[0]==max(priority):
            cnt+=1
            priority.popleft()
            if idx_pri.popleft()==m:
                print(cnt)
        else:
            priority.append(priority.popleft())
            idx_pri.append(idx_pri.popleft())


