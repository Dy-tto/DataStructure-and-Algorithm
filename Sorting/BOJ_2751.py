import sys
lst=[]
for _ in range(9):
    num=int(sys.stdin.readline())
    lst.append(num)
lst.sort()
for i in lst:
    print(i)
