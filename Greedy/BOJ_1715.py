# BOJ No.1715
# 카드 정렬하기

from queue import PriorityQueue
import sys

q=PriorityQueue()

n=int(sys.stdin.readline())
for i in range(n):
    q.put(int(sys.stdin.readline()))
result=0
while True:
    if q.qsize()==1:
        break
    a=q.get()
    b=q.get()
    result+=a+b
    q.put(a+b)
print(result)
