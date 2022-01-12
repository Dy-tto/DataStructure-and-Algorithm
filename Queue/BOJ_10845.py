# BOJ No.10845
# 큐

import sys
from collections import deque
def push(lst:deque,
         x:int):
    lst.append(x)
    return lst

def size(lst:deque):
    return print(len(lst))

def empty(lst:deque):
    if len(lst)==0:
        print('1')
    else:
        print('0')

def front(lst:deque):
    if len(lst)==0:
        print(-1)
    else:
        print(lst[0])

def back(lst:deque):
    if len(lst)==0:
        print(-1)
    else:
        print(lst[-1])

N=int(sys.stdin.readline())
queue=deque()

for _ in range(N):
    inp=list(sys.stdin.readline().split())
    if inp[0]=='push':
        push(queue,inp[1])
    elif inp[0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif inp[0]=='size':
        size(queue)
    elif inp[0]=='empty':
        empty(queue)
    elif inp[0]=='back':
        back(queue)
    elif inp[0]=='front':
        front(queue)
