# BOJ No.10828
# 스택

import sys

def push(lst:list,
         x:int):
    lst.append(x)
    return lst

def size(lst:list):
    return print(len(lst))

def empty(lst:list):
    if lst==[]:
        print('1')
    else:
        print('0')
def top(lst:list):
    if lst==[]:
        print(-1)
    else:
        print(lst[-1])

N=int(sys.stdin.readline())
stack=[]

for _ in range(N):
    inp=list(sys.stdin.readline().split())
    if inp[0]=='push':
        push(stack,inp[1])
    elif inp[0]=='pop':
        if stack==[]:
            print(-1)
        else:
            print(stack.pop())
    elif inp[0]=='size':
        size(stack)
    elif inp[0]=='empty':
        empty(stack)
    elif inp[0]=='top':
        top(stack)
