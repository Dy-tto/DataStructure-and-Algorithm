# BOJ_1158
# 요세푸스 문제

from collections import deque
import sys
N,K=map(int,sys.stdin.readline().split())

queue=deque(list(range(1,N+1)))
result=deque()

cnt=0
while len(queue)!=0:
    person=queue.popleft()
    cnt+=1
    if cnt%K!=0:
        queue.append(person)
    else:
        result.append(str(person))

print("<",", ".join(result)[:],">",sep='')
